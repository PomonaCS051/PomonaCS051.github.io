---
layout: default
section: General
description: A general guide to Git.
title: Git Guide
starter-code: fa2015
permalink: /gitguide/
---

## The Git Philosophy
Git is a version control system that facilitates cooperation between many users
by allowing them to create separate versions of the same directory structure
and combine finalized features into a master copy. It is the de facto
industry-standard for version control, a status which has been helped by GitHub,
a massive community for open-source contributions on everything from novels to
mobile apps, from Adobe Illustrator projects, to Eclipse projects.

One of the greatest assets about using Git for your projects is that it is almost
impossible to do anything irreversible. This is because of the way that Git
tracks changes, generally it adds changes to maintain the current state of your
file system, so if I add a line of code at one point, and then remove it at a
later date, Git will know both that I added that line *and* that I deleted it.
This means that if you royally screw up a piece of code, it is really easy to
revert it back. Especially if you regularly push your code to a remote repository.

So how does this work? In the process of your labs, you will be making changes to
your assignment, and you will want to set 'checkpoints' for yourself as you go
along. Its basically a more advanced way of saving your work.  If you've used
Google Drive, you may have noticed that they have a `Changes` tool, that allows
you to see who made what modification to the file and undo those changes. Git
does the same thing, but better.

## The Git Workflow
There are three states in which your files can reside `modified`, `staged`, and
`committed`. Once you start editing files, they have become `modified`. To propose
a file change, you `git add` them to staging index, and they are
`staged`. You can continue to add files to the staging index at your leisure.
Once you are satisfied that your collection of changes in the staging index are
sufficent, you `git commit` your changes in a batch to the repository. Ideally, this
represents a discrete, standalone block of changes, so that it is easy to undo
specific file changes. Then, when you want to publish your changes, to either
get feedback or to submit them for review, `git push` the changes to a remote
repository.

### `Add`ing
After you have made some changes on your working copy, you want to stage the
changes you have made so that you can continue to make low-risk changes. To do
this for all of the tracked files, run `git add -A` or `git add --all` from the
command line.  To stage changes for a specific file, run `git add <filename>`.

Sometimes you want to remove a file from the staging index.  To do this you have
to reset the file to its state at the current HEAD, by running
`git checkout <branchname> <filename>`.

> Protip: If you want to add all the files in directory `test_dir`, instead of
> typing `git add test_dir/file1 test_dir/file2` ... etc., you can accomplish the same
> by running `git add test_dir`.

### `Commit`ting
Once you have made a collection of changes and added them to the staging index,
you are ready to commit. To do this, run `git commit -m '<A descriptive message>'`
The descriptive message should describe the collection of changes you've made,
e.g. 'Implemented OnMouseClick() method', or 'Dropped the Ball'. Each commit is
uniquely identified by a hexadecimal hash, containing the user's name, email, a
timestamp, and other information. You can see this identifer next to each commit
by running `git log`.

Commits should be small and modular, including changes that can be easily undone
in the future. You dont want to have both the `OnMouseClick` implementation and
ball drop implementation in the same commit, because then if you want to undo the
`OnMouseClick()` implementation, you end up undoing more than you would like.

There are several ways to undo a commit.  The safest (and recommended) way is to
run `git revert <commit-hash>`, which will create a new commit that undoes exactly
the commit specified by `<commit-hash>`.

If this is insufficient, you may find yourself needing to completely undo the
latest commit. This is done using `git reset HEAD~1`. You can either do a soft
reset or a hard reset. A soft reset, specified by the `--soft` flag, will undo all
the changes in the most recent commit and add them to the the staging index. A
hard reset, specified by the `--hard` flag, will completely obliterate all of
your changes, so please be explicit about which you are intending and always
include `--soft` or `--hard`.

> Protip: running `git status` will display the status of the changed files in
> your working copy, i.e. are they staged, modified, untracked, etc.

### `Push`ing
Once you have a collection of commits you would like to publish to GitHub for
feedback or as final, submitted code, you run `git push` on your repository. This
will add the commits on your current branch to the remote-tracked branch. Best
practices are that if I have a branch named `lab09` the remote will also have a
branch `lab09` that is being tracked by the local copy. Pushing adds the local
changes to the remote one.  This takes some setting up.

Generally you will need to specify the upstream destination of the branch. To avoid
this, add the `-u` parameter to the command the first time, so you will have
`git push -u <remote-name> <branch-name>`. This sets the current branch to track
a remote branch of the same name while pushing the recent changes. Every
subsequent `git push` will push to the specified remote.

### `Pull`ing
To update the local copy of your branch with the tracked remote, use the command
`git pull`. This will only work if you have set the upstream remote.

### `Fetch`ing
The command `git fetch` updates all local references to remote branches with their
remote copies.

### `Branch`ing and `Merge`-ing
One of the novel features of Git that makes it different from other version
control software is that it allows for divergent copies to be checked out. This
allows for managing multiple versions of code simultaneously. You can then merge
branches together to combine the changes that have been made. Accepted best
practices suggest having a `master` branch that contains the best and most
functional version of the code. Then for each addition or change, create a new
branch. Once that change has been finalized, merge it back into the current branch.
Typically, if `branchB` is checked out from `branchA`, `branchB` will eventually
be merged back into `branchA`.

Some handy branching commands:

| Action                         | Description                                                |
|:------------------------------:|:----------------------------------------------------------:|
| `git checkout existing-branch` | *Checks out the branch `existing-branch`*                  |
| `git checkout -b new-branch`   | *Creates a new branch `new-branch` and checks it out*      |
| `git merge branchA`            | *merges branch existing `branchA` into the current branch* |
| `git branch -a`                | *lists all branches, local and remote*                     |


## Related links
 + [Try Git](https://try.github.io/levels/1/challenges/1) -- Git Interactive Tutorial
 + [Simple Guide to Git](http://rogerdudler.github.io/git-guide/) -- for the basic commands
 + [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics) -- for a more specific understanding of how it works.

