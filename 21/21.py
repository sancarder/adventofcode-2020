
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
    
    
    while len(definite) < len(all_allergens):
        print("Entering while loop with:")
        
        for alg in all_allergens:
            print(alg)
            existing_recipes_with_single_allergens = []
            existing_recipes_with_multiple_allergens = []        
            for rec in all_recipes:
                if alg in rec[1] and len(rec[1]) == 1:
                    existing_recipes_with_single_allergens.append(rec)
                elif alg in rec[1] and len(rec[1]) > 1:
                    existing_recipes_with_multiple_allergens.append(rec)
                    
            #print(existing_recipes_with_multiple_allergens)
            #print(existing_recipes_with_single_allergens)
            
            if len(existing_recipes_with_single_allergens) > 1:
                print("Several recipes with single allergens")
                #concatenate all lists into one. Find the word that exists exactly the same number as the number of lists.
                togetherlist = []
                for rec in existing_recipes_with_single_allergens:
                    togetherlist += rec[0]
                    
                for word in existing_recipes_with_single_allergens[0][0]: #loop over any of the recipes:
                    if togetherlist.count(word) == len(existing_recipes_with_single_allergens):
                        definite[alg] = word #add it as definite for this allergen

                for r in all_recipes:
                    if word in r[0]:
                        r[0].remove(word)                         
                                
                
            elif len(existing_recipes_with_single_allergens) == 1:
                print("Exactly one recipe with single allergens")
                
                if len(existing_recipes_with_single_allergens[0][0]) == 1: #if there is only one ingredient
                    print("only one ingredient left")
                    last_ing = existing_recipes_with_single_allergens[0][0][0] 
                    definite[alg] = last_ing #add it as definite for this allergen
                    for r in all_recipes:
                        if last_ing in r[0]:
                            r[0].remove(last_ing)                    
                    
                else:
                    print("Several ingredients left")
                    for food in existing_recipes_with_single_allergens[0]: #loop over words in recipe ingredients
                        for recipe in existing_recipes_with_multiple_allergens:
                            counter, found_ing = match(food, existing_recipes_with_multiple_allergens[0][0])
                            #print(counter, found_ing)
                            if counter == 1:
                                definite[alg] = found_ing
                                
                                for r in all_recipes:
                                    if found_ing in r[0]:
                                        r[0].remove(found_ing)
                                        
            print(definite)
            #print(all_recipes)
                        

    occurrences = 0
    for left in all_recipes:
        occurrences += len(left[0])
        
    print(definite)
    
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
    opuzzle = open('input.txt', 'r')
    puzzle = opuzzle.readlines()
    finalResult = runCode(puzzle)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
