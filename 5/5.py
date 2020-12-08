
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
                
    return max(seats)

def findPosition(positions, first, last):

    seat = -1
    
    #FBFBBFF (F or L = lower half, B or R = upper half)
    while last-first > 1:
        for pos in positions:
            #print(pos)
            #print(first, last)
            middle = (first+last)//2 #floor division to get integers
            
            if pos.strip() == 'F' or pos.strip() == 'L':
                last = middle
            elif pos.strip() == 'B' or pos.strip() == 'R':
                first = middle+1
                                
        if pos.strip() == 'F' or pos.strip() == 'L':
            seat = middle
        elif pos.strip() == 'B' or pos.strip() == 'R':
            seat = middle+1

    return seat

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
