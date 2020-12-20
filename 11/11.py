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
    new_list = []
    similar = False
    
    
    while not similar:

        occupied = 0
        #print(data)

        new_list = []
        
        for ri in range(0, len(data)):
            
            
            row = data[ri]            
            new_row = ''
            
            for si in range(0, len(row)):
                seat = row[si]
                up = False
                down = False
                right = False
                left = False
                
                if ri != 0: #If it's not on row 1, it's ok to search on the row above
                    up = True
                if ri != len(data)-1: #if it's not on the last row, it's ok to search on the row below
                    down = True
                if si != 0: #if it's not the first position on the row, it's ok to search to the left
                    left = True
                if si != len(row)-1: #if it's not the last position on the row, it's ok to search to the right
                    right = True
                    
                adjacents = find_adjs(up, down, right, left, data, ri, si)
                
                new_seat = check_seat(seat, adjacents)
                new_row += new_seat

            occupied += new_row.count('#')
            new_list.append(new_row)            
        
        #print("\n")
        #for line in new_list:
            #print(line)
        
        #if input("Continue?") == "\n":
            #continue

        if data != new_list:
            #print("Not similar, go on")
            data = copy.deepcopy(new_list)
        else:
            print("Similar, stop")
            similar = True

    print(occupied)

    return occupied

def find_adjs(up, down, right, left, data, ri, si):

    adjacents = []
    upright = 0
    upleft = 0
    downright = 0
    downleft = 0

    if up:
        up = data[ri-1][si]
        adjacents.append(up)
        if right:
            upright = data[ri-1][si+1]
            adjacents.append(upright)
        if left:
            upleft = data[ri-1][si-1]
            adjacents.append(upleft)

    if down:
        down = data[ri+1][si]
        adjacents.append(down)        
        if right: 
            downright = data[ri+1][si+1]
            adjacents.append(downright)            
        if left:
            downleft = data[ri+1][si-1]                
            adjacents.append(downleft)

    if right:
        right = data[ri][si+1]                    
        adjacents.append(right)       

    if left:
        left = data[ri][si-1]
        adjacents.append(left)                    
    
    return adjacents


def check_seat(seat, adjs):
    
    new_seat = seat
    #print(new_seat)
    
    if seat == 'L':
        if '#' not in adjs:
        #if adjs.count('L') == len(adjs):
            new_seat = '#'
            
    if seat == '#':
        if adjs.count('#') > 3:
            new_seat = 'L'

    #print(new_seat)
    return new_seat

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
