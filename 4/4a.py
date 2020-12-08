
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
    
    passports = []
    passport = ''
    passdict = {}
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    
    #a list of passports
    for line in data:

        if line != '\n':
            passport += line
        else:
            passports.append(passport)
            passport = ''
    passports.append(passport)
    
    #print(passports)
    
    for p in passports:
        status = True
        
        #Replaces newline with space
        pp = p.replace('\n', ' ')
        
        #Check each key is present
        for k in keys:
            if k in pp:
                pass
            else:
                status = False
                
        if status:
            valid+=1
                
    return valid

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
