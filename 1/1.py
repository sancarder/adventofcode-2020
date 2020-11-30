
def readData(data):
    line = input.readline().strip()
    return line.split(',') 

def testData(test, answer):

    test = readData(open('test.txt', 'r'))
    answer = readData(open('answer.txt', 'r'))

    status = False
    print("Runs test data")
    result = runCode(test)

    if result == answer:
        status = True
 
    print(status)
    return status
    

def runCode(data):
    print("Runs code")
    
    return "default"

#Runs testdata
testResult = testData()

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    puzzle = readData(open('input.txt', 'r'))
    runCode(puzzle)
else:
    print("Test data failed. Code is not correct. Try again.")
