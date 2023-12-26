
class Preference:
    # Class variables
    tupledLines = []
    lines = []
    exclude = []

    # Constructor: takes in preference variables and which lines are to be tupled
    # lines to be tupled are passed in as a list of int lists

    def __init__(self, problemType, numProblems, fileType, info, lines):
        self.problemType = problemType
        self.numProblems = numProblems
        self.fileType = fileType
        #contructor for reorder and multiple choice
        if problemType == "reorder" or problemType == "multiple_choice":
            self.tupleLines(info, lines)
        #contructor for fill in the blank
        elif problemType == "fill_blank":
            for e in info:
                self.exclude.append(int(e))
            self.lines = lines
            if numProblems > (len(lines) - len(info)):
                self.numProblems = len(lines) - len(info)
            
        self.correct = lines

    # Function: Tuples the lines based off the passed in lines to be tupled
    def tupleLines(self, tuples, lines):
        usedLines = []
        current = []
        for e in tuples:
            for i in e:
                current.append(lines[int(i) - 1])
                usedLines.append(int(i) - 1)
            self.tupledLines.append(current)
            current = []
        for i in range(len(lines)):
            if i in usedLines:
                continue
            else:
                self.tupledLines.append([lines[i]])

    def __str__(self):
        # For debugging purposes
        return("Problem type: {0}\nNumber of problems: {1}\nOutput type: {2}\nLines: {3}".format(self.problemType, self.numProblems, self.fileType, self.tupledLines))
