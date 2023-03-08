# git-for-frans-schartau

Example repository for test specialist education at Frans Schartau Handelsinstitut

# Create, checkout and update branch - version 1

1. Skapa en branch, med erat namn, git branch branch_name
2. Checka ut branchen som ni skapat, git checkout branch_name
3. Lägg till ett test i test_calculator.py, namnge testet med test_add_function_eratNamn
4. `git add .`
5. Commit:a med ett meddelande, git commit -m "..."
6. `git branch --set-upstream-to origin/main`
7. Push:a till en ny branch på Github: git push origin <erat_namn>         Här skall token användas första gången

# Create, checkout and update branch - version 2 (den jag gör varje dag)

1. Skapa och checka ut branch i ett steg: `git checkout -b namnet_på_branch origin/main`
2. Lägg till ett nytt test i test_calculator.py, namnge testet med test_add_function_eratNamn_2
3. `git add .`
4. `git commit -m "..."`
5. `git push origin namnet_på_branch`

# Rebase (rewrites history)

1. `git checkout main`
2. `git pull`
3. `git checkout branch_name`
4. `git rebase main`
5. Resolve conflicts in eg PyCharm (Right+click, select Git/Resolve Conflicts, Press merge button)
6. `git rebase --continue`
7. `git add .`
8. `git commit -m "..."`
9. `git push origin branch_name -f`          -f = force, needed if we use rebase as we rewrite history

# Delete branch

On local machine:
`git branch -D [branch_name]`

On Github:
Press the garbage can on branch.

# Prune (remove) deleted branches from local repository

When a branch has been deleted on remote (eg Github), you need to prune it from local repository.

1. `git checkout main`
2. `git pull`
3. `git fetch --all`
4. `git pull --all`
5. `git fetch -p`
6. `git pull -p`