
def Read_File(path):
  # a_example에서 읽어오기
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
