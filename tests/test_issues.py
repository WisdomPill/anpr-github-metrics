from random import choice
from time import sleep
from unittest import TestCase

import settings
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.query import Term
from faker import Faker
from github import Github, GithubObject

from utils import get_response_dict


class TestIssues(TestCase):
    @classmethod
    def setUpClass(cls):
        user = settings.GITHUB['user']
        passwd = settings.GITHUB['passwd']
        cls.github = Github(user, passwd)
        cls.faker = Faker('it_IT')
        repo_name = settings.GITHUB['repo']
        cls.repo = cls.github.get_repo(repo_name)
        connections.configure(**settings.ELASTICSEARCH)
        cls.es = connections.get_connection()
        # TODO add template

    @staticmethod
    def get_search_kwargs():
        return {
            'doc_type': 'issue_comment_event',
            'index': 'githubs'
        }

    def tearDown(self):
        # comment the following line if you want to keep the data
        # self.es.delete('github-*')
        pass

    def test_close_issue(self):
        """
        lock an issue
        :return:
        """
        issue = self.create_issue()

        issue.edit(state='closed')

        sleep(.5)

        last_issue = self.get_last_issue(state='closed')

        self.assertEqual(last_issue.state, issue.state)

        sleep(.5)

        last_result = self.fetch_events(Term(issue__id=issue.id))

        print('last_result[\'issue\'][\'id\'] -> {}\n last_issue.id -> {}'.format(last_result['issue']['id'], last_issue.id))

        self.assertEqual(last_result['issue']['state'], last_issue.state)

    def test_create_issue(self):
        """
        create new issue and fetch it from elasticsearch
        :return:
        """
        issue = self.create_issue()

        self.assertEqual(self.repo.get_issue(issue.number), issue)

        sleep(.5)

        last_result = self.fetch_events(Term(issue__id=issue.id))

        self.assertEqual(last_result['issue']['id'], issue.id)

    def test_assign_label(self):
        """
        create new issue and add a label
        :return:
        """
        issue = self.create_issue()

        label_names = [l.name for l in self.repo.get_labels()]

        label = choice(label_names)

        issue.add_to_labels(label)

        last_label = issue.get_labels()[0]
        self.assertEqual(last_label.name, label)

        self.fetch_events(Term(issue__id=issue.id))

    def test_add_label(self):
        """
        create new issue and add a label
        :return:
        """
        issue = self.create_issue()

        label = self.repo.create_label(self.faker.word(), self.get_random_safe_color())

        issue.add_to_labels(label)

        last_label = issue.get_labels()[0]
        self.assertEqual(last_label, label)

        self.fetch_events(Term(issue__id=issue.id))

    def get_random_safe_color(self):
        """
        This is because github label colors don't have the hashtag
        :return:
        """
        return self.faker.safe_hex_color().replace('#', '')

    def test_issue_comment(self):
        """
        create new comment and fetch it from elasticsearch
        :return:
        """
        issue = self.create_issue()
        comment = self.comment_issue(issue)

        comments = self.get_last_issue().get_comments()

        self.assertEqual(comments[0].id, comment.id)

        last_result = self.fetch_events(Term(comment__id=comment.id))

        self.assertEqual(last_result['comment']['id'], comment.id)

    def fetch_events(self, query):
        search = Search(**self.get_search_kwargs())
        search = search.query(query)
        search.sort('-@timestamp')
        response = search.execute()
        results = get_response_dict(response)
        return results[0]

    def comment_issue(self, issue):
        return issue.create_comment(self.faker.paragraph(nb_sentences=27, variable_nb_sentences=True))

    def create_issue(self):
        return self.repo.create_issue(self.faker.sentence(nb_words=9, variable_nb_words=True),
                                      self.faker.paragraph(nb_sentences=3, variable_nb_sentences=True))

    def get_last_issue(self, state=GithubObject.NotSet):
        return self.repo.get_issues(state=state)[0]
