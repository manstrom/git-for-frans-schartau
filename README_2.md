# This is a git example

This is a README for testing git on.

## Commiting

git commit - Takes staged files and directories and saves them as snapshot. Will open editor.

git commit -m "A message" - Takes staged files and directories and saves them as snapshot. 
Will NOT open editor, the "A message" will be used as commit message.

## Add files to staging area

git add [name_of_file1] [name_of_file2] - adds specific files to staging area

git add . - Short command to add all changed files and directories, works well if list of files is small.

## Branching

git branch - lists branches on local repository

git branch [new_branch] - creates a new branch named [new_branch]
example:
git branch branch-details

### Checkout a branch

git checkout [branch-name] - checkouts a branch
example:
git checkout branch-details

or

git checkout master - checkouts master branch

git checkout -b [branch-name] - checkouts AND creates a branch named [branch-name]
example:
git checkout -b delete-branch

## Delete a branch

git branch -D [branch-name] - Deletes a branch named [branch-name].

## Stash

git stash list - lists changes temporary "saved" as stashes

git stash pop - Takes latest temporary "saved" stash and puts it on current branch

git stash - Saves all uncommited changes and "saves" them temporary as stashes

Tip! Keep stash list small!!!