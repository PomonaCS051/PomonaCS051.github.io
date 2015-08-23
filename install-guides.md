---
layout: default
section: Everyone
description: General installation guides for personal computers.
title: Installation Guides
starter-code: fa2015
permalink: /installguides/
---

> These guides are focused on OSX. More will be added for other operating
> systems in the future. Until then, please feel free to ask us for help
> if you would like assistance or are in need of troubleshooting on a different
> operating system.

## Java JDK

1. Check which version of the Java JDK your computer has installed.
   1. Open up Terminal.
   2. Execute the following command by copying and pasting it into the Terminal
      window and hitting return: `java -version`
   3. If you see `java version 1.8.x`, you already have the Java JDK installed!
2. Download and install Java JDK 1.8 from Oracle.
   1. [Download the Java JDK 1.8 from Oracle][JavaJDK].
   2. Install the Java JDK by double clicking the `.tar` file that is
      downloaded.

## Eclipse IDE with `OBJECTDRAW` and EGit 

> This step assumes you have alread installed the Java JDK from [above](#java-jdk).

1. Go to the this page: [Eclipse IDE for Java EE Developers][eclipse].
   
   > **WARNING:** Do not click the large orange download link at the top of
   > the page--it will make these instructions useless!

2. On the right side of the page under **Download Links** select the
   appropriate operating system. (If you're on the lab computers, select Mac
   OS X.)
3. On the next page, click the orange download button that is on the **left 
   side** of the page. **(Do not use the button that is in the upper right
   corner!)**
4. Once the file downloads, open Finder in Mac and navigate to the Downloads
   directory.
5. Double click the `.tar` file that downloaded to install Eclipse.
6. Move the application to your Applications folder by dragging the
   application that installed after Step 5 in your Downloads folder.
7. Download the `OBJECTDRAW` [library][objectdraw] and move the file into
    a permanent place.
8.	In the toolbar, click ***Eclipse > Preferences > Build Path > Classpath
    Variables***
9. Click ***New...*** on the right side.
10. In *Name*, type the following (including the capitilization): `OBJECTDRAW`
11. In *Path*, browse to the file you downloaded and moved in Step 7.
12. Then click OK twice to finish!

## Git

If you're on the Pomona CS lab computers, open a Terminal window and type
`git`, and then press enter. Git will automatically install if it is not found.

Head over to the official Git website to find the proper download and
instructions for your OS: [Official Git Site](https://git-scm.com/downloads).


[JavaJDK]: http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
[eclipse]: http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/marsr
[objectdraw]: http://eventfuljava.cs.williams.edu/library/objectdrawV1.1.2.jar
