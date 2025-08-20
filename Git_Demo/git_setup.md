# Git Setup
For Window download Gitbash

git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

# Clone and Status
Remote -[Github]
local -[laptop/Pc]

- CLONE = Cloning a repository on our local machine
-> git clone <git link >

- STATUS = Checking the status of our repository
-> git status

-> Untracked = New files that are not tracked by Git

-> Modified = Files that have been modified but not committed

-> Staged = Files that have been added to the staging area but not committed


 # Add and Commit

 -> add = adds new file or changed files in your working directory to the Git staging area
    --> git add <file name> or git add .
--> Commit = it is the record of change
    --> git commit -m "<commit message>"

-> push = Upload local repository to a remote repository
    --> git push origin main

# Init Command
-> init = Used to create a new git repository
    --> git init
    -->git remote add origin <-link->
    -->git remote -v  (to verify remote)
    -->git branch  (to check branch)
    --> git branch -M main  (to rename branch)
    --> git push -u origin main

# Work Flow
-> Branch Command
    --> git branch  (to check branch)
    --> git branch -M main  (to rename branch)
    --> git checkout <-branch name->   (to navigate)
    --> git checkout -b <-new branch name->  (to create new branch)
    --> git branch -d <-To delete branch->

# when you add new branch and add some new feature You need to push the file
   --> git push -u origin <-branch name->

# Note
-> when You add new feature to Feature1 you will see changes to feature1 branch and in main branch there will be nothing changed

# Merging Code
# Way 1
    --> git diff <-branch name->  (to compare commits, branches, files and more)
    --> git merge <-branch name->  (to merge 2 branches)

 # Way 2
  -> Create a PR  (PR= Pull Request)

# Pull Request
 -> It lets you tell others about changes you've pushed to a branch in a repository on GitHub.

 # Pull Command
 -> Used to fetch and download content form a remote repo and immediately update the local repo to match that content.
     --> git pull origin main


# Resolving Merge Conflicts
-> An event that takes place when Git is unable to automatically resolve differences in code between two commits.


# Undoing Changes
-> Case 1: Staged changes (Added but not commited)
   -> git reset <-file name->
   -> git reset
-> Case 2: Commited Changes (for one commit)
git reset HEAD~1

-> Case 3: Commited Changes (for many commits)
    -> git reset <- commit hash->
    -> git reset --hard <- commit hash->    

# Fork
 -> A fork is a new repository that shares code and visibility settings with the original "upstream" repository.
  -> Fork is rough copy