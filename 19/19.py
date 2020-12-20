
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
    
    rules = {}
    messages = []
    valid = 0
    
    #a list of numbers
    for line in data:
        if ':' in line:
            content = []
            a, b = line.strip().split(':')
            if '\"' in b.strip():
                c = b.split('\"')
                content.append([c[1]])
            else:
                if '|' in b:
                    bs = b.strip().split(' | ')
                    for bss in bs:
                        bsss = bss.split(' ')
                        content.append(bsss)
                else:
                    bs = b.strip().split(' ')
                    #for bss in bs:
                        #content.append(bss)
                    content.append(bs)
                        
                        
            rules[a.strip()] = content

        elif line != '\n':
            messages.append(line.strip())
            
    print(rules)
    print(messages)
            
    for message in messages:
        startmessage = message
        status = False
        #print(message)
        print("\n")
        current_rule = '0'

        #while status != True:
        message, status = check_rule(message, current_rule, rules)
        print("Remaining message = ", message)
        if status and len(message) < 1:
            print(startmessage, "is valid")
            valid += 1
        '''
        if check_rule(message, 0, rules):
            valid+=1
            print("valid")
        '''
        
    print(valid)
    return valid


def check_rule(message, rule, rules):
    status = False
    print("\nChecking rule ", rule, " with message ", message)
    #print(rules)
    print(rules[rule])
    
    if not rules[rule][0][0].isdigit(): #isdigit as cond
        print("Rule is not a digit")
        check = rules[rule][0][0]
        #print("check", check)
        #print(len(check), len(message))
        if message == check:
            print(message, "matches totally")
            message = message[1:]            
            return message, True
        elif len(message) > len(check) and message.startswith(check):
            print(message, "starts with", check)
            message = message[1:]
            return message, True
        elif len(message) == len(check) and message != check:
            print(message, "is one char and doesnt match", check)
            return message, False
        else:
            print(message, "doesn't start with or is equal to", check)
            return message, False

    elif len(rules[rule]) > 1: #with options 1 = [[2,3],[3,2]]
        print("Rules has two options")
        tempmessage = message
        tempstatus = False
        for r in rules[rule][0]: #[2,3]
            tempmessage, tempstatus = check_rule(tempmessage, r, rules)
            if tempstatus == False:
                break
        if tempstatus == True:
            return tempmessage, True

        tempmessage = message
        for r in rules[rule][1]: #[3,2]
            tempmessage, tempstatus = check_rule(tempmessage, r, rules)
            print("Get back status", tempstatus)
            if tempstatus == False:
                return tempmessage, False
        return tempmessage, tempstatus
        
    else: #single rules, no options
        print("Rule has single rules")
        for r in rules[rule][0]:
            print("About to check rule", r)
            message, status = check_rule(message, r, rules)
            if status != True:
                return message, False
        return message, True
    

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
