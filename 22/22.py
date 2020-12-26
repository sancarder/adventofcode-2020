
def testData():

    otest = open('test.txt', 'r')
    test = otest.read()

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
    
    player1 = []
    player2 = []
    
    #a list of numbers
    p1, p2 = data.strip().split('\n\n')
    
    for p in p1.split('\n'):
        player1.append(p)
    for c in p2.split('\n'):
        player2.append(c)
    player1.pop(0)
    player2.pop(0)


    #print(player1)
    #print(player2)
    
    gameOver = False
    winner = []
    round = 0
    
    while not gameOver:
        round += 1
        print("\n-- Round", round)
        #print(player1)
        #print(player2)
        player1, player2 = play(player1, player2)
        
        if len(player1) == 0:
            gameOver = True
            winner = player2
            print("Player 2 wins with deck:")
            print(player2)
            
        elif len(player2) == 0:    
            gameOver = True
            winner = player1
            print("Player 1 wins with deck:")
            print(player1)
            
    score = calculate_score(winner)
            
    print(score)
            
    return score

def play(player1, player2):
    
    print("Player 1:s deck: ", player1)
    print("Player 2:s deck: ", player2)
    
    p1topcard = player1[0]
    player1.pop(0)
    
    p2topcard = player2[0]
    player2.pop(0)
    
    print("Player 1 plays:", p1topcard)
    print("Player 2 plays", p2topcard)
    
    if int(p1topcard) > int(p2topcard):
        player1.append(p1topcard)
        player1.append(p2topcard)
        print("Player 1 wins the round!")
    
    elif int(p2topcard) > int(p1topcard):
        player2.append(p2topcard)
        player2.append(p1topcard)
        print("Player 2 wins the round!")
        
    return player1, player2
    

def calculate_score(player):
    
    player.reverse()
    score = 0
    
    print(player)
    
    for i in range(len(player)):
        value = i+1
        card = player[i]
        
        print(value, card)
        
        score += value*int(card)
        
    return score
        

#Runs testdata
testResult = testData()

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    opuzzle = open('input.txt', 'r')
    puzzle = opuzzle.read()
    finalResult = runCode(puzzle)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
