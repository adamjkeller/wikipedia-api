# Wikipedia API Demo

## Purpose

The Wikipedia API demo application receives a request with a search term and then responds back with the results from Wikipedia.
This application is used for demo purposes to be deployed to container orchestrators.

## Build and Run

```bash
docker build -t wiki-demo:latest .

docker run -p 8080:8080 -d wiki-demo:latest
```

## Interact with service

Open `http://localhost:8080/docs` in your browser to view docs.

Search Wikipedia for the search term "pizza":

```bash
curl -X 'POST' \
  'http://localhost:8080/summary' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "term": "pizza"
}'
```

## Unit testing

Unit tests are stored in the `test` directory.
To test the code, run the following:

```bash
pytest test/*.py
```
