
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
        rule, password = line.split(':')
        times, letter = rule.split()
        mini, maxi = times.split('-')

        c = password.strip().count(letter.strip())
        
        if (int(c) >= int(mini) and int(c) <= int(maxi)):
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
