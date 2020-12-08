
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
    
    seats = []
    
    #a list of boarding passes
    for boarding in data:
        #print(boarding)
        rows = boarding.strip()[:7]
        cols = boarding.strip()[7:]
        
        row = findPosition(rows, 0, 127)
        column = findPosition(cols, 0, 7)
        
        seat = int(row) * 8 + int(column)
        seats.append(seat)
     
    mySeat = findSeat(seats)
     
    return mySeat

def findPosition(positions, first, last):

    seat = -1
    
    #FBFBBFF (F or L = lower half, B or R = upper half)
    while last-first > 1:
        for pos in positions:
            middle = (first+last)//2 #floor division to get integers
            
            #Re-calculate first and last row
            if pos.strip() == 'F' or pos.strip() == 'L':
                last = middle
            elif pos.strip() == 'B' or pos.strip() == 'R':
                first = middle+1
        
        #Calculate middle
        if pos.strip() == 'F' or pos.strip() == 'L':
            seat = middle
        elif pos.strip() == 'B' or pos.strip() == 'R':
            seat = middle+1

    return seat

def findSeat(seats):
    
    seats.sort()

    for i in range(0, len(seats)-1):
        if seats[i+1]-seats[i] == 1:
            pass
        else:
            return seats[i]+1
                    

#Runs testdata
#testResult = testData()
testResult = True

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    opuzzle = open('input.txt', 'r')
    puzzle = opuzzle.readlines()
    finalResult = runCode(puzzle)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
