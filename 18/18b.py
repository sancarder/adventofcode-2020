import re

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
    
    answers = []
        
    #If ( in line, send to find innermost.
    #Use regex to find an innermost parentheses
    #Send back the substring that the regex corresponds to and the calculation
    #Replace the substring with the calculation in the line
    
    
    for line in data:
        print(line.strip())
        
        if '(' not in line:
            answer = solvefinal(line.strip())
            print(answer)            
            answers.append(answer)


        else:
            while '(' in line:
                line = line.replace(' ', '')
                print(line)
                match = find_innermost(line.strip())
                print(match)
                #solved = solve(match)
                solved = solvetwo(match)
                print(solved)
                line = line.replace(match,str(solved))
                print(line)
                                            
            line = line.replace('*', ' * ')
            line = line.replace('+', ' + ')
            line = line.strip()

            answer = solvefinal(line)                        
            print(answer)
            answers.append(answer)
    
        print('\n')
    
    print(answers)
    return sum(answers)


def find_innermost(line):
    pattern = r'\((\d+[\*,\+]\d+)+([\*,\+]\d+)*\)'    
    p = re.search(pattern, line)
    return p.group()


def solvetwo(expr):
    expr = expr.replace('(','')
    expr = expr.replace(')','')    
    expr = expr.replace('*', ' * ')
    expr = expr.replace('+', ' + ')
    expr = expr.strip()

    answer = solvefinal(expr)
    print(answer)
        
    return answer
    


def solvefinal(items):

    multsummed = 1  
    addsummed = 0
    summed = 0
    
    if '*' in items:
        additions = items.split(' * ')
        multiply = []
        
        for expr in additions:
            terms = expr.split(' + ')
            for t in terms:
                addsummed += int(t)
            multiply.append(addsummed)
            addsummed = 0
                
                        
        for mult in multiply:
            multsummed *= mult
            
        summed = multsummed
            
        
    else:
        additions = items.split(' + ')
        print(additions)
        for add in additions:
            summed += int(add)
            print(add, summed)
            
    return summed

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
