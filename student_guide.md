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
you to know them.*** In some cases, we have wrapped complicated Git manoeuvres
with simpler aliases, so as you read the guide, be sure to check out the 
explanations to get a better sense of what is going on behind the scense. 
Also, be sure to checkout the 
[list of Git resources](#resources-and-further-reading) we have compiled.

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
includes a graphical user interface (GUI) to complete common Git commands
without having to use the command line (although we will be using a bit of
the command line this semester).

### Terminal

A terminal is a way to interact with a computer by giving it text commands. The
commands can include everything from making a directory (`mkdir myDirectory`)
to removing a file (`rm myFile`) to running a console application like `git`.

In Eclipse, you will be using a Terminal Emulator that will allow you to
execute basic system commands like navigating into a folder
(`cd path/to/folder`) or running Git commands and aliases we created for this
course all without leaving the IDE.

## Getting Setup

You should only need to complete the steps in this section once for the lab
computers and once for your personal computer. They are instructions
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

1. Launch Eclipse by double clicking the icon.
2. In the dialog box that appears, leave the default value and check the box
   in the lower left corner to have this set as the default. Then click OK.
3. In the upper right corner of the new Eclipse window, click ***Workbench***.
4. On the toolbar go to ***Window > Perspective > Open Perspective > Java***.
5. Add the Terminal to the view by clicking !["terminal"](/images/terminal.png)
   in the toolbar. Then click OK in the dialog box that appears.

    > The terminal that appears will appear in the same tab as the java
    > debugger that you will rely on throughout the semester, so be sure to
    > close the terminal when you are not using it (or switch tabs)!

6. Now, add the EGit plug-in to the workbench by clicking ***Window > Show
   View > Other... > Git > Git Repositories***.

At this point, Eclipse should look like [this](/images/env_preview.png).

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
   7. Select *Import existing Eclipse Projects*. Then click **Next >**.
   8. Ensure the box next to Lab00 is checked. Then click **Finish**
      
      > Once it finishes, you should see the `LabXX` folders in Eclipse's
      > Package Explorer.

4. In the repositories view in the EGit window, expand the repository by
   clicking the triangle next to its name. Then click **Working Directory** so
   it is highlighted in blue.
5. Hit `command-C` to copy the path of the folder.
6. Click the `Terminal` icon
   !["terminal"](/images/terminal.png) in the top menu bar.
7. Type `cd` plus a space and paste the path you copied from step 5. It should
   look something like this: `cd /Users/cecilsagehen/git/fa2105`  
   Hit return.    
   Then copy and paste the following: `python configure_git.py`   
   Hit return.  
   You will be prompted for your password. Enter the password for the **lab
   computer** and hit return.  
   Enter the remaining information as it prompts you to and hit return after
   each prompt.

## Repeated Tasks Throughout the Semester

### Getting Around with the Command Line

In order to navigate into a directory, you will use the current directory
(`cd`) command. It's most basic use looks something like this:  
{% highlight bash %}
cd path/to/folder # swap out 'path/to/folder' with the actual path!
{% endhighlight %}
When you are working with Git commands, you will want to `cd` into the
directory that is one level above the `.git` directory.

1. In the Git Repositories view in Eclipse, click the arrow next to your
   repository.
2. Then, `ctrl`-click on *Working Directory* and click *Copy Path to Clipboard*.
3. In terminal type `cd` plus a space and paste the path you copied in the above
   step. Then hit return and you will be in the proper directory.

> Hint: If you need to figure out where you are in your filesystem, you can
> type `pwd` which stands for "print working directory."

### Getting New Assignments

Professors will be pushing new assignments to your `starter-code` remote.
In order to get the starter code and outlines that are in this repository, you
will have to `pull` from that remote to your local repository on the `master`
branch. To do that, complete the following steps:  

1. Open Terminal in Eclipse.
2. [`cd` into the appropriate directory](#getting-around-with-the-command-line).
3. Execute the following command: `git starterCode`
4. Then, `ctrl`-click in the repository view and select **Import Projects...**
5. Follow the steps to import the projects and they will appear in the Package
   explorer where you will edit and write code. When you go through the import,
   you can leave the default values.

### Working on Assignments

After you completed the [above step](#getting-new-assignments) and you see the
code in Eclipse's Package Explorer, you'll want to follow the below workflow:

#### 1. Branch

For this course, we will consider each new lab a feature, so the first time you
go to work on a particular lab, you will want to create a new branch by
executing the following command: 
{% highlight bash %}
git newLab labXX # labXX should be the actual lab number. i.e. lab01 or lab47
{% endhighlight %}

This will create a new branch and `checkout` the branch.

> If you are returning to work on an assignment that you have already started,
> you can `checkout` its branch by using `git checkout labXX`. (Just remember
> to change `XX` to the appropiate number!) This will put the relevent files
> and changes back into your working directory.

#### 2. Create and Submit a Design

1. Open the files you want to change in Eclipse through it's standard Package
   Explorer and make your changes.
2. Commit your work through the EGit GUI. (TODO: Add explanation and specific
   steps).
3. Now, you'll need to `push` the changes you made locally to GitHub.

{% highlight bash %}
git submit labXX # swap out 'labXX' with the appropriate number
{% endhighlight %}

#### 3. Develop Your Code and Commit Your Work

Continue working on your code in Eclipse as you would normally. When you
complete an incremental component or if the instructions tell you to `commit`
at a certain step, follow the below instructions to do so:

1. Save your work.
2. In the Package Explorer, `ctrl`-click on the lab's folder.
3. In the menu that appears (towards the bottom), click **Team...**, then click
   **Commit...**.
4. In the dialog box that appears add a commit message.
   
   > Commit messages should be short and to the point.

5. On the bottom of the window, you will see a list of the modified files in
   present in your workspace. If you would like a changes of a file to be
   captured in the commit, use the checkbox to select the appropriate files.
   In Git, this is called staging files for a commit.
6. Click **Commit**.
7. Repeat this sections steps to incrementally and strategically capture the
   progress of your work.


#### 4. Push Your Assignment to GitHub

Until you do this step, all your work is being completed locally and is not
being synced up to GitHub. To push it to GitHub, execute the following command 
after [`cd`ing to the appropriate directory](#getting-around-with-the-command-line).:  
{% highlight bash %}
git submit labXX # swap out `labXX` with the appropriate number
{% endhighlight %}

#### 5. Initiate a Pull Request for Grading

1. Go to [GitHub](https://github.com).
2. Navigate to your private repository.
3. On the left hand side, click the Pull Requests tab.
4. Click the green button in the top-right labeled ***New pull request***.
5. Ensure base is set to master and compare is set to labXX.
6. Click ***Create new pull request*** to finish.

If you did any extra credit, please tell the TA by explaining the extra cedit
you completed in the comment of the Pull Request.

If it is before the lab deadline and you want to edit your code, simply
work on it in Eclipse and use `git submit labXX`. The new commits will
automatically appear in the Pull Request as long as you are committing
to the same branch. ***Commits submitted after the deadline will not be 
graded!***

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

## Quick Reference

### Terminal Navigation
{% highlight bash %}
cd /path/to/folder # makes current directory /path/to/folder
pwd # prints the path of the working directory
{% endhighlight %}

### Git
{% highlight bash %}
$ git status # get details of your git repo - modified files, current branch, etc.
$ git starterCode  # fetches new assignments and merges them into `master` branch
$ git newLab lab47 # creates a branch, `lab47` for you to work on
$ git submit lab47 # pushes lab47 branch to your private GitHub repo
$ git checkout a-branch-name # checks out `a-branch-name`
$ git commit -m "my commit message" # creates a new commit with a message
$ git add -A # stages all modified files for next commit
{% endhighlight %}

## Resources and Further Reading

