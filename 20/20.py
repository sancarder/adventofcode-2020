
def testData():

    otest = open('test.txt', 'r')
    test = otest.read()

    oanswer = open('answer.txt', 'r')    
    answer = oanswer.readline()

    status = False
    print("Runs test data")
    result = runCode(test)

    if result == int(answer): #not always int
        status = True
 
    print("Correct answer: " + answer + "My answer: " + str(result))
    return status
    

def runCode(inputString):
    print("Runs code")
    
    #a list of numbers
    tileList = {}

    inputString = inputString.replace("#", "1")
    inputString = inputString.replace(".", "0")
    inputList = inputString.split("\n\n")
    
    for tile in inputList:
        id = tile.split("\n")[0]
        tile = tile.replace (id + "\n", "")
        idNr = int(id.split(" ")[1].replace(":", ""))
        tmpArray = createArray(tile.strip())
        tileList[idNr] = tile    
    
    return -1

def createArray(tile):
    tileList = tile.split("\n")
    
    print(tileList)
    
    tLen = len(tileList)
    tWidth = len(tileList[0])
    
    #tList = [[0] * tLen] * tWidth
    
    tList = [[0] * tWidth for i in range(tLen)]

    
    #tList[5][5] = 1
    #print(tList)
        
    for i, line in enumerate(tileList):
        #print(i, line)
        for j, char in enumerate(line):
            #print(j,char)
            #print(tList[i])
            tList[i][j] = int(char)
            
    for t in tList:
        print(t)
    
    return tList

#Runs testdata
testResult = testData()

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    opuzzle = open('input.txt', 'r')
    puzzle = opuzzle.read()
    finalResult = runCode(puzzle)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
