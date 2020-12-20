import math
import copy

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
    buses = []
    original_deps = []
    
    departure = data[0]
    for b in data[1].split(','):
        if b != 'x':
            buses.append(int(b))
        else:
            buses.append(b)
            original_deps.append(b)
            
    original_deps.append(buses[0])
    
    timestamp = 0    
    found = False
    
    
    while not found: #just a test number

        print("Not found, try with next departure")
        #print("\n")
        #print("Timestamp:", timestamp)
        
        deps = copy.deepcopy(original_deps)        
        #print(deps)
                
        for index, bus in enumerate(buses):
            #print(index)
            if bus == 'x':
                pass
            elif index == 0:
                pass
            else:
                #print(index, bus)
                for x in range(0,3500,bus):
                    if x == timestamp+index:
                        #print(timestamp, x, index, bus)
                        deps.append(bus)
                        break                                

        print(deps)
        print("\n")
        if len(deps) == len(buses):
            found = True
            break
        
        timestamp +=buses[0] #jump by first bus

    print(timestamp)

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
