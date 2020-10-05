import unittest
import main.py

class TestCommentCounter(unittest.TestCase):
    
    def testParseJavaFile(self):
        path = "./javaExample.java"
        game = GameOfLife(init_board)
        game.next_move()
        self.assertTrue(game.board,[
                                    [0,0,0],
                                    [1,0,1],
                                    [0,1,1],
                                    [0,1,0]
                                    ])
    def testParsePythonFile(self):
        path = "./pythonExample.py"
        game = GameOfLife(init_board)
        game.next_move()
        self.assertTrue(game.board,[
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0]
                                    ])
    def testParseJSFile(self):
        path = "./javaScriptExample.js"
        game = GameOfLife(init_board)
        game.next_move()
        self.assertTrue(game.board,[
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0]
                                    ])
    def testParseSQLFile(self):
        path = "./sqlExample.sql"
        game = GameOfLife(init_board)
        game.next_move()
        self.assertTrue(game.board,[
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0]
                                    ])
    def testParseCSSFile(self):
        path = "./tests/cssExample.css"
        game = GameOfLife(init_board)
        game.next_move()
        self.assertTrue(game.board,[
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0]
                                    ])
    def testParseHTMLFile(self):
        path = "./htmlExample.html"
        game = GameOfLife(init_board)
        game.next_move()
        self.assertTrue(game.board,[
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0],
                                    [0,0,0]
                                    ])
                                    ])
unittest.main()
