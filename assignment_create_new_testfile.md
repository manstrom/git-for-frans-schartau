# Assignment 2 - Create a new test file and upload to Github

You shall create a new testfile for the calculator.
It shall have one test for add.
You shall upload file to remote server (Github).

Name the file:
test_calculator_[yourname].py

Name test:
def test_add_assignment_2_[yourname]():
    assert add(1,2) == 3 # Or some assert

Note: The test and the calculator does not need to 100% working, but good if it is.

## git steps

1. Secure you are on *main* branch (`git checkout main`)
2. Update your local repository (`git pull`)
3. Create a new branch AND checkout it `git checkout -b [yourname] origin/main`
4. Add the file and test
5. `git add .`
6. `git commit -m "..."`
7. `git push origin [yourname]`