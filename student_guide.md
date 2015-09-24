---
layout: default
section: Students
description: A general guide to getting started with GitHub in the CS051 lab environment.
title: Lab Guide
starter-code: fa2015
permalink: /studentguide/
---

## Why Git and GitHub?

The goal of implementing Git and GitHub in the CS051 lab workflow is to
optimize the distribution-submission-feedback cycle for assignments while
exposing students to industry standard tools. It will make it easier for
course assistants and professors to provide feedback to students by creating
a simpler, more transparent workflow.

Git is used extensively throughout the open source and professional
development communites, so learning about these invaluable tools will add to
the set of skills that make you a more effective programmer. ***However,
CS051's focus is on Object-Oriented Programming (OOP) and design--not on Git;
therefore, we will not be covering advanced Git topics nor will we require
you to know them.***

We appreciate your interest and willingness to help test this new workflow!
At any point during the semester, **please ask questions as they arise**
about Git and GitHub. If the Git-related instructions make no sense, please
let us know so we can clarify them for the future!

[We would love to hear about your personal feedback and suggestions!](#feedback)

## Tools You Will Be Using

In order to make everything work together, we will be using several different
tools and software throughout the semester. Here is a brief intro to
each of the major tools you will be encountering:

### Eclipse IDE

Eclipse is an open-source **integrated development environment** (IDE) that we
will be using in CS051 to work on the Java assignments. (It's where you'll
spend the majority of your time developing your lab assignments.) An IDE is
software that bundles together all the various tools that are needed to write
code and run that code. It includes everything from source code editors to
debugging tools to compilers to console emulators.

### Git

Git is a distributed **version control system** (VCS) that has become the
industry-standard for development in open-soure and professional communities
thanks to the popularization and adoption of the online repository hosting
service [GitHub](#github).

Git aids in the development of software and projects by allowing the developer
(or team of developers) to take snapshots of their work as they progress. This
allows you to develop your projects incrementally and introduce new changes
that are easily revertable should there be a need.

In a git repository (or *repo* for short), there is a record of all the changes
which are captured in *commits* as well as any *branches* that are created.
Branches are a key feature in git. They allow you to start with some code at the
base then branch off and develop a feature. When you are done with that feature
a branch can be merged back into the main branch--the master branch. This can
be especially helpful when multiple people are working on the same project
developing different components or if a single developer wants to try
refactoring or adding code without risking the functional version of their
code. (We'll be talking a lot more about Git later in this guide and throughout
the semester!)

### GitHub

[GitHub](https://github.com) is an online Git repository hosting service. In
your Git repository that you *clone* to your computer, you will configure
*remotes* that point to the address of the GitHub hosted repository so that your
repository can pull in updates from the online repos or push updates to them.

It's important to note that you will have a *local* repository that is
stored on your computer and another that is hosted online through GitHub.
While you will tell the repositories to interact, they don't automatically
stay synced and can vary from eachother. There will be one online repository
that all students will pull in starter code from and another where you will
be pushing and pulling your own work. (More on this later!)

In addition to supporting many features of Git, GitHub has added extra online
features like issue tracking, inline code commenting, and Pull Requests (PRs)
that we will be using throughout the semester.

### EGit

EGit is an implementation of Git in the Eclipse IDE; it supports the way the
IDE sets up projects and stores the files on your computer. This plug-in also
includes a graphical user interface (GUI) to complete common Git commands.

## Getting Setup

**You should only need to complete the steps in this section once for the lab
computers and once for your personal computer.** They are instructions
specifically for Mac OSX, so if you're running any other operating system,
please contact us, and we will gladly help you get setup.

***Please read all the instructions in any given section below before clicking
the links in them!***

### Signing Up for GitHub

> **NOTE:** If you already have a GitHub account, do **not** sign up for a new
> account.

1. Go to [GitHub's Signup page](https://github.com/join).
2. Fill in the information on the first step using your Claremont issued email
   address. (*You can always add a personal email address later if you would
   like.*) Click next once you have completed the step.
3. On GitHub's Step 2, select the **$0** plan and continue to the final step.
4. Once you have completed the GitHub registration, tell us about your account
   username so we can add you to your own private repository.

### Setup Your Development Environment

> This guide assumes you already have Eclipse with EGit installed.
> If you need to install it, follow the [installation guide](/installguides).

> If you are on the lab machines, skip steps 2, 3, and 4 here.

1. Launch Eclipse by double clicking the icon.
2. In the dialog box that appears, leave the default value and check the box
   in the lower left corner to have this set as the default. Then click OK.
3. In the upper right corner of the new Eclipse window, click ***Workbench***.
4. On the toolbar go to ***Window > Perspective > Open Perspective > Java***.
5. Now, add the EGit plug-in to the workbench by clicking ***Window > Show
   View > Other... > Git > Git Repositories***.
6. Add the Git menu to your toolbar by clicking ***Window > Customize Perspective...
   > Command Groups Availability (tab)***. Check **Git** and **Git Navigation Actions**.
   Click ok to finish

At this point, Eclipse should look like [this](/images/screenshots/repo_view.png).

### Configuring Git and Cloning the Starter Code Repository into Eclipse

1. Clone the repository.
   1. Click on **File** *>* **Import** *>* **Git** *>* **Projects from Git**
      *>* **Next** *>*
   2. Click on **Clone URI** and **Next >**.
   3. In the **Source Git Repository** dialog box that appears, copy and paste
      the following into the *URI* box:
      `https://github.com/PomonaCS051/fa2015.git`
   4. Type in your GitHub username where it says "User" and your GitHub
      password where it says "Password". Check the box next to "Store in Secure
      Store" and click **Next >**.
   5. Ensure the `master` branch is selected. Then click **Next >**.
   6. In the next step, leave the default values and click **Next >**.
   7. Change the remote name to `starter-code`.
      Check *Import existing Eclipse Projects*. Then click **Next >**.
   8. Ensure the box next to HelloWorld (and any other labs) are checked.
      Then click **Finish**
2. Add a remote to point to your personal repository.
   1. In the Git Repositories view, `ctrl`-click on your project and select
      **Create Remote...**.
   2. For remote name, type `submission` and click **Next >**.
   3. Next to the URI box, click **Change...**.
   4. Type in your personal URI of the repository we have added you to.
      It should look something like
      `https://github.com/PomonaCS051/cecil-sagehen_fa2015.git` (except cecil
      and sagehen will be replaced with your name).
   5. Under authentication, put your GitHub credentials.
   6. Then click **Finish**.
   7. Finally, click **Save and Push**.

   > If you get an error message, it may have been that you mistyped the URI or
   > your username/password combination was wrong. Be sure to use your GitHub
   > credentials and **not** the CS lab credentials.

Once it finishes, you should see the `HelloWorld` folder in Eclipse's Package Explorer.

## Repeated Tasks Throughout the Semester

### Getting New Assignments

Professors will be pushing new assignments to your `starter-code` remote.
In order to get the starter code and outlines that are in this repository, you
will have to `pull` from that remote to your local repository on the `master`
branch. To do that, complete the following steps:

1. In the git repositories view, `ctrl`-click (or right click) on the `fa2015`
   repository. Use the **Switch To** option and select master. The professors will
   always push the start code to the master branch, so if you are on another branch
   there will not be changes to pull in with the configuration of the repository.
2. `ctrl`-click on the repository name again. This time it should read `fa2015 [master]`.
   Then select **Pull** and all the latest changes will be fetched and merged into
   your repository for you to begin working on. If the projects don't immediately
   appear in the package explorer, `ctrl`-click on the repository name and follow
   the default prompts under the **Import Projects...** menu.

   > Note: Access the import wizard through the git repositories view. The import
   > wizard that is used normally, will not handle the git data appropriately.

3. If this does not work, you will need to **Fetch** and **Merge**. To do this,
   checkout the master branch, click on the fetch icon. Once that task completes,
   and then click on the Merge icon. A Dialog will pop up. Click the small arrow
   next to Remote references on the dialog that pops up and click on
   `starter-code/master`.  Click through the remainder of the dialog, accepting
   defaults.

   > Note: This *fetch and merge* strategy is in fact what git is doing under the
   > hood when it performs a `pull`.

### Working on Assignments

After you completed the [above step](#getting-new-assignments) and you see the
code in Eclipse's Package Explorer, you'll want to follow the below workflow:

#### 1. Branch

For this course, we will consider each new lab a feature, so the first time you
go to work on a particular lab, you will want to create a new branch:

1. `ctrl`-click on the `fa2015` repository in the Git Repositories view.
2. Click **Switch To** > **New Branch...** and name the branch `labXX` where
   `XX` is a two digit lab number (`{01, 02, 03,..., 10, 11}`).
3. Now, in your Git Repositories view, your repository will read something like
   `fa2015 [lab00] - /path/to/directory` with the bracketed information indicating

This will create a new branch and `checkout` the branch.

> **If you are returning to work on an assignment that you have already
> started,** you must `checkout` its branch by using switching to it. When you
> checkout a branch or commit, git changes the files in your working directory
> to match the specified snapshot. This means if you create branch `lab00` work on
> it, then create a branch for `lab01` and work on a new assignment in it, then
> checkout the older branch, `lab00`, it may appear as if your Lab 1 files disappeared.
> Your code is not gone, git simply moved it out of your working directory since it
> wasn't there during Lab 0. If you checkout Lab 1 again, git will put the code back.

#### 2. Create and Submit a Design

1. Open the files you want to change in Eclipse through it's standard Package
   Explorer and make your changes.
2. Commit your work through the EGit GUI. (See below for detailed instructions
   for commiting.)
3. Now, you'll need to `push` the changes you made locally to GitHub.

#### 3. Develop Your Code and Commit Your Work

Continue working on your code in Eclipse as you would normally. When you
complete an incremental component or if the instructions tell you to `commit`
at a certain step, follow the below instructions to do so:

1. Save your work.
2. In the Package Explorer, ensure that you are on the correct branch as indicated
   by the bracketed information next to the project name. (i.e. `Laundry-Lab [lab01]`
   indicates you are on the `lab01` branch).
3. `ctrl`-click on the lab's folder.
4. In the menu that appears (towards the bottom), click **Team...**, then click
   **Commit...**.
4. In the dialog box that appears add a commit message.

   > Commit messages should be short and to the point. Something like "fixed
   > OnMouseDrag() method" or "implemented color changing methods" or "completed
   > lab47 design".

5. On the bottom of the window, you will see a list of the modified files
   present in your workspace. If you would like a changes of a file to be
   captured in the commit, use the checkbox to select the appropriate files.
   In Git, this is called staging files for a commit.
6. Click **Commit and Push**. If it's the first time you are pushing a branch,
   a dialog box will appear. Simply select the `submission` remote under the
   **Configured remote repository**. This is how Git knows where to push your code
   to.
7. Repeat this sections steps to incrementally and strategically capture the
   progress of your work.

> If you aren't connected to the internet, use **Commit** instead of **Commit
> and Push**. Once you have an internet connection, you can push all the local
> commits at once by `ctrl`-clicking on the project and selcting push.

#### 4. Initiate a Pull Request for Grading

1. Go to [GitHub](https://github.com).
2. Navigate to your private repository.
3. On the left hand side, click the Pull Requests tab.
4. Click the green button in the top-right labeled ***New pull request***.
5. Ensure base is set to master and compare is set to labXX.
6. Click ***Create new pull request*** to finish.

***If you did any extra credit, please tell the TA by explaining the extra cedit
you completed in the comment of the Pull Request.***

If it is before the lab deadline and you want to edit your code, simply
work on it in Eclipse and use `git submit labXX`. The new commits will
automatically appear in the Pull Request as long as you are committing
to the same branch (in this case that branch is labXX).
***Commits submitted after the deadline will not be graded!***

## Reviewing TA and Professor Feedback

Go to GitHub, and navigate to your private repository to view the comments
which will be found in the Pull Requests tab or Issues tab. If you want to be
notified of changes to the repositories as well as discussions, *watch* the
repository using the  button in the upper left hand corner when you are on the
repo page.

## Feedback

If you have questions, you can email us or post an issue on GitHub through
the Issues tab. If it is a question about a comment from another TA or
professor, respond directly to the comment by making another comment.
If it is a general question, raise an issue in your repository or the starter
code repository depending on the nature of the question or concern.
