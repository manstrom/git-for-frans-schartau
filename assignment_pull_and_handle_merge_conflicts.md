# Assignment 3 - Add a new test to test_calculator.py

You shall add update to a test file.
Since many testers will do updates to this file, there will be conflicts.
You must resolve conflicts.
You shall do pull on the branch you are working on.
You shall push your changes to remote server (Github), in your own branch.

Name test:
def test_add_function_[yourname]():
    assert add(1,2) == 3 # Or some assert

Note: The test and the calculator does not need to 100% working, but good if it is.


## git steps

1. Secure you are on *main* branch (`git checkout main`)
2. Update your local repository (`git pull`)
3. Create a new branch AND checkout it `git checkout -b [yourname] origin/main`
4. Change a file that one colleague also changes
5. git add .
6. git commit -m "..."
7. git push origin [yourname]
8. Open pull request in Github
9. Get a colleague to merge code in same file
10. In branch [yourname] you shall do ``git pull``