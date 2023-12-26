# PPALMS

The PPALMS is a python application that runs within the terminal. It is meant to create exam questions by shuffling lines of code.

## Instructions for running PPALMS:
In order to run this application, open up a terminal and navigate into the directory containing the application files. 
Once in the directory, run the following commands within the terminal:

### For reorder problems
- py Facade.py
- create
- input.py
- reorder
- 10
- TSV
- 2,3
- exit

### For fill in the blank problems
- py Facade.py
- create
- input.py
- fill_blank
- 5
- TSV
- -1

### For multiple choice problems
- py Facade.py
- create
- input.py
- multiple_choice
- TSV



The created problem file will then be viewable in problems.tsv
By running the program in this way, the following requirements have been met:
1.1, 2.1, 2.2, 2.3, 3.1, and 3.2

## Instructions for running unit tests:
In the terminal, navigate to the directory containing the application python files and run the following command: 

- py unit_test.py
