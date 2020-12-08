
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
    
    bag_dict = {}

    for line in data:
        line = line.replace('.', '') #remove dot
        line = line.replace('bags', 'bag') #remove plural form
        containing_bag, content = line.split(" contain ")

        for bag in content.strip().split(', '):
            bag = bag.strip()
            
            #Splits upp in bagname and its number
            words = bag.split(' ')
            bagname = ' '.join(words[1:])
            number = words[0]
            
            contains = {}       
            if number == 'no':
                number = 0
            else:
                contains[bagname] = int(number)

            #Sets value depending on if the key exists already or not
            if containing_bag in bag_dict:
                value = (bag_dict[containing_bag.strip()]) #get the value which is a list of bags
            else:
                value = []

            #Set the empty list as value if it's "no other bags"
            if number == 0:
                value = []
            else:
                value.append(contains)                    
                
            #Each main bag goes as key into the dict list with its content as value
            bag_dict[containing_bag.strip()] = value
    
    #print(bag_dict)
    
    #Count the bags starting with the top node
    total_bags = count_bags('shiny gold bag', bag_dict)

    return total_bags
    

def count_bags(current_bag, bag_dict):
    
    returnvalue = 0
    bag_content = bag_dict[current_bag] #list of dicts
    
    if bag_content != []: #if bag has bags inside, else return value is still 0

        #For each bag in the current bag's lists of bags, 
        for bag in bag_content: #dict
            for k in bag:
                v = bag[k]
            returnvalue += v + v*count_bags(k, bag_dict)
        
    return returnvalue

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
