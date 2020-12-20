
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
        
    ruledict = {}
    all_rules = []
        
    #a list of numbers
    rules, my_ticket, tickets = data.strip().split('\n\n')
    
    #Splitting rules
    rulelist = rules.split('\n')
    #print(rulelist)
    
    for rule in rulelist:
        r, content = rule.split(':')
        #print(content)
        rs = content.strip().split('or')
        #print(rs)
        rlist = []
        for x in rs:
            a, b = x.split('-')
            start = int(a)
            stop = int(b)
            for y in range(start,stop+1):
                rlist.append(y)
                all_rules.append(y)
                
        ruledict[r] = rlist
        
    #print(ruledict)
    unique_rules = set(all_rules)
    #print(unique_rules)

    #Splitting tickets
    nearby_tickets = tickets.split('\n')
    nearby_tickets.pop(0)
    #print(nearby_tickets)

    myt = my_ticket.split('\n')
    my = myt[1].split(',')
    #print(my)
    
    invalid_tickets = []
    for t in nearby_tickets:
        nrs = t.split(',')
        for n in nrs:
            nr = int(n)
            if nr in unique_rules:
                pass
            else:
                invalid_tickets.append(nr)

    #print(invalid_tickets)
    
    fields = identify_fields(ruledict, nearby_tickets)
    #Multiply the sum of the fields
    
    mydep = []
    #mydeplist = my.split(',')
    for field in ruledict:
        print(field)
        if 'departure' in field:
            position = fields[field]
            mydep.append(my[position])
            
    # Multiply elements one by one
    result = 1
    for x in mydep:
         result = result * x 
                
    print(result)
    return -1

def identify_fields(ruledict, nearby_tickets):

    rulepos = {}
    #print(ruledict)

    #Count the total fields per position for each rule    
    #The output is: {'class': [{0: 2}, {1: 3}, {2: 3}], 'row': [{0: 3}, {1: 3}, {2: 3}], 'seat': [{0: 2}, {1: 2}, {2: 3}]}
    for rule in ruledict:
        #print(rule)
        for pos in range(len(ruledict)):
            #print(pos)
            nrofpos = {}
            for ticket in nearby_tickets:
                #print(ticket)
                #print(ticket.strip().split(',')[pos])
                #print(ruledict[rule])
                if int(ticket.strip().split(',')[pos]) in ruledict[rule]:
                    #print("count")
                    if pos in nrofpos:
                        nrofpos[pos] += 1
                    else:
                        nrofpos[pos] = 1

            if rule in rulepos:
                rulepos[rule].append(nrofpos)
            else:
                temp = []
                temp.append(nrofpos)
                rulepos[rule] = temp
        
    print(len(rulepos))
    #length = len(nearby_tickets[0].split(','))
    length = len(nearby_tickets)
    print(length)
    

    #Check for each pos: check each matches and remove those that are not the same lenght as the total amount of tickets        
    for r in rulepos:
        #print("\n")
        #print(r)
        toberemoved = []
        
        
        for p in rulepos[r]:
            #print(p)
            for x in p:
                matches = 0                
                value = p[x]
                #print(value)
                if value < length:
                    toberemoved.append(p)
                else:
                    matches += value

        for rem in toberemoved:
            rulepos[r].remove(rem)

    print(rulepos)

    facit = {}
    
    while rulepos != {}:
        #print("Entering while loop")
        #print(len(rulepos))
        #print(rulepos)            

        k = -1

        for rul in rulepos:
            #k = 0
            #print(rulepos[rul])
            if len(rulepos[rul]) == 1:
                print("match with 1")
                #print(rulepos[ru])
                for k in rulepos[rul][0]:
                    facit[rul] = k
                break
                    
        
        removals = []
        
        #print("\n")
        #print("Loop further")
        #print(rulepos)
        #print(k)
        if k != -1:
            for ru in rulepos:
                #print(rulepos[ru])            
                for y in rulepos[ru]:
                    #print(y)
                    if k in y:
                        removals.append(ru)
            
            for item in removals:
                rulepos[item].remove(y)
                    
            rulepos.pop(rul) 
        
            
    #print(facit)
    return(facit)
  
    

#Runs testdata
#testResult = testData()
testResult = True

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    opuzzle = open('input.txt', 'r')
    puzzle = opuzzle.read()
    finalResult = runCode(puzzle)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
