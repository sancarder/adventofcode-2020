
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
    
    shipdirection = 'E'
    ship = [0,0]
    waypoint = [10, -1]

    print("Ship: ", ship)
    print("Waypoint: ", waypoint)
    
    #a list of commands
    for line in data:
        
        print(line.strip())
        
        heading = line[0]
        steps = int(line[1:])
        
        shipdirection, ship, waypoint = execute_command(shipdirection, ship, heading, steps, waypoint)
        
        print("Ship: ", ship)
        print("Waypoint: ", waypoint)        

    distance = abs(ship[0])+abs(ship[1])
    print(distance)

    return distance

def execute_command(shipdirection, ship, heading, steps, waypoint):
    
    #position[0] #east/west
    #position[1] #north/south
    
    turns = steps%89
    degrees = turns%4 #needed for the last item to be able to pick the first in the list

    #Ship moves by multiplying the waypoint with steps, waypoint stays    
    if heading == 'F': 
        ship[0] += waypoint[0]*steps
        ship[1] += waypoint[1]*steps
        
    elif heading == 'L':
        degrees = (4-degrees)%4 #re-write the degree to the corresponding degree for a right turn...

    #Ship stays, waypoint turns (both directions)
    if heading == 'R' or heading == 'L':

        #... which means that we only need one set of rules for the different number of degrees, whether the turn is left or right
        if degrees == 1:
            x = waypoint[0]
            y = waypoint[1]
        
            waypoint[0] = -y
            waypoint[1] = x
            
        elif degrees == 2:
            waypoint[0] = -waypoint[0]            
            waypoint[1] = -waypoint[1]

        elif degrees == 3:
            x = waypoint[0]
            y = waypoint[1]
        
            waypoint[0] = y
            waypoint[1] = -x            

        
    #Ship stays, waypoint moves
    if heading == 'E': 
        waypoint[0] += steps
    elif heading == 'W': 
        waypoint[0] -= steps
    elif heading == 'S': 
        waypoint[1] += steps
    elif heading == 'N': 
        waypoint[1] -= steps

    return shipdirection, ship, waypoint

    

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
