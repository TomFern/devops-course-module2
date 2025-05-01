# Module 3 - Monitor errors with test reports

**Goal**: Test test reports in Semaphore

## Steps

Create a virtualenv with the following code:

```shell
python -m venv venv
source venv/bin/activate
```

1. Install the dependencies using `pip install -r requirements.txt`
2. Run `pytest` and see that some tests are failing. This is ok.
3. Run `pytest -junitxml=reports.xml` to create an XML file with the reports

### Setting up test reports

During exercise 6 where we configure the pipeline you will need the following commands in the job

```shell
# enter the directory
cd 5-test-reports
# install dependencies
pip install -r requirements.txt
pytest --junitxml=reports.xml
[[ -f report.xml ]] && test-results publish report.xml
```

Next, create an "After pipeline job" with the following command:

```shell
test-results gen-pipeline-report
```
