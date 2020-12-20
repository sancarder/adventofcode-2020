  
def testData():

    otest = open('test2.txt', 'r')
    test = otest.readlines()

    oanswer = open('answer2.txt', 'r')    
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
    threes = []
    rest = []
    
    for i in range(0, len(adapters)-1):
        if int(adapters[i+1])-int(adapters[i]) == 3:
            threes.append(int(adapters[i]))
            threes.append(int(adapters[i+1]))

    #Add the last item in adapters which should always be in
    threes.append(adapters[len(adapters)-1])
    
    for k in adapters:
        if int(k) not in threes:
            rest.append(k)

    groups = make_groups(rest)
    answer = calculate(groups)
        
    return answer


def make_groups(rest):
    
    #Divides the rest into its groups    
    groups = []
    group = []            
    for i in range(0, len(rest)-1):        
        if int(rest[i+1])-int(rest[i]) == 1:
            group.append(int(rest[i]))
        else:
            group.append(int(rest[i]))
            groups.append(group)
            group = []
    group.append(rest[len(rest)-1])    
    groups.append(group)    
    
    return groups


def calculate(groups):
    
    answer = 1
    
    for g in groups:
        size = len(g)
        cube = 2**size
        
        if size > 2:
            cube -=1
        
        answer = answer * cube

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
