import unittest
import sys
from main import *

class TestCommentCounter(unittest.TestCase):
    
    def testMultiFileExtension(self):
        print("Test 1: Multiple Valid File Extensions \n")
        
        fileNames = {"cssExample.css" : [23, 4, 2, 1, 0, 6],
                     "htmlExample.html" : [27, 2, 5, 1, 1, 7],
                     "javaExample.java" : [60, 6, 22, 2, 1, 28],
                     "javaScriptExample.js":  [40, 6, 17, 3, 1, 23],
                     "pythonExample.py" : [61, 23, 0, 0, 3, 23],
                     "sqlExample.sql" : [7, 2, 2, 1, 0, 4]
                     }
        
        for file in fileNames.keys():
            print("File Name: " +  file)
            totals = countComments("./test_files/" + file)
            self.assertEqual(totals,fileNames[file])
            print("\n")

    def testInvalidPath(self):
        print("Test 2: Invalid File Path \n")
        with self.assertRaises(SystemExit) as cm:
            countComments("")
        self.assertEqual(cm.exception.code, 'Invalid file path')
        
    def testFileIsHidden(self):
        print("Test 3: File starts with . \n")
        with self.assertRaises(SystemExit) as cm:
            countComments("./test_files/.hiddenFile.txt")
        self.assertEqual(cm.exception.code, "File begins with '.' ")
        
    def testNoExtensionOnFile(self):
        print("Test 4: File with no extension \n")
        with self.assertRaises(SystemExit) as cm:
            countComments("./test_files/noExtensions")
        self.assertEqual(cm.exception.code, "File does not contain an extension")
        
    
if __name__ == "__main__":
    unittest.main()


    

        
