import FileInputter
import random
class ProblemCreator:
    file = []
    problemFile = ""

    def __init__(self, file):
        self.inputter = FileInputter.FileInputter(file)
        if self.inputter.checkFile() == False:
            print("File type not accepted")
            return
        self.file = self.inputter.readFile()
        if self.file is not None:
            self.size = len(self.file)

    def createProblems(self, pref):
        # Create problems
        problems = []
        tupledLines = pref.tupledLines.copy()
        #create a reorder problem type
        if pref.problemType == "reorder":
            for i in range(pref.numProblems):
                random.shuffle(tupledLines)
                problems.append(tupledLines.copy())

            return(problems, pref.correct)
        #create a multiple choice problem type
        elif pref.problemType == "multiple_choice":
            for i in range(pref.numProblems):
                correctLineNum = int(random.random() * 1000000000000) % len(tupledLines[0])
                correctLine = tupledLines[0][correctLineNum]
                incorrectLineNums = []
                incorrectLines = []
                #create 3 different samples of code
                for x in range(3):
                    while (True):
                        randLineNum = int(random.random() * 1000000000000) % len(tupledLines[0])
                        different = True
                        if randLineNum == correctLineNum:
                            different = False
                        for z in incorrectLineNums:
                            if randLineNum == z:
                                different = False
                                break
                        if different:
                            break
                    incorrectLineNums.append(randLineNum)
                    incorrectLines.append(tupledLines[0][randLineNum])
                #format for the output file type
                currentProblem = tupledLines[0].copy()
                currentProblem[correctLineNum] = "______________"
                currentProblemInfo = []
                currentProblemInfo.append("CORRECT OPTION " + str(correctLine))
                currentProblemInfo.append("INCORRECT OPTION 1 " + str(incorrectLines[0]))
                currentProblemInfo.append("INCORRECT OPTION 2 " + str(incorrectLines[1]))
                currentProblemInfo.append("INCORRECT OPTION 3 " + str(incorrectLines[2]))
                problems.append(currentProblem)
                problems.append(currentProblemInfo)
            return(problems, tupledLines[0])
        #create a fill in the blank problem type
        elif pref.problemType == "fill_blank":
            exclusions = pref.exclude
            availableLines = []
            #find a piece of code to remove for fill in the blank
            for i in range(len(pref.lines)):
                if i not in exclusions:
                    availableLines.append(i)
                random.shuffle(availableLines)
            #replace the removed piece of code with underscores
            for i in range(pref.numProblems):
                currentProblem = pref.lines.copy()
                currentProblem[availableLines[i]] = '______________'
                problems.append(currentProblem)
            return(problems, pref.correct)


        else:
            print("NOT IMPLEMENTED")
            return([],[])
