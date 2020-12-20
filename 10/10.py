  
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
    
    ads = []
    
    for ad in data:
        ads.append(int(ad))
        
    #sort the list
    adapters = sorted(ads)
    
    outlet = 0
    onejolts = 0
    threejolts = 0


    #Any given adapter can take an outlet 1, 2 or 3 volts lower
    #That means any given output can take an adapter 1, 2 or 3 volts higher
    #Since the list is sorted, just go with them one after another?
    
    if adapters[0]-outlet == 1:
        onejolts+=1
    elif adapters[0]-outlet == 3:
        threejolts+=1
        
    for i in range(0, len(adapters)-1):
        if int(adapters[i+1])-int(adapters[i]) == 1:
            onejolts+=1
            print(int(adapters[i]))
        if int(adapters[i+1])-int(adapters[i]) == 3:
            threejolts+=1

    #Add one to threejolts for the device where the difference always is three
    threejolts+=1
        
    result = onejolts*threejolts

    return result

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
