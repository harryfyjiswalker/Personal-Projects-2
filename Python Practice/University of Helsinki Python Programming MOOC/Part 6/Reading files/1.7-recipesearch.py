# filename = "recipes1.txt"
# search = "cake"

# recipedict = {}
# recipelist = []
# names = []
# timings = []
# ingredients = []
# indices = [2]

# number = 1
# with open("recipes1.txt") as new_file:
#     filelist = [line.strip() for line in new_file] 
#     for i in range(len(filelist)):
#         if filelist[i] == '':
#             indices.append(i-1)
#             indices.append(i+3)
#     indices.append(len(filelist)-1)
#     #print(indices)
#     for i in range(len(filelist)):
#         if i == 0 or filelist[i-1] == '':
#             names.append(filelist[i])
#             timings.append(filelist[i+1])
#     for i in range(0,len(indices),2):
#         ingredients.append(filelist[indices[i]:indices[i+1]+1])
#     for i in range(len(names)):
#         recipedict[names[i]] = [timings[i], ingredients[i]]
#     #print(recipedict)

def search_by_name(filename:str, word:str):
    found_recipes = []
    with open(f"{filename}") as new_file1:
        filelist = [line.strip() for line in new_file1] 
        names = []
        for i in range(len(filelist)):
            if i == 0 or filelist[i-1] == '':
                names.append(filelist[i])
        for i in range(len(names)):
            if word.lower() in names[i].lower():
                found_recipes.append(names[i])
        return found_recipes
        
def search_by_time(filename:str, prep_time:int):
    timings = []
    names =[]
    found_recipes = []
    with open(f"{filename}") as new_file:
        filelist = [line.strip() for line in new_file] 
        for i in range(len(filelist)):
            if i == 0 or filelist[i-1] == '':
                names.append(filelist[i])
                timings.append(filelist[i+1])
        for i in range(len(timings)):
            if int(timings[i]) <= prep_time:
                found_recipes.append(f"{names[i]}, preparation time {timings[i]} min")
        return found_recipes

def search_by_ingredient(filename:str, ingredient:str):
    found_recipes = []
    recipedict = {}
    recipelist = []
    names = []
    timings = []
    ingredients = []
    indices = [2]
    number = 1
    with open(f"{filename}") as new_file:
        filelist = [line.strip() for line in new_file] 
        for i in range(len(filelist)):
            if filelist[i] == '':
                indices.append(i-1)
                indices.append(i+3)
        indices.append(len(filelist)-1)
        #print(indices)
        for i in range(len(filelist)):
            if i == 0 or filelist[i-1] == '':
                names.append(filelist[i])
                timings.append(filelist[i+1])
        for i in range(0,len(indices),2):
            ingredients.append(filelist[indices[i]:indices[i+1]+1])
        for i in range(len(names)):
            recipedict[names[i]] = [timings[i], ingredients[i]]
        for k, v in recipedict.items():
            for i in range(len(v[1])):
                if ingredient.lower() in v[1][i].lower():
                    found_recipes.append(f"{k}, preparation time {v[0]} min")
        return found_recipes

if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)



