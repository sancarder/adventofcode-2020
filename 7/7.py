
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
    
    #a list of bags
    #goal: to be able to look up a specific bag and see what bags it can be in
    #light red bags contain 1 bright white bag, 2 muted yellow bags.
    #faded blue bags contain no other bags.


    for line in data:
        #print(line)
        line = line.replace('.', '') #remove dot
        line = line.replace('bags', 'bag') #remove plural form
        containing_bag, content = line.split(" contain ")
        for bag in content.strip().split(', '):
            bag = bag.strip()
            #Splits upp in bagname and its number
            words = bag.split(' ')
            bagname = ' '.join(words[1:])
            number = words[0]
            
            if bagname == 'no other bag':
                pass
            else:       

                #Each content bag goes as key into the dict list with the main bag as value
                if bagname in bag_dict:
                    value = (bag_dict[bagname.strip()]) #get the value which is a list of bags
                else:
                    value = []

                value.append(containing_bag)                    
                bag_dict[bagname.strip()] = value
    
    #print(bag_dict)
    
    counter = check_bag('shiny gold bag', bag_dict, [])
    #Need to subtract 1 in the end?
    
    print(counter-1)
    return counter-1

def check_bag(bag, bag_dict, checked):
    
    print("\nChecking for " + bag)
    print("Checked bags: ")
    print(checked)
    
    if bag not in checked:
        print("Bag has not been checked")
        if bag in bag_dict:
            print("Bag is in the dictionary")
            print("Bag can be in:")
            print(bag_dict[bag])

            for b in bag_dict[bag]:
                check_bag(b, bag_dict, checked)

        checked.append(bag)
    
    return len(checked)

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
