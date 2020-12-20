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
        
    #a list of numbers
    
    #If ( in line, send to find innermost.
    #Use regex to find an innermost parentheses
    #Send back the substring that the regex corresponds to and the calculation
    #Replace the substring with the calculation in the line
    
    
    for line in data:
        print(line.strip())
        
        if '(' not in line:
            answer = solvefinal(line.strip().split(' '))
            print(answer)            
            answers.append(answer)


        else:
            while '(' in line:
                line = line.replace(' ', '')
                match = find_innermost(line.strip())
                #solved = solve(match)
                solved = solvetwo(match)
                print(match, solved)
                line = line.replace(match,str(solved))
                                            
            line = line.replace('*', ' * ')
            line = line.replace('+', ' + ')
            line = line.strip()
            items = line.split(' ')
            
            answer = solvefinal(items)
            
            print(answer)
            answers.append(answer)

    print(answers)
    return sum(answers)

def calculate(summed, op, term):
        
    if op == '*':
        answer = int(summed)*int(term)
        
    elif op == '+':
        answer = int(summed)+int(term)
        
    else:
        answer = -1
        
    return answer
    

def find_innermost(line):
    
    #Regex should be "(digit*or+digitatleastonce*or+optional)"
    pattern = r'\((\d+[\*,\+]\d+)+([\*,\+]\d+)*\)'    
    p = re.search(pattern, line)
    return p.group()


def solvetwo(expr):
    print("In solvetwo", expr)
    expr = expr.replace('(','')
    expr = expr.replace(')','')    
    expr = expr.replace('*', ' * ')
    expr = expr.replace('+', ' + ')
    expr = expr.strip()
    items = expr.split(' ')
        
    answer = solvefinal(items)
    
    print(answer)
    print(type(answer))
    return answer
    

def solvefinal(items):

    summed = 0
    op = '+'
    answer = 0
    
    print(items)
    
    for i in range(0, len(items)):
        #print(items[i])
        if items[i].isdigit():
            summed = calculate(summed, op, items[i])
            #print(summed)
        else:
            op = items[i]
            
        i+=1
            
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
