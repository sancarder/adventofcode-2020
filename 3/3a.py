
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
    
    position = 0
    trees = 0
    
    pattern = data[0]
    right, down = pattern.split(':')
    
    #a list of map routes
    for i in range(2, len(data), int(down)): #start on line 3 - first line is pattern, first line in map is ignored
        line = data[i].strip()
        rowlength = len(line)
        position += int(right)
        
        print(position, len(line))
        
        #Check here if pos will go outside range, if so, add a line (line + line) and then go steps
        if (position >= rowlength):
            position = position-rowlength
                
        location = line[position]
        if location == '#':
            trees +=1

    return trees

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
