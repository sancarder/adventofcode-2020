
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
    
    patterns = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    total_trees = 1
    
    for p in patterns:
            
        position = 0
        trees = 0
        
        right = p[0]
        down = p[1]
                
        #a list of map routes
        for i in range(int(down), len(data), int(down)): #start with going down, then right
            line = data[i].strip()
            rowlength = len(line)
            position += int(right)
                        
            #Check here if pos will go outside range, if so, reset position
            if (position >= rowlength):
                position = position-rowlength
                    
            location = line[position]
            if location == '#':
                trees +=1
                
        print(trees)
                
        total_trees = trees * total_trees
        

    return total_trees

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
