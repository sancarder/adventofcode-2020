
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
    
    memory = []
    jump = 1
    maskdict = {}
    
    #a list of numbers
    for i in range(0, len(data), jump):
        if 'mask' in data[i]:
            jump = 0
            memories = []
            mask = data[i].split("=")[1].strip()
            #print(mask)
            if i+1 != len(data):
                while "mask" not in data[i+1]:
                    memories.append(data[i+1].strip())
                    #jump +=1
                    i+=1
                    #print(memories)
                maskdict[mask] = memories
                print(maskdict)
        else:
            pass
                

    print maskdict
                

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
