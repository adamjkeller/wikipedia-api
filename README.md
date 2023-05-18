# Wikipedia Search Service

This is an API service that fetches summary information from Wikipedia based on a user-provided search term. 
It's built with Python and FastAPI.
This is the application that I like to use for demonstration purposes.

## Features

- Fetches summary information from Wikipedia based on the search term
- (Not implemented) Posts the fetched summary results to a summary result microservice
- Provides a health check route (`/health`) for monitoring service availability

## Requirements

- Python 3.6 or above
- `requests`, `fastapi`, and `pydantic` Python packages
- (Not implemented) A running instance of the Summary Result Microservice

## Setup

To run the service locally, follow the steps below:

1. Clone the repository:

```
git clone <repository-url>
```

2. Navigate into the cloned repository:

```
cd <repository-folder>
```

3. Install the required Python packages:

```
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

4. Run the service:

```
python main.py
```

The service will be available at `http://localhost:8080`. You can view the API documentation by navigating to `http://localhost:8080/docs` in your browser.

## API Routes

- `/health`: Returns the health status of the API
- `/summary`: Accepts a POST request with a search term and returns a summary result from Wikipedia

## Future Enhancements

- The implementation for populating a DynamoDB table with the latest queries and timestamps. This will allow functionality like sorting by top 10 queries, etc.
- The addition of a `/random` endpoint, which will pick a random topic and return summary information about it.

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

## Contribution

Contributions are welcome. Please fork this repository and create a pull request for any enhancements or features you would like to add.

## Contact

For any issues, please file an issue in the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
