# GitHub Issues Analytics

Library that show some analytics on GitHub project issues. It is based on Elastic Search, Kibana and Logstash.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Download ngrok, check your permission on GitHub (only owners can add a webhook).

Download Logstash, Kibana and ElasticSearch to test you analytics locally or you can try Docker and Docker Compose.

### Installing

On ngrok, you have to write _http://localhost:2727_ and copy the public IP ngrok gave to you (something like _https://idgiventoyou.ngrok.io_) on GitHub Webhook menu.

On GitHub project, go to Settings > Webhook > click on "Add Webhook" and paste your **ngrok address**.

After that:
* With Docker - After inital setup of Docker and Docker Compose, open the project with it. Give command _docker-compose up_ from _compose_ directory.
* With Logstash/Kibana/ElasticSearch - Add the pipeline _compose/logstash/pipeline/github.conf_ inside logstash and start all the services. Then open the "Dev Tools" menu of Kibana and paste the content of _/elastic_setup.txt_ and execute all the queries.

## Running the tests

The tests are located in /test directory and are written in Python through UnitTest: actually they are used to test issue events.

Contributors can add other tests by opening tests/conf directory, opening _settings.py_ file and filling the "GITHUB" dictionary with your GitHub informations.

```
GITHUB = {
    'user': '<user_name>',
    'passwd': '<password>',
    'repo': '<owner>/<repo_name>'
}
 ```

## Built With

* [Elastic Search](https://www.elastic.co/products/elasticsearch) - Analytics engine
* [Kibana](https://www.elastic.co/products/kibana) - Analytics Dashboard
* [LogStash](https://www.elastic.co/products/logstash) - Processing pipeline
* [ngrok](https://ngrok.com/) - Local server on public IP over tunnels
Opt:
* [Docker](https://www.docker.com/) - Software container platform

## Authors

* **Anas El Amraoui**  - [WisdomPill](https://github.com/WisdomPill)
* **David Marinangeli** - [davidmarinangeli](https://github.com/davidmarinangeli)

## License

This project is an open-source project, built for **ANPR Challenge** in Hack.Developers hackathon for the issue 314 (https://github.com/italia/anpr/issues/314).
