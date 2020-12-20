
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
        
    all_rules = []
        
    #a list of numbers
    rules, my_ticket, tickets = data.strip().split('\n\n')
    
    #Splitting rules
    rulelist = rules.split('\n')
    print(rulelist)
    
    for rule in rulelist:
        r, content = rule.split(':')
        print(content)
        rs = content.strip().split('or')
        print(rs)
        for x in rs:
            a, b = x.split('-')
            start = int(a)
            stop = int(b)
            for y in range(start,stop+1):
                all_rules.append(y)

    unique_rules = set(all_rules)
    print(unique_rules)

    #Splitting tickets
    nearby_tickets = tickets.split('\n')
    nearby_tickets.pop(0)
    print(nearby_tickets)
    
    invalid_tickets = []
    for t in nearby_tickets:
        nrs = t.split(',')
        for n in nrs:
            nr = int(n)
            if nr in unique_rules:
                pass
            else:
                invalid_tickets.append(nr)

    print(invalid_tickets)
    
    return sum(invalid_tickets)

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
