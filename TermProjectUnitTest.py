# Kim K.
# CSC 110
# 12/13/2023
# Term Project unittest
# This program tests my file processing and filtering via unittest

import unittest
import fileprocess

class testfile(unittest.TestCase):
            
    def testProcessProvidable(self):
        testfilepath = "PyUnitTest/testfile1.txt"
        assumedreturntable = {
            "A":"A",
            "C":"awesome test",
            "E":"tes test 5",
            "Q":"C",
        }
        returnfile = fileprocess.processprovidable(testfilepath)
        self.assertEqual(assumedreturntable, returnfile)
        
    def testSeparatedArray(self):
        testfilepath = "PyUnitTest/testfile1.txt"
        assumedreturntable = [
            ["awesome test","C"],
            ["AWESOME TESTTT","A"],
            ["tes test 5","E"],
            ["AAAAAAAAAAAAAA","A"],
            ["A","A"],
            ["C","Q"],
        ]
        returnfile = fileprocess.separatedarray(testfilepath)
        self.assertEqual(assumedreturntable, returnfile)



if __name__ == "__main__":
    unittest.main()