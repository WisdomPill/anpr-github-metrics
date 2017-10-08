# GitHub Issues Analytics

Library that show some analytics on GitHub project issues. It is based on Elastic Search, Kibana and Logstash.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You have to install ngrok, check your permission on GitHub (only owners can add a webhook),

You can download Logstash, Kibana and ElasticSearch to test you analytics locally or you can try Docker and Docker Compose.

### Installing

On ngrok, you have to give your _localhost_ address and copy you public ip (which should be something like _https://idgiventoyou.ngrok.io_) on GitHub Webhook menu.

On GitHub project, go to Settings, Webhook, click on "Add Webhook" and paste your **ngrok address**.

With:
* Docker -
* Logstash/Kibana/ElasticSearch -

## Running the tests

The tests are located in /test directory and are written in Python through UnitTest. They are used to create new issues, add comments and add labels.

The contributors can add other tests opening the source

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Elastic Search](https://www.elastic.co/products/elasticsearch) - Analytics engine
* [Kibana](https://www.elastic.co/products/kibana) - Analytics Dashboard
* [LogStash](https://www.elastic.co/products/logstash) - Processing pipeline
* [ngrok](https://ngrok.com/) - Local server on public ip over tunnels
Opt:
* [Docker](https://www.docker.com/) -

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Anas El Amraoui**  - [WisdomPill](https://github.com/WisdomPill)
* **David Marinangeli** - [davidmarinangeli](https://github.com/davidmarinangeli)

## License

This project is an open-source project, built for **ANPR Challenge** in Hack.Developers hackathon for the issue 314 (https://github.com/italia/anpr/issues/314).
