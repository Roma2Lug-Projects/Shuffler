Shuffler
========

Creating random questionnaires for students

Requirements
------------

Linux, Python 2.7 and optionally a bottle of Jack Daniels.

HowTo
-----

The program will generate a Latex document starting from a
text file with questions and a list of students.

NOTE: THE LIST OF STUDENTS ACTUALLY NEED TO BE IN FILE STUDENTS.TXT

To generate the output file:

    $ python shuffle.py < question file > < tex file >

The format of question file is the following:

Q: Question1?  
Answer1  
Answer2  
Answer3  

Q: Question2?  
Answer1  
Answer2  
Answer3  

There are not limits to question or answer number.

However by default (actually hardcoded) each questionnarie
page contains max 10 questions randomly choosen.

The output Latex file need to be compiled.
