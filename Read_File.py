# 파일 읽어오기
def Read_File(path):
    with open("./source/" + path, 'r') as file:
        tempLine = list(map(int, file.readline().split()))
        pizzaCount = tempLine[0]
        Team = tempLine[1:]
        ingredient = [0] * pizzaCount
        ingredientNum = [0] * pizzaCount
    
        for n in range(pizzaCount):
            string = file.readline().split()
            ingredientNum[n] = int(string[0])   #재료의 갯수
            ingredient[n] = string[1:]          #재료의 종류

    return (Team, pizzaCount, ingredient, ingredientNum)
"""
입력 형식
----------------------------
5 1 2 1 
3 onion pepper olive 
3 mushroom tomato basil 
3 chicken mushroom pepper 
3 tomato mushroom basil 
2 chicken basil
"""