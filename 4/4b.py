
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
        allFieldsPresent = True
        
        #Replaces newline with space
        pp = p.replace('\n', ' ')
        
        #Check each key is present
        for k in keys:
            if k in pp:
                pass
            else:
                allFieldsPresent = False
                
        if allFieldsPresent:
            if checkPassport(pp.strip().split(' ')):
                valid+=1
                
    return valid

def checkPassport(passports):
    
    status = True
    
    for passport in passports:
        #print(passport)
        key, value = passport.split(':')
        #print(key, value)
        
        if key == 'byr':
            print(key, value)
            if (len(value) == 4 and value.isdigit()):
                if (int(value) >= 1920 and int(value) <= 2002):
                    pass
                else:
                    status = False
            else:
                status = False

            print(status)

        if key == 'iyr':
            print(key, value)            
            if (len(value) == 4 and value.isdigit()):
                if (int(value) >= 2010 and int(value) <= 2020):
                    pass
                else:
                    status = False
            else:
                status = False

            print(status)
                

        if key == 'eyr':
            print(key, value)            
            if (len(value) == 4 and value.isdigit()):
                if (int(value) >= 2020 and int(value) <= 2030):
                    pass
                else:
                    status = False
            else:
                status = False

            print(status)
                
        if key == 'hgt':
            print(key, value)            
            if 'cm' in value:
                height, unit = value.split('cm')
                if (int(height) >= 150 and int(height) <= 193):
                    pass
                else:
                    status = False

            elif 'in' in value:
                height, unit = value.split('in')
                if (int(height) >= 59 and int(height) <= 76):
                    pass
                else:
                    status = False                
            else:
                status = False

            print(status)
                
        if key == 'hcl':
            print(key, value)            
            if value.startswith('#'):
                if len(value[1:]) == 6:
                    if value[1:].isalnum():
                        pass
                    else:
                        status = False
                else:
                    status = False
            else:
                status = False

            print(status)
                
        if key == 'ecl':
            print(key, value)            
            if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                pass
            else:
                status = False

            print(status)                
                
        if key == 'pid':
            print(key, value)            
            if (len(value) == 9 and value.isdigit()):
                pass
            else:
                status = False

            print(status)                

    print(status)
    print('\n\n\n')
    return status

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
