
def testData(preamble):

    otest = open('test.txt', 'r')
    test = otest.readlines()

    oanswer = open('answer.txt', 'r')    
    answer = oanswer.readline()

    status = False
    print("Runs test data")
    result = runCode(test, preamble)

    if result == int(answer): #not always int
        status = True
 
    print("Correct answer: " + answer + "My answer: " + str(result))
    return status
    

def runCode(data, preamble):
    print("Runs code")
    
    print(preamble)
    
    #a list of numbers
    for i in range(preamble, len(data)):
        
        codes = []
        
        for code in data:
            codes.append(int(code))
        
        value = codes[i]
        start = i-preamble
        stop = i
        numbers = codes[start:i]

        found = False

        for j in range(0, len(numbers)-1):
            for k in range(1, len(numbers)):
                if numbers[j]+numbers[k] == value and numbers[j] != numbers[k]:
                    found = True
                    
        if not found:
            print(value)
            return value

    return -1

#Runs testdata
preamble = 5
testResult = testData(preamble)

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    opuzzle = open('input.txt', 'r')
    puzzle = opuzzle.readlines()
    preamble = 25
    finalResult = runCode(puzzle, preamble)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
