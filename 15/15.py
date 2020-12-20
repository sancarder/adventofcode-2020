
def testData():

    otest = open('test.txt', 'r')
    test = otest.readline()

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

    seen = {}
    speak = 0
    
    #a list of numbers
    numbers = data.strip().split(',')
        
    for turn, n in enumerate(numbers):
        turns = []
        print("Turn: ", turn+1)
        
        number = int(n)
        #print("Number: ", number)
        
        speak = number
        turns.append(turn+1)
        seen[speak] = turns
        
        #print("Speak: ", speak)
    print("Seen: ", seen)
        
    turn+=2
    
    while turn < 30000001: #2021
        
        if turn%1000000 == 0:
            print(turn)
        
        #print("\n")
        #print("Turn: ", turn)
        
        #print("Last spoken: ", speak)
    
        if speak in seen:
            last_turns = seen[speak]
            last_turn = seen[speak][len(last_turns)-1]
            
            if len(last_turns) > 1:
                #print("Last spoken has more than one last turn")
                last_index = len(last_turns)-1
                speak = last_turns[last_index]-last_turns[last_index-1]
                

                if speak in seen:
                    #print(speak, " has been seen before")
                    last_turns = seen[speak]
                    last_turns.append(turn)
                    seen[speak] = last_turns
                    
                else:
                    seen[speak] = [turn]


                
            elif len(last_turns) == 1:
                #print("Last spoken has been seen once before")    
                
                speak = 0
                
                if speak in seen:
                    #print(speak, " has been seen before")
                    last_turns = seen[speak]
                    last_turns.append(turn)
                    seen[speak] = last_turns
                    
                else:
                    seen[speak] = [turn]
                                    
            
        else:
            #print("Last spoken was spoken first time")
            speak = 0
            seen[speak] = [turn]
        
        turn+=1
        
    print(speak)


    return speak

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
