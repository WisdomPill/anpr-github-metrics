FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.2

RUN mkdir /data
COPY alias /data
RUN apt-get update
RUN apt-get install -y httpie
RUN httpie get :9200 > /tmp/test.json