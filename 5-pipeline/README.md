# Module 3 - CI pipeline

**Goal**: implement all the tests in a CI pipeline

## Steps

1. Add this project to your Semaphore account
2. On the pipeline use the container image: `registry.semaphoreci.com/python:3.12.1`
2. Create a pipeline with 4 blocks:
   - Install dependencies
   - Unit tests
   - Integration tests
   - End-to-end tests
3. Ensure the pipeline runs without errors

## Tips

- Check pipeline.png in this folder to see an example.
- If you have trouble running `app.py` in CI try using `nohup python app.py &`
- If you have time you may implement optimization techniques discussed on Module 1
