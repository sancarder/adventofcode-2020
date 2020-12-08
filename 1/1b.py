
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
    
    #a list of numbers
    for i in range(0, len(data)-2):
        for j in range(i+1, len(data)-1):
            for k in range(i+2, len(data)):
                a = int(data[i])
                b = int(data[j])
                c = int(data[k])
            
                #print(a, b)
            
                if (a + b + c == 2020):
                    return a*b*c    

    return -1

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
