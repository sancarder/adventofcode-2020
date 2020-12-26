
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

    length = 100
    width = 100
    startrow = length//2
    startcell = width//2
    

    blackSwaps = 0
    blackTiles = 0

    grid = [[0] * length for i in range(width)]
    
    #print(grid)
    
    #a list of numbers
    for line in data:
        steps = []
        swappedToBlack = False
        linelist = list(line.strip())
        print(line)
        i = 0
        while len(linelist) >= 1:
            #print(linelist)
            #print(linelist[i])
            if linelist[i] in ['e', 'w']:
                steps.append(linelist[i])
                linelist.remove(linelist[i])
                    
            elif linelist[i] in ['s', 'n']:
                steps.append(linelist[i]+linelist[i+1])
                linelist.remove(linelist[i])
                linelist.remove(linelist[i])
              
              
        swappedToBlack, grid = walk(steps, grid, startrow, startcell)
        
        if swappedToBlack:
            blackSwaps+=1
            
            
        #print(steps)
        print('\n')
            
    
    #print(grid)
    
    #print("Black swaps:", blackSwaps)

   
    for row in grid:
        for cell in row:
            #print(cell)
            if cell == 1:
                blackTiles+=1
   
    print(blackTiles)
    return blackTiles

def walk(steps, grid, row, cell):
    
    swappedToBlack = False
    
    for step in steps:
        if step == 'e':
            cell+=2
        if step == 'w':
            cell-=2            
        if step == 'se':
            row+=1
            cell+=1          
        if step == 'ne':
            row-=1
            cell+=1           
        if step == 'sw':
            row+=1
            cell-=1           
        if step == 'nw':
            row-=1
            cell-=1            
            
    #print(grid[row][cell])        
    
    if grid[row][cell] == 0:
        grid[row][cell] = 1
        swappedToBlack = True
    elif grid[row][cell] == 1:
        grid[row][cell] = 0
    
    #print(grid[row][cell])            
    
    return swappedToBlack, grid

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
