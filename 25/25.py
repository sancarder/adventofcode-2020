
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
    
    #a list of public keys
    cardkey = int(data[0].strip())
    doorkey = int(data[1].strip())

    cardloopsize = find_loopsize(int(cardkey))
    doorloopsize = find_loopsize(int(doorkey))
    
    print(cardloopsize)
    print(doorloopsize)
    
    encryption_key1 = calculate_encryption_key(doorkey, cardloopsize)
    encryption_key2 = calculate_encryption_key(cardkey, doorloopsize)

    print(encryption_key1, encryption_key2)
    return encryption_key1


def find_loopsize(publickey):
    
    '''
    To transform a subject number, start with the value 1. Then, a number of times called the loop size, perform the following steps:

    Set the value to itself multiplied by the subject number.
    Set the value to the remainder after dividing the value by 20201227.
    '''

    subnr = 7
    length = 1000
    value = 1
    loopSize = 1
    
    while value != publickey:
        #print(value)
        value = value * subnr
        value = value%20201227
        if value == publickey:
            return loopSize
        loopSize+=1
    
    return -1
    
    
def calculate_encryption_key(key, loopsize):
    
    '''
    The card transforms the subject number of the door's public key according to the card's loop size. The result is the encryption key.
    '''

    subnr = key
    value = 1
    
    for i in range(1, loopsize+1):
        #print(value)
        value = value * subnr
        value = value%20201227


    return value
    
    

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
