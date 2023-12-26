import ProblemCreator
import FileOutputter
import Preference

# Function: Interacts with the user to get their preference on how to create problems
def readPreferences(size, file):
        valid = False
        while(valid == False):
            # Gets the user's choice on problem type, catches wrong problem type
            problemType = input("Enter problem type (reorder, multiple_choice, fill_blank): ")
            if(problemType == "reorder" or problemType == "multiple_choice" or problemType == "fill_blank"):
                valid = True
            else:
                print("Invalid problem type")

        valid = False
        while(valid == False):
            # Gets the user's choice on number of problem, catches a non-positive integer entry
            try:
                numProblems = int(input("Enter maximum number of problems: "))
                if numProblems > 0:
                    valid = True
                else:
                    print("Enter only positive integers")
            except:
                print("Enter only positive integers")

        valid = False
        while(valid == False):
            # Gets the user's choice on output file type, catches wrong file types
            outputType = input("Enter output file type (QTI, GIFT or TSV): ")
            if(outputType == "QTI" or outputType == "GIFT" or outputType == "TSV"):
                valid = True
            else:
                print("Invalid output type")

        valid = False
        if problemType == "reorder" or problemType == "multiple_choice":
            print("Enter lines to be tupled separated by commas, exit to finish")
            tuples = []
            while(valid == False):
                        # Gets user's choice on which lines are to be tupled
                        lines = input("Lines: ")
                        if(lines == "exit"):
                            valid = True
                            break
                        else:
                            try:
                                tupledLine = lines.split(',')
                                for e in tupledLine:
                                    e = int(e)

                                alreadyInput = False
                                tooLarge = False
                                for already in tuples:
                                    # Check whether an inputted line was already inputted
                                    if (any(x in tupledLine for x in already)):
                                        alreadyInput = True
                                for x in tupledLine:
                                    # Checks that the input file actually has the line selected
                                    if int(x) >= size:
                                        tooLarge = True
                                if(alreadyInput):
                                    print("Only enter lines that haven't been entered before")
                                elif(tooLarge):
                                    print("Invalid line (file does not have that many lines)")
                                else:
                                    tuples.append(tupledLine)

                            except:
                                # Catches invalid entry (not exit or integers followed by commas)
                                print("Only enter tupled lines separated by a comma or exit")
            return Preference.Preference(problemType, numProblems, outputType, tuples, file)
        #Interface for the Fill in the Blank Problem Type
        elif problemType == "fill_blank":
            excluded = []
            print("Enter lines to be excluded from fill in the blank problems as numbers separated by commas, -1 for all lines: ")
            valid = False
            while (not valid):
                #get users input tupled lines
                lines = input("Exclusions: ")
                try:
                    excluded = lines.split(",")
                    if (excluded[0] == '-1'):
                        excluded[0] = -1
                        valid = False
                        break
                    for e in excluded:
                        e = int(e)
                        if e < 0 or e >= size:
                            excluded.remove(e)
                    # Remove duplicates
                    excluded = [*set(excluded)]
                    valid = True
                except:
                        print("Only enter positive numbers separated by commas or -1")

            return Preference.Preference(problemType, numProblems, outputType, excluded, file)



        # Returns as a preference object with collected choices


# Function: creates problems
def problemCreation():
    outputter = FileOutputter.FileOutputter('problems.tsv')
    # Asks for an input file
    file = input("Enter input file name: ")
    # Tries to access file to create a problem creator
    PPALMS = ProblemCreator.ProblemCreator(file)
    # Creates preferences based on user input
    preferences = readPreferences(PPALMS.size, PPALMS.file)
    # Create problems based of preferences
    problems, correct = PPALMS.createProblems(preferences)
    # Outputs created problems
    outputter.outputFile(problems, correct, preferences)

if __name__ == '__main__':

    while(True):
        # Gets user's choice on whether to create problems or view statistics
        choice = input("choose whether to create problems (create) or view statistics (stats): ")
        if(choice == 'create'):
            problemCreation()
            break
        elif(choice == 'stats'):
            print("NOT IMPLEMENTED")
            break
        else:
            print("Invalid choice (create/stats)")
