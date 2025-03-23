# Module 3 - TDD

**Goal**: experiment with the TDD development methodology.

## Steps

1. Open `test_factorial.py` and examine its contents
2. Add a few more tests in the same file
3. **(RED STAGE)** Run `python test_factorial.py` you should get an error message like this:

    ```
    F
    ======================================================================
    FAIL: test_factorial_of_0 (__main__.TestFactorial.test_factorial_of_0)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/tom/r/devops-course/module3/tdd/test_factorial.py", line 7, in test_factorial_of_0
        self.assertEqual(factorial(0), 1)
        ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
    AssertionError: None != 1

    ----------------------------------------------------------------------
    Ran 1 test in 0.001s

    FAILED (failures=1)
    ```

4. **(GREEN STAGE)** Open `factorial.py` and implement the solution until the test passed
5. **(REFACTOR STAGE)** Improve the solution on `factorial.py` to make it more general or cover edge cases
