import unittest
import ProblemCreator
import FileInputter
import FileOutputter
import Facade
import Preference
from unittest import mock
  
class Testing(unittest.TestCase):
  
    # Returns True or False. 
    def test_createProblems(self):        
        problemCreator = ProblemCreator.ProblemCreator("input.py")
        pref = Preference.Preference("reorder", 5, "TSV", ["2","3"], problemCreator.file)
        problemCreator.createProblems(pref)
        self.assertEqual(problemCreator.size, 5)
    
    def test_createProblemsInvalidFile(self):        
        problemCreator = ProblemCreator.ProblemCreator("output.py")
        self.assertRaises(FileNotFoundError)

    def test_checkFilePython(self):
        fileInput = FileInputter.FileInputter("input.py")
        self.assertTrue(fileInput.checkFile())
    
    def test_checkFileJava(self):
        fileInput = FileInputter.FileInputter("input.java")
        self.assertTrue(fileInput.checkFile())
    
    def test_checkFileC(self):
        fileInput = FileInputter.FileInputter("input.c")
        self.assertTrue(fileInput.checkFile())
    
    def test_checkFileCPP(self):
        fileInput = FileInputter.FileInputter("input.cpp")
        self.assertTrue(fileInput.checkFile())
    
    def test_checkFileWrongExtention(self):
        fileInput = FileInputter.FileInputter("input.ts")
        self.assertFalse(fileInput.checkFile())
    
    def test_readFile(self):
        fileInput = FileInputter.FileInputter("input.py")
        self.assertNotEqual(fileInput.readFile(), [])

    def test_readFileNotExist(self):
        fileInput = FileInputter.FileInputter("output.py")
        fileInput.readFile()
        self.assertRaises(FileNotFoundError)
    
    def test_outputFile(self):
        fileOutput = FileOutputter.FileOutputter("outputTest.tsv")
        problems = [[['return result'], ['number1 = x', 'number2 = y'], ['result = number1 + number2'], ['def addNumbers(x, y):']], 
                    [['def addNumbers(x, y):'], ['return result'], ['result = number1 + number2'], ['number1 = x', 'number2 = y']], 
                    [['def addNumbers(x, y):'], ['return result'], ['result = number1 + number2'], ['number1 = x', 'number2 = y']], 
                    [['def addNumbers(x, y):'], ['return result'], ['number1 = x', 'number2 = y'], ['result = number1 + number2']], 
                    [['result = number1 + number2'], ['return result'], ['def addNumbers(x, y):'], ['number1 = x', 'number2 = y']]]
        correct = ['def addNumbers(x, y):', 'number1 = x', 'number2 = y', 'result = number1 + number2', 'return result']
        fileOutput.outputFile(problems, correct, "TSV")
        readOutput = open("outputTest.tsv", "r")
        self.assertNotEqual(readOutput, None)
        readOutput.close()

    @mock.patch("Facade.input")
    def test_readPreferences(self, mocked_input):
        mocked_input.side_effect = ["reorder", "5", "TSV", "2, 3", "exit"]
        problemCreator = ProblemCreator.ProblemCreator("input.py")
        preferences = Facade.readPreferences(problemCreator.size, problemCreator.file) #Need to mock or smth for the input
        return Preference.Preference("reorder", 5, "TSV", ["2","3"], problemCreator.file) == preferences

    @mock.patch("Facade.readPreferences")
    @mock.patch("Facade.input")
    def test_problemCreation(self, mocked_input, mocked_pref):
        problemCreator = ProblemCreator.ProblemCreator("input.py")
        mocked_pref.return_value = Preference.Preference("reorder", 5, "TSV", ["2","3"], problemCreator.file)
        mocked_input.side_effect = ["input.py", "reorder", "5", "TSV", "2, 3", "exit"]
        Facade.problemCreation()
        readOutput = open("problems.tsv", "r")
        self.assertNotEqual(readOutput, None)
        readOutput.close()

if __name__ == '__main__':
    unittest.main()