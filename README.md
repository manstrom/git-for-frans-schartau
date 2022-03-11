# git-for-frans-schartau

Example repository for test specialist education at Frans Schartau Handelsintitut

Can this be uploaded to github?


# Assignment - version 1

1. Skapa en branch, med erat namn, git branch branch_name
2. Checka ut branchen som ni skapat, git checkout branch_name
3. Lägg till ett test i test_calculator.py, namnge testet med test_add_function_eratNamn
4. git add .
5. Commit:a med ett meddelande, git commit -m "..."
6. git branch --set-upstream-to origin/main
7. Push:a till en ny branch på Github: git push origin <erat_namn>         Här skall token användas första gången

# Assignment - version 2 (den jag gör varje dag)

1. Skapa och checka ut branch i ett steg: git checkout -b namnet_på_branch origin/main
2. Lägg till ett nytt test i test_calculator.py, namnge testet med test_add_function_eratNamn_2
3. git add .
4. git commit -m "..."
5. git push origin namnet_på_branch

# Rebase (rewrites history)

1. git checkout main
2. git pull
3. git checkout branch_name
4. git rebase main
5. Resolve conflicts in eg PyCharm (Right+click, select Git/Resolve Conflicts, Press merge button)
6. git add .
7. git commit -m "..."
8. git push origin branch_name -f          -f = force, needed if we use rebase as we rewrite history