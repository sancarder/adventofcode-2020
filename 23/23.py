
def testData():

    otest = open('test.txt', 'r')
    test = otest.readline()

    oanswer = open('answer.txt', 'r')    
    answer = oanswer.readline()

    status = False
    print("Runs test data")
    result = runCode(test)
    
    print(type(result))
    print(type(answer))

    if int(result) == int(answer): #not always int
        status = True
 
    print("Correct answer: " + answer + "My answer: " + result)
    return status
    

def runCode(data):
    print("Runs code")
    
    cups = []
    
    #a list of numbers
    for char in data.strip():
        cups.append(int(char))
    
    #Current cup default value
    cc = 0
    
    for i in range(1,101):
        print("-- Move", i)
        cups, cc = actions(cups, cc)
        print("\n")


    print(cups)

    one = cups.index(1)
    a = cups[one+1]
    cups.remove(1)
    b = cups.index(a)
    firsthalf = cups[b:]
    lasthalf = cups[:b]
    
    lastlist = []
    for h in firsthalf:
        lastlist.append(str(h))
    for l in lasthalf:
        lastlist.append(str(l))
    
    answer = ''.join(lastlist)
    print(answer)
    return answer


def actions(cups, cc):
    
    print("cups:", cups)
    
    length = len(cups)
    
    #Modolo = what is left if you divide the right side of the modulo sign with the left side
    #example = 11%10 = 1 because 11 fits in 10 one time and then one is left
    
    #Indexes
    c1 = cc+1%length
    c2 = cc+2%length
    c3 = cc+3%length

    #Current cup
    current_cup = cups[cc]
    print("current:", current_cup)
    
    #Cups to pick up
    cup1 = cups[c1]
    cup2 = cups[c2]
    cup3 = cups[c3]
    
    #Remove cups1-3
    print("pick up:", cup1, cup2, cup3)
    cups.remove(cup1)
    cups.remove(cup2)
    cups.remove(cup3)

    #Find destination_cup
    destination_cup = 0
    i = current_cup-1
    found = False
    
    while not found:
        #print(i, cups)
        if i in cups:
            destination_cup = i
            found = True
        elif i < min(cups):
            destination_cup = max(cups)
            found = True
        else:
            i-=1
        
    dc = cups.index(destination_cup)    
    print("destination:", destination_cup)
    
    #Choose new current cup    
    if cc < len(cups)-1:
        new_current = cups[cc+1]
    else:
        new_current = cups[0]
        
    #print("New current cup", new_current)    
    
    #Insert picked up cups:
    cups.insert(dc+1, cup1)
    cups.insert(dc+2, cup2)
    cups.insert(dc+3, cup3)
    
    #Get the new current cup's index
    new_cc = cups.index(new_current)
    
    '''
    The new current should be at index current_index + 1
    Take this index minus the index where this number is right now.
    Then you get the number of cups that should be removed from the begnning of the list
    and then put as the three last numbers of the list.
    '''
    
    should_be_index = cc+1
    nrofcupstoremove = abs(new_cc-should_be_index)
    
    #print("should be index", should_be_index)
    #print("nr of cups to remove", nrofcupstoremove)

    if nrofcupstoremove != 0:

        #Extract cups
        cupstoremove = []
        for j in range(0,nrofcupstoremove):
            cupstoremove.append(cups[j])
            
        #print("Remove", cupstoremove, "from", cups)

        #Remove cups from the beginning
        for y in range(0,len(cupstoremove)):
            #print(cupstoremove[y])
            cups.remove(cupstoremove[y])
            
        #Put back cups in the end
        for z in range(0,len(cupstoremove)):
            cups.append(cupstoremove[z])

    #Get the new current cup's index
    newest_cc = cups.index(new_current)
        
    #print(cups)
    
    return cups, newest_cc

#Runs testdata
testResult = testData()

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    opuzzle = open('input.txt', 'r')
    puzzle = opuzzle.readline()
    finalResult = runCode(puzzle)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
