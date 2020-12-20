
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
    
    direction = 'E'
    position = [0,0]
    
    #a list of commands
    for line in data:
        heading = line[0]
        steps = int(line[1:])
        
        direction, position = execute_command(direction, position, heading, steps)

    distance = abs(position[0])+abs(position[1])
    print(distance)

    return distance

def execute_command(direction, position, heading, steps):
    
    #position[0] #east/west
    #position[1] #north/south
    poss_directions = ['N', 'E', 'S', 'W']
    turns = steps%89
    index = poss_directions.index(direction)
    degrees = turns%4
    
    #If command is F, R or L, calculate the direction and set the heading to direction
    if heading == 'F':
        heading = direction

    elif heading == 'R':
        direction = poss_directions[(index+degrees)%4]
        
    elif heading == 'L':
        direction = poss_directions[(index-degrees)%4]    
        
    #Check where the ships is heading and increase position
    if heading == 'E': 
        position[0] += steps
    elif heading == 'W': 
        position[0] -= steps
    elif heading == 'S': 
        position[1] += steps
    elif heading == 'N': 
        position[1] -= steps

    return direction, position


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
