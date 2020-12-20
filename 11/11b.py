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
    

def runCode(data1):
    print("Runs code")
    
    #a list of numbers
    new_list = []
    similar = False
    
    data = []
    
    for line in data1:
        data.append(line.strip())    
    
    while not similar:

        occupied = 0
        print(data)

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
                    
                
                if seat != '.':
                    adjacents = find_adjs(up, down, right, left, data, ri, si)
                    new_seat = check_seat(seat, adjacents)
                else:
                    new_seat = seat
                new_row += new_seat

            occupied += new_row.count('#')
            new_list.append(new_row)            
        
        #print("\n")
        for line in new_list:
            print(line)
        
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
    print("\n")
    print("Row: ", data[ri], "Seat: ", str(si))

    #Now find the first occurrence in each direction that is not a dot

    if up:
        
        for i in range(ri-1, -1, -1):
            v = data[i][si]
            if v != '.':
                adjacents.append(v)
                print("up")                                                
                break


        if right:
            for i in range(ri-1, -1, -1):
                if si+(ri-i) < len(data[i]):
                    v = data[i][si+(ri-i)]                                   
                    if v != '.':
                        adjacents.append(v)
                        print("up right")                                
                        break
                else:
                    break

        if left:
            for i in range(ri-1, -1, -1):
                if si+(i-ri) >= 0:          
                    v = data[i][si+(i-ri)]
                    if v != '.':
                        adjacents.append(v)    
                        print("up left")                                                    
                        break
                else:
                    break

    if down:

        for i in range(ri+1, len(data)):
            v = data[i][si]
            if v != '.':
                adjacents.append(v)
                print("down")                                
                break


        if right:
            for i in range(ri+1, len(data)):
                if si+(i-ri) < len(data[i]):
                    v = data[i][si+(i-ri)]                    
                    if v != '.': #i?
                        adjacents.append(v)
                        print("down right")                
                        break
                else:
                    break

        if left:
            for i in range(ri+1, len(data)):
                if si+(ri-i) >= 0:          
                    v = data[i][si+(ri-i)]
                    if v != '.':
                        adjacents.append(v)
                        print("down left")                                        
                        break
                else:
                    break

    if right:
        for i in range(si+1, len(data[ri])):
            if data[ri][i] != '.':
                adjacents.append(data[ri][i])
                print("right")
                break

    if left:
        for i in range(si-1, -1, -1): 
            if data[ri][i] != '.':
                adjacents.append(data[ri][i])
                print("left")                
                break
    
    print(adjacents)
    print("\n")
    
    #if input("Next?") == '\n':
        #pass
    
    return adjacents


def check_seat(seat, adjs):
    
    new_seat = seat
    #print(new_seat)
    
    if seat == 'L':
        if '#' not in adjs:
        #if adjs.count('L') == len(adjs):
            new_seat = '#'
            
    if seat == '#':
        if adjs.count('#') > 4:
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
