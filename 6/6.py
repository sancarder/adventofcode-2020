import numpy as np


def testData():

    otest = open('test.txt', 'r')
    test = otest.readlines()

    oanswer = open('answer.txt', 'r')    
    answer = oanswer.readline()

    status = False
    print("Runs test data")
    result = runCode(test)

    if result == int(answer): #not always int
        status = True
 
    print("Correct answer: " + answer + "My answer: " + str(result))
    return status
    

def runCode(data):
    print("Runs code")
    
    decls = []
    decl = ''
    dlist = []
    total = 0
    
    #a list of numbers
    for line in data:

        if line != '\n':
            decl += line.strip()
        else:
            for l in decl:
                dlist.append(l)
            decls.append(dlist)
            decl = ''
            dlist = []
    decls.append(decl) 
        
    #Makes a set to eliminate duplicates and count the list
    for de in decls:
        uniques = set(de)
        answers = len(uniques)
        total += answers

    return total

#Runs testdata
testResult = testData()

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    opuzzle = open('input.txt', 'r')
    puzzle = opuzzle.readlines()
    finalResult = runCode(puzzle)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
