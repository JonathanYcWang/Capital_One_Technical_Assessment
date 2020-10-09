# Welcome
Hey there!
 
Below, you can find an all inclusive guide to my Comment Counter where I outline how to run the program, the unit testing, an overview of how it works and any assumptions made.
 
I try to make sure that documentation is as clear and concise as possible for anyone to understand but if there are any questions please feel free to reach out at jonw.wang@mail.utoronto.ca.

# Overview  
Comment Counter is a program which checks in a single file and scans it for the following values regardless of the type of file. 
- Total Lines
- Total Single Comments
- Total Block Comment Lines
- Total Block Comments
- Total Todos
- Total  Comments

However files that do not contain an extension or are hidden (aka start with a ‘.’) will be ignored.

## Progam Flow 
1. Validate the inputed argument, path for file to be scanned, passes all the criteria depicted from unit test 2 to 5 above. If any of the conditions fail, the program terminates with the appropriate error message.

2. Identify the input file extension type.

3. Read the values of extensionsAndCommentFormats.csv row by row until the desired file extension and it's associated comment formats is found. 

4. Read in all the file content into an array where each element is a line in the file.

5. Begin scanning for comments while keeping a count for the tracked values. At every line, it is possible to find one of the following possibilities:
     
    - Contains both a multiline start and end comment. 
    - Contains a multiline start comment indicating the proceeding lines until a multiline end comment is discovered will be in block comments.
    - Is currently within a block comment.
    - Contains multiline end comment.
    - Conatinas single comment.

6. Additionally at each line regardless of comment type, check for ToDos.

7. Once every line is scanned, print and return the totals.


## Format of `extensionsAndCommentFormats.csv`
The CSV file contains the extension for different file types and the commenting formats associated. Each row is designated for a file type and strucutured in the following way:

Position |  Value | Constraint |
---- | --- | ----------- |
1 | File Extension | Required |
2 | Single Comment | Optional |
3 |  Start of Multiline Comment | Required if 4 is present |
4 | End of Multiline Comment | Required if 3 is present |

**E.g.**

 `java,//,/*,*/`

`css,,/*,*/`


# How To Run
The program is written in **Python 3** so make sure the version is properly installed in your machine's environment.
If not, you can refer to this link for further information to get you set up https://docs.python.org/3/using/index.html
 
To run the program from the terminal or command prompt, make sure to be **within this file directory** and execute the following command:
 
>python3 main.py test_files/[file name to scan]
 
The parts of the command are:
-   `python3` ->  the python compiler
-   `main.py`-> name of the main python file that will be executed
-   `test_files/javaExample.java` -> path to the file that will be scanned

 
## Additional File Types
When running the program for a file type which is not currently supported, all you have to do is add an extra row with the comment formats into the CSV in the format above.

# Testing
## Provided Unit Testing
Along with the examples provided by the assessment PDF, I have also included addition file types to demonstrate my program's ability to adapt to various languages.
 
To run the unit test, execute the following command within the current directory:
 
>python3 test.py
 
This will run the following 5 test cases:
 
**Test 1.** Check all the values are accurate across the 6 different file types.
 
File Types: *Java, Python, Javascript, HTML, CSS, HTML, SQL*
 
**Test 2.** Given that the path provided is invalid and a file to be scanned could not be found, then system exits with the following message: *"Invalid file path"*
 
**Test 3.**  Given that a file is hidden, then the system exits with the following message: *"File begins with ."*
 
**Test 4.** Given if a file has no extension, then the system exits with the following message: *"File does not contain an extension"*
 
**Test 5.** Given a file's extension is not found in extensions_and_comment_formats.csv, then the system exits with the following message: *"File format not supported"*
 
 
# Assumptions
- While in the Python example the single line comment, #, is considered a block comment if they are presented consecutively. However I am treating those as single comment still given Python has a block comment syntax of ''' which the program will be treating as multiline comment.
 
- Files will not contain nested comments within block comments, otherwise the nested comment will only be counted as an inline comment rather than a seperate single or block comment.
 
- The file already compiles without any syntactical error such as an unclosed starting multiline comment or a multiline end comment before a starting one.
- Even if a multiline comment is used, if that multiline comment also ends on the same line, it will be considered a single line comment as the comment only exists for one line.
 
- Block comments can start at the end of a line of code.
 
- Programming languages that this program will be checking only those that have a structure of at most a single line comments, multiline comments or both. It will not account for languages that use more than 3 types of symbols to write comments.



# Thank you
Lastly thank you for taking the time to review my application! Hopefully my documentation here helped save you some time in understanding my approach when tackling this technical assessment and gave insight on my thought process when working through it.