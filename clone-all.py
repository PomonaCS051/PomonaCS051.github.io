import os

# IMPORTANT:
# Ensure this script is run in the desired parent directory for CS051 grading.
# alongside a file containing a text file entitled `all_students.txt`.
# Each line should be the first and last name of a student.

students = open('./all_students.txt', 'r')
studentName = students.readline()
request = 'git clone git@github.com:pomona-cs051/'

# easily modified to use HTTPS
while studentName is not None:
     spaceIdx = studentName.index(' ')
     if spaceIdx >= 1:
          first = studentName[:spaceIdx].lower()
          last = studentName[spaceIdx + 1:].lower()
          request += first + '-' + last
          os.system(request + '-fa2015')
     else:
          print('Bad Student Name ' + studentName)
          break

close(students)
