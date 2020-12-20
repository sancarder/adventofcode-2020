import math

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
    
    #939 = minutes since the bus began
    
    #a list of numbers
    buses = []
    departure = int(data[0])
    for b in data[1].split(','):
        if b != 'x':
            buses.append(int(b))
    
    
    #Gives the number of whole hours
    hours = math.floor(939/60)
    #Answer = 39, means 39 minuter more then
    minutes = 939%60    
    
    #buses = [13]
    lowest = min(buses)
    
    '''
    for bus in buses:    
        start = 0
        for hour in range(1,hours):
            for minute in range(start,60, bus):
                print(hour,minute)
                if minute+bus > 59:
                    start = (minute+bus)-60
        for m in range(start, minutes, bus):
            print(hour+1,m)                                
            if m+bus > 59:
                start = (m+bus)-60
    '''
    
    possible_times = []
    possible_buses = []
    
    #This gives the right timestamps for each bus
    for bus in buses:
        for t in range(0,departure+lowest, bus):
            if t >= departure:
                print(t, bus)
                possible_buses.append(bus)
                possible_times.append(t)
                
    nearest_time = min(possible_times)
    index = possible_times.index(nearest_time)
    nearest_bus = possible_buses[index]
    
    wait_time = nearest_time-departure
    answer = wait_time*nearest_bus
    
    print(answer)

    return answer

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
