import os.path
import sys
import csv

def getCommentFormat(path, fileName):
    '''
    (str, str) -> list of str

    Given a file path containing all file extensions which can be scanned and their associated comment types along with the basename of the file we are scanning.

    Return a list of the different comment formats if the file extension is supported.
    '''
    
    fileExtension = fileName.split(".")[-1]
    
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            if line[0] == fileExtension:
                return line[1:]
    
    sys.exit("File format not supported")
        
    
def fileIsValid(path):
    '''
    (str) -> str

    Given a file path 
    
    Return basename if the file path provided is a valid file.
    
    A file is considered valid if it can be found, does not begin with "." and has an extension.
    '''
    
    if not os.path.isfile(path):
        sys.exit("Invalid file path")

    fileName = os.path.basename(path)
    if fileName.startswith('.'):
        sys.exit("File begins with '.' ")

    if "." not in fileName:
        sys.exit("File does not contain an extension")

    return fileName


def getFileContent(path):
    '''
    (str) -> list of str

    Given a file path 
    
    Return each line in the file as the elements in a list of strings
    '''
    
    f = open(path, 'r')
    fileContent = f.read().splitlines()
    f.close()
    return fileContent

def isComment(commentIndex, line):
    '''
    (int, str[]) -> bool
    
    Given a line containing a comment and the index of the comment symbol.

    Return if it is a valid comment or if it is just a comment symbol within a string.
    '''
    strings = {"'", '''"'''}
    leftCheck = True
    rightCheck = True

    leftPointer = commentIndex
    rightPointer = commentIndex
    while rightPointer < len(line) and leftPointer >= 0:
        if line[leftPointer] in strings:
            leftPointer = not leftPointer
        if line[rightPointer] in strings:
            rightPointer = not rightPointer
        rightPointer += 1
        leftPointer -= 1
    return leftCheck and rightCheck

def scanComments(fileContent, singleComment, multiCommentStart, multiCommentEnd):
    '''
    (str[], str str, str) -> int, int, int, int, int

    Given each line in the file as elements in a list of strings along with the format of single and multi line comments
    
    Return number of single line comments, number of lines in a block comment, number of block comments, number of todos, and overall total number of comments
    '''
        
    totalSingleComments = 0
    totalBlockCommentLines = 0
    totalBlockComments = 0 
    totalTodos = 0

    inBlockComment = False
    tempCount = 0

    for line in fileContent:
        line = line.strip()
        #check multi line comments
        if multiCommentStart and multiCommentEnd: 
            if multiCommentStart in line and multiCommentEnd in line and isComment(line.find(multiCommentStart),line) and isComment(line.find(multiCommentEnd),line): #block comments that are only one line are treated as single line comments
                totalSingleComments += 1
                
            elif multiCommentStart in line and not inBlockComment and isComment(line.find(multiCommentStart),line): #start of comment block
                inBlockComment = True
                totalBlockCommentLines += 1
                
            elif multiCommentEnd in line and inBlockComment and isComment(line.find(multiCommentEnd),line): #end of comment block
                inBlockComment = False
                totalBlockCommentLines += 1
                totalBlockComments += 1
                
            elif inBlockComment:
                totalBlockCommentLines += 1

        #check for single line comments
        if singleComment and not inBlockComment:
            if singleComment in line[1:] and isComment(line.find(singleComment),line): 
                totalSingleComments += 1 

            if line.startswith(singleComment): 
                tempCount += 1

            elif tempCount == 1:
                totalSingleComments += 1
                tempCount = 0

            elif tempCount > 0:
                totalBlockCommentLines += tempCount
                totalBlockComments += 1
                tempCount = 0

        #check for ToDos
        if "TODO" in line:
            totalTodos += 1

    totalComments = totalSingleComments + totalBlockCommentLines
    
    return totalSingleComments, totalBlockCommentLines, totalBlockComments, totalTodos, totalComments

def countComments(file):

    #Read in provided file
    fileName = fileIsValid(file)

    #Import comment format
    singleComment, multiCommentStart, multiCommentEnd = getCommentFormat("extensionsAndCommentFormats.csv", fileName)

    #Get all the content in the file
    content = getFileContent(file)
    totalLines = len(content)
    
    totalSingleComments, totalBlockCommentLines, totalBlockComments, totalTodos, totalComments = scanComments(content,singleComment, multiCommentStart, multiCommentEnd)
    print("Total number of lines: {}".format(totalLines))
    print("Total number of comment lines: {}".format(totalComments))
    print("Total number of single line comments: {}".format(totalSingleComments))
    print("Total number of comment lines within block comments: {}".format(totalBlockCommentLines))
    print("Total number of block line comments: {}".format(totalBlockComments))
    print("Total number of TODO’s: {}".format(totalTodos))
    return [totalLines, totalSingleComments, totalBlockCommentLines, totalBlockComments, totalTodos, totalComments]
    

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        sys.exit("Invalid number of arguments")

    countComments(sys.argv[1])


    

        
