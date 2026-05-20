# Git


## What I've Learned

### 1. Repository Structure
A Git repository (repo) is basically a digital folder that tracks changes over time. 
* **Working Directory:** The files I can see and edit on my computer.
* **Staging Area:** A waiting room where I select which files I want to save next (`git add`).
* **Local Repo:** Where my saved snapshots (`git commit`) live on my computer.
* **Remote Repo:** A backup server on the internet (like GitHub) where I upload my code.

### 2. The Collaborative Workflow
When working with a team, we don't all edit the `main` code at the same time. We follow this flow:
1. **Pull:** Always start by getting the latest code (`git pull`).
2. **Branch:** Create a new branch for a specific task (`git switch -c new-feature`).
3. **Work:** Make changes, `git add`, and `git commit`.
4. **Push:** Upload the branch to GitHub (`git push`).
5. **Pull Request:** Ask the team to review the code before it joins the main project.

### 3. Pull Requests (PRs)
A Pull Request isn't a terminal command; it's a feature on websites like GitHub. It is a formal request saying, "Hey team, I finished my branch. Please review my code and merge it into the main project." It gives everyone a chance to talk about the code before it becomes official.

### 4. Surviving Merge Conflicts
A merge conflict happens when two people edit the exact same line of code, or one person edits a file while another deletes it. Git gets confused and pauses the merge. 

**How to fix it:**
1. Git will point out the conflicting files.
2. Open those files in a code editor.
3. Look for weird symbols like `<<<<<<<`, `=======`, and `>>>>>>>`. 
4. Delete the versions of the code I don't want (and delete the symbols).
5. Run `git add` on the fixed file, and `git commit` to finish the merge!
(And if I panic, I can always run `git merge --abort` to cancel everything).

## 5.Git Commands

### Setup & Starting Out
* `git config --global user.name "Name"` — Sets my display name.
* `git config --global user.email "email"` — Sets my email address.
* `mkdir my-git-project` — Creates a new folder.
* `cd my-git-project` — Moves into the folder.
* `git init` — Turns the folder into a Git repo.
* `git status` — Checks what Git is currently seeing (use this constantly!).

### Saving Work
* `touch README.md` — Creates a new blank file.
* `git add README.md` — Stages a specific file.
* `git add .` — Stages all changed files at once.
* `git commit -m "Message"` — Takes a snapshot of my staged files.
* `git log` — Shows the history of all my commits.
* `git log --oneline` — Shows a clean, compact commit history.

### Branching
* `git branch` — Lists all branches (the `*` shows where I am).
* `git branch [branch-name]` — Creates a new branch.
* `git switch [branch-name]` — Moves into a branch.
* `git switch -c [branch-name]` — Creates a new branch and moves to it in one step.
* `git branch -d [branch-name]` — Deletes a branch.

### Reviewing & Undoing
* `git diff` — Shows unstaged code changes.
* `git diff --staged` — Shows staged code changes.
* `git restore [file]` — Discards unsaved changes in a file.
* `git restore --staged [file]` — Un-stages a file, but keeps my typed changes.

### Merging
* `git switch main` — Returns to the main branch.
* `git merge [branch-name]` — Combines a branch into the one I am currently on.
* `git merge --abort` — Panic button! Cancels a messy merge conflict.

### Working with GitHub
* `git remote add origin [URL]` — Connects my local folder to an online repo.
* `git push -u origin main` — Uploads my code for the first time.
* `git push` — Uploads my code (use this after the first time).
* `git pull` — Downloads the latest code from the internet and merges it.
* `git clone [URL]` — Downloads an entire existing project to my computer.