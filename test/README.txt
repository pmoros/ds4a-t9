This folder contains unitary test files, it's recommended to develop tests for each module that is created. A unitary test verifies that new functionality created works fine.

Example: We create module stats.py that contains mean(series) function. Lets think of some test cases:
	1. 1, 2, 3, 4, 5
	2. 0, 0
	3. -1, 0, -5, 5

In this folder should be a test file for stats module, e.g, "stats_test.py", extension may vary. Inside this module must be a function called "mean_test()" thatis used to test that the function works fine with that input cases.
