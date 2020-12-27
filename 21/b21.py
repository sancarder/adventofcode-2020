
def testData():

    otest = open('./21/test.txt', 'r')
    test = otest.readlines()

    oanswer = open('./21/answer.txt', 'r')    
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
    
    foodlist = []
    all_allergens = []
    all_ings = []
    all_recipes = []
    definite = {}

        
    #a list of numbers
    for line in data:
        print(line)
        recipe = []
        foods, allergens = line.strip().split(" (")
        ings = foods.split(" ")
        allergens = allergens.replace("contains ", '')
        allergens = allergens.replace(")", '')
        allergenlist = allergens.split(", ")
        recipe = [ings, allergenlist]
        all_recipes.append(recipe)
        
        for a in allergenlist:
            if a not in all_allergens:
                all_allergens.append(a)
        for i in ings:
            if i not in all_ings:
                all_ings.append(i)

    print("Allergens and ingredients:")
    print(all_allergens)
    print(all_ings)
    
    grid = [[True] * len(all_ings) for i in range(len(all_allergens))]

    
    for recipe in all_recipes:
        for i, alg in enumerate(all_allergens):
            if alg in recipe[1]:
                for j, ing in enumerate(all_ings):
                    if ing not in recipe[0]:
                        grid[i][j] = False

    while len(definite) < len(all_allergens):
        for i, row in enumerate(grid):
            if row.count(True) == 1:
                index = row.index(True)
                definite[i] = index
                for j, r in enumerate(grid):
                    grid[j][index] = False

                        
    to_remove = []
    #Remove the trues from all_ings
    for alg in definite:
        a = definite[alg]
        v = all_ings[a]
        to_remove.append(v)

    for ing in to_remove:
        all_ings.remove(ing)

    occurrences = 0

    #Loop over all_ings to find the leftovers
    for ing in all_ings:
        for rec in all_recipes:
            occurrences += rec[0].count(ing)
        
    
    '''
    Goal: Find the ingredient that is the only one for a specific allergen to be found in another row where the same allergen is one of several. Then we can eliminate this ingredient to belong to this allergen. If theere are rows where it's only a single ingredient, it's the one. 
    Save this find in a dict with the allergen as key. Remove this ingredient from all  rows, even the own one.
    In the end, collect the ingredients that are still on the rows and count how many times they appear and sum it. 
    
    '''
    
    print(occurrences)
    return occurrences


def match(recipe1, recipe2):
    #Recipe is a list of ingredients

    counter = 0
    found = ''
    #print(recipe1)
    for ing in recipe1:
        #print(ing)
        if ing in recipe2:
            found = ing
            counter+=1
            
    return counter, found        


#Runs testdata
testResult = testData()

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    opuzzle = open('./21/input.txt', 'r')
    puzzle = opuzzle.readlines()
    finalResult = runCode(puzzle)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
