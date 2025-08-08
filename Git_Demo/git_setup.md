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