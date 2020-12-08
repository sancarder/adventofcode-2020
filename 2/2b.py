
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
    
    correctPasswords = 0
    
    #a list of numbers
    for line in data:
        pos1true = False
        pos2true = False

        rule, passw = line.split(':')
        password = passw.strip()
        positions, letter = rule.split()
        tempPos = positions.split('-')
        pos1 = int(tempPos[0])
        pos2 = int(tempPos[1])
        
        if (password[pos1-1] == letter):
            pos1true = True
        if (password[pos2-1] == letter):
            pos2true = True

        if (pos1true != pos2true):
            correctPasswords +=1 

    return correctPasswords

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
