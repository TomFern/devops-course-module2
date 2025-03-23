# Module 3 - End-to-end tests

**Goal**: implement end-to-end tests

## Steps

1. Install the dependencies using `pip install -r requirements.txt`
2. Open `app.py`, examine this Flask application
3. Open `test_e2e.py`, examine the test structure
4. Implement two tests:
  - Perform a GET request to `http://127.0.0.1:5000/` then check status code is 200 and the response body contains the string "Welcome"
  - Perform a POST request on `http://127.0.0.1:5000/add`. Send a JSON message in the request and check that status code is 200 and that the response data in the body is correct
 
