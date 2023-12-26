
class FileOutputter:

    # Constructor: takes in a file
    def __init__(self, file):
        self.file = file

    # Function: outputs created problems to a file of the chosen type
    def outputFile(self, out, correct, pref):
        f = open(self.file, "w")
        if (pref.fileType == "TSV"):
            #output reorder
            if pref.problemType == 'reorder':
                for problem in out:
                    for tuple in problem:
                        for line in tuple:
                            f.write(str(line) + "\t")
                    f.write("\n")
                f.write("CORRECT\n")
                for line in correct:
                    f.write(str(line) + "\t")
            #output fill in the blank
            elif pref.problemType == 'fill_blank':
                for problem in out:
                    for line in problem:
                        f.write(str(line) + "\t")
                    f.write("\n")
                f.write("CORRECT\n")
                for line in correct:
                    f.write(str(line) + "\t")
            #output multiple choice
            elif pref.problemType == 'multiple_choice':
                for problem in out:
                    for line in problem:
                        f.write(str(line) + "\t")
                    f.write("\n")
        else:
            print("NOT IMPLEMENTED")
        f.close()
