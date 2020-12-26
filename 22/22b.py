import copy

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
    
    playerdecks = {}
    playerdecks["player1"] = player1
    playerdecks["player2"] = player2

    gamenr = 1
    winner = start_game(player1,player2, gamenr)
            
    score = calculate_score(playerdecks[winner])
    print(score)
            
    return score

def start_game(player1, player2, gamenr):
    
    print("\n-- Game", gamenr)
    
    gameOver = False
    winner = []
    roundnr = 0
    decks = []
            
    while not gameOver:
        roundnr += 1
        player1, player2, decks = play_round(player1, player2, decks, gamenr, roundnr)
        
        if len(player1) == 0:
            gameOver = True
            winner = "player2"
            #print("Player 2 wins with deck:")
            #print(player2)
            
        elif len(player2) == 0:    
            gameOver = True
            winner = "player1"
            #print("Player 1 wins with deck:")
            #print(player1)

    print("\n-- Game", gamenr, "ends")    
    return winner


def play_round(player1, player2, decks, gamenr, roundnr):
    
    print("\n-- Round", roundnr, "game", gamenr)
    
    #print("Player 1:s deck: ", player1)
    #print("Player 2:s deck: ", player2)
    
    #print(decks)
    
    
    #If the decks in this round are similar to another round, player 1 wins
    if (player1,player2) in decks:
        print("Similar decks - player 1 wins")
        player2 = []
        return player1,player2, decks
    
    
    deckcopy = copy.deepcopy((player1,player2))
    decks.append(deckcopy)
    #print(decks)
    
    p1topcard = player1[0]
    player1.pop(0)
    
    p2topcard = player2[0]
    player2.pop(0)
    
    #print("Player 1 plays:", p1topcard)
    #print("Player 2 plays", p2topcard)
    
    #If both players draw cards of the same value as the lenght of their decks, they play a subgame
    if int(p1topcard) <= len(player1) and int(p2topcard) <= len(player2):
        
        #Their new decks are the next amount of cards in their deck corresponding to the value of the drawn card
        p1copy = player1[0:int(p1topcard)]
        p2copy = player2[0:int(p2topcard)]
        
        subwinner = start_game(p1copy,p2copy, gamenr+1)
        
        if subwinner == "player1":
            player1.append(p1topcard)
            player1.append(p2topcard)
            #print("Player 1 wins the round by a subgame!")
            
        elif subwinner == "player2":
            player2.append(p2topcard)
            player2.append(p1topcard)
            #print("Player 2 wins the round by a subgame!")            
        
    else:
        
        if int(p1topcard) > int(p2topcard):
            player1.append(p1topcard)
            player1.append(p2topcard)
            #print("Player 1 wins the round!")
        
        elif int(p2topcard) > int(p1topcard):
            player2.append(p2topcard)
            player2.append(p1topcard)
            #print("Player 2 wins the round!")
        
    return player1, player2, decks
    

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
