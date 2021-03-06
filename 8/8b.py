
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
    
    for i in range(0, len(data)):
    
        codes = data
        accumulator = 0
        index = 0
        backtobeginning = False
        indexvisited = []
            
        while index not in indexvisited:
            
            if index < len(codes):
                            
                op, step = codes[index].split(' ')
                
                if index == i and op == 'nop':
                    op = 'jmp'
                elif index == i and op == 'jmp':
                    op = 'nop'
                
                step = int(step.strip())
                indexvisited.append(index)        
                accumulator, index = execute(accumulator, op, step, index)
                
            else:
                print(accumulator)
                return accumulator
            

def execute(accumulator, op, step, index):
            
    if op == 'nop':
        index +=1
    elif op == 'jmp':
        index += step
    elif op == 'acc':
        accumulator += step
        index +=1
        
    return accumulator, index

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
