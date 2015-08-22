---
layout: default
section: Course Assistants
description: A general guide to grading with GitHub in the CS051 lab environment.
title: TA Guide
starter-code: fa2015
permalink: /taguide/
---

> Note: These instructions are optimized for OSX. If you would like help setting
> up a grading environment on a Windows or Linux machine, contact
> [Eric Campbell](mailto:eric.campbell@pomona.edu).

> Note: If anything in these instructions is unclear or inaccurate, please
> [post an issue](https://github.com/pomonaCS051/pomonaCS051.github.io/issues?q=is%3Aopen+is%3Aissue), [submit a PR](https://github.com/pomonaCS051/pomonaCS051.github.io/pulls), or contact
> [us](mailto:eric.campbell@pomona.edu;ross.wollman@pomona.edu)

## Configuring your GitHub Account

First, visit [GitHub](http://www.github.com/), and create an account if you do
not have one already. You now have two options for enabling git access to your
account, `ssh` and `https`. Please do not enable two-factor authentication unless
you intend on using `ssh` to access your account.

### Using `https` authentication
This method will ask for your GitHub username and password each time you access
a remote repository (if you are on a Mac, you should be able to add these
credentials to your keychain).

> This method requires no setup.  When you clone the repositories, simply copy the
> HTTPS clone link in the right side-bar.

### Using `ssh` (recommended)
This method will require you to set up RSA keys on your computer and on GitHub
to enable unqueried access to your repositories. If you already have ssh keys,
skip step 1. If you have set up GitHub ssh access for your current machine, you
may skip all the steps below.
1. Open your bash terminal and in your home directory type `ssh-keygen`
    followed by the return key (it is recommended to accept the default settings).
2. Login to GitHub, navigate [here](https://www.github.com/settings/ssh) and click on
    **Add SSH key**
3. Provide a name in the *title* field to identify your device and copy the
    entire contents of your `$HOME/.ssh/rsa_pub` file into the *Key* box
4. Push, pull, and clone freely.

## Setting up your grading environment

### Configuring Eclipse
#### Install the Latest Distribution (recommended)
Visit [this link](http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/marsr)
to view and download the appropriate distro of Eclipse Mars.

#### Install Plugins to Existing Eclipse installation
Follow the instructions to install the [EGit plugin](http://www.eclipse.org/egit/),
and use your favorite bash terminal instead of Eclipse TM for the following instructions.

#### Selecting a workspace
When you open Eclipse, you will be asked to specify a workspace. Please ensure
that your workspace is in a different directory from the one housing your git
repositories. Not following this instruction will result in unpredictable
behavior.

#### Using the EGit GUI
Eclipse allows you to customize different sets of toolbars for different
development modes. They call these different sets of toolbars "Perpectives". If
you would like to include the EGit plugin effectively, you will need to customize
you current plugin. Navigate to **Window** *>* **Perspective** *>* **Customize
Perspective..**. A dialog box entiled "Customize Perspective - Java" will appear.
For each tab in the dialog box, click the box next to each instance of `Git` or
`Git Navigation Actions`.

### Cloning the repositories

> The following bash commands can be run in Eclipse TM or your favorite bash
> terminal.

In order to set up the repositories of the students you will be grading, you will
need to clone each students submission repo - each url should conform to the following
pattern:

{% highlight bash %}
https://www.github.com/pomona-cs051/cecil-sagehen_fa2015
https://www.github.com/pomona-cs051/fname-lname_fa2015
https://www.github.com/pomona-cs051/roonil-wazlib_fa2015
{% endhighlight %}

To clone each repository, open the Eclipse TM plugin (or your preferred bash
shell) and type

{% highlight bash %}
cd /path/to/grading/directory
{% endhighlight %}

This directory houses your git repositories and must be different from your
workspace.

For each student's lab you wish to grade, type

{% highlight bash %}
git clone https://www.github.com/pomona-cs051/cecil-sagehen_fa2015
{% endhighlight %}

This will create a new directory called `cecil-sagehen_fa2015` and will create a
local copy of the remote repository (the default name of this remote is `origin`).

Since this can be a rather tedious process, [this script](/clone-all.py) will do
it for you, otherwise you can use the rubygem `teachers_pet` to perform the same
functionality.

Ideally cloning only occurs once per semester for each student's code. As 
part of the grading workflow, TAs will see the repos in the EGit window. 
After they have pulled in the new branches and commits from students, they will 
need to right click and import in the EGit window on the student repo to switch 
to grading that student's code.

> Note: For simplicity, we recommend grading the same lab section throughout the
> semester, since this process will need to be repeated for each additional lab
> section you will grade.
>
> Another option is to clone all of the student repositories at the beginning of
> the semester.

### Importing your projects into Eclipse
Once you have configured Eclipse to use EGit and TM, and cloned the repositories
you wish to grade, you will need to make Eclipse aware of your repositories so
you can import them into your workspace to test functionality.
1. Visit **Import** *>* **Git** *>* **Projects from Git**
  + If you are given the option to select "Existing local repository", do so
2. Since you have already cloned the repositories, click **Add...**
3. In the `Directory` box, type the absolute path to your grading directory and
    hit **Search**. Select each grading repository and hit **OK** or **Finish**.
4. In the Git Repositories Window `ctrl+click` on the remote respository you
    wish to import and hit import. Follow the guide to import the project to your
    workspace
    > Note: you will need to import each repository into the workspace to test it.

### Managing your repositories
Each time you wish to grade a lab, you will need to fetch the latest copy of the
remote branches of each repository. It is simple to `cd` into each repository and
run `git fetch`, `git pull --all`, or your preferred update command. However this
is tedious, especially if you have a lab of 20-30 students. The solution to this
is [MyRepos](https://myrepos.branchable.com/), or `mr` for short. This command-line
tool reduces this tedium to a single line, `mr update`.

##### Getting started with `mr`
To install `mr`, visit [this link](https://myrepos.branchable.com/) and click on 
**Download**. Otherwise if you have `homebrew` installed, you can run `brew install mr`
in your home directory. Once it has been installed, `cd` into each repository and 
type `mr register`. This will add the repository to `mr`'s repo registry. Then, in 
any parent directory, you can call `mr update` (or `mr up` for short) to update each
repository.

##### What does `mr update` do?
The default git command that is run by `mr update` is `git pull --all`. Which
fetches all remotes and merges `-ff-only` with local branches set up to track
remotes. It does *not* create a local copy of each remote branch.
To modify the git commands run by `mr update`, you can modify the `update` field
of the `$HOME/.mrconfig` file -- this can be specific to a repository or global.
You can also define additional `mr` commands in this file.

## How to Grade for CS051 + Git
To grade a student's assignment, follow the above instructions to test the code's
functionality. Then, navigate to their submission repository on GitHub. Open the
**Pull Requests** tab and click on the PR for the current Lab. Comment your grade
for their functionality. The **Files Changed** tab will allow you to leave in-line
comments on their code. Be sure that you leave your final grade in a comment on
the **Conversations** Tab. Once you have finished grading, click **Merge** and
record their grade in the Google Doc. *Do not delete the branch.*

If a student has questions or concerns about their grade, they will be encouraged
to leave comments and questions about your comments. If you are unsure about how
to grade someone's code, you can always tag another TA or Professor in an inline
comment.

> Note: It is currently undecided if/how Git will be incorporated into the
> students' grades. If you have suggestions, please [join the discussion](https://github.com/pomonaCS051/pomonaCS051.github.io/issues?q=is%3Aopen+is%3Aissue).
