a = "a_example"
b = "b_little_bit_of_everything.in"
c = "c_many_ingredients.in"
d = "d_many_pizzas.in"
e = "e_many_teams.in"

# 파일 읽어오기
def Read_File_Suck(path):
    import heapq

    with open("./source/" + path, 'r') as file:
        tempLine = list(map(int, file.readline().split()))
        pizzaCount = tempLine[0]
        Team = tempLine[1:]
        ingredient = []
    
        for n in range(pizzaCount):
            string = file.readline().split()
            heapq.heappush(ingredient, (-int(string[0]), string[1:], n))

    return (Team, pizzaCount, ingredient)

# 입력받기
Team, pizzaCount, ingredient = Read_File_Suck(c)

# 겹치는거 검사? ㅇㅇ got it
# 피자를 2개 -> 3개 -> 4개 순으로 검색
# 이 때 각 Process 에서 갯수가 늘어나지 않으면 전진하지 않고 그 Process 를 채택
finalResult = []
finalScore = []

for alpha, value in enumerate(ingredient):
    # 전부 선택했다면 Finish
    if (not Team[0]) and (not Team[1]) and (not Team[2]):
        break

    result = [value[2]]
    nowPizzas = set(value[1])
    nowLength = len(nowPizzas)

    betaBestIndex = alpha + 1
    for beta in range(alpha + 1, pizzaCount):
        tempLength = len(nowPizzas | set(ingredient(beta)[1]))
        if tempLength > nowLength:
            nowLength = tempLength
            betaBestIndex = beta

    betaCount, betaValue, betaIndex = ingredient.pop(betaBestIndex)
    result.append(betaIndex)
    nowPizzas = nowPizzas | betaValue
    nowLength = len(nowPizzas)

    del betaBestIndex
    del betaCount
    del betaValue
    del betaIndex

    charlieBestIndex = -1
    for charlie, nextValue in enumerate(ingredient):
        if alpha == charlie:
            continue
        
        tempLength = len(nowPizzas | nextValue[1])
        if tempLength > nowLength:
            nowLength = tempLength
            charlieBestIndex = charlie

    if charlieBestIndex == -1 and (Team[0] != 0):
        Team[0] -= 1
        finalResult.append([2] + result)
        finalScore.append(nowLength)
        continue
    
    charlieCount, charlieValue, charlieIndex = ingredient.pop(charlieBestIndex)
    result.append(charlieIndex)
    nowPizzas = nowPizzas | charlieValue
    nowLength = len(nowPizzas)

    del charlieBestIndex
    del charlieCount
    del charlieValue
    del charlieIndex

    deltaBestIndex = -1
    for delta, nextValue in enumerate(ingredient):
        if alpha == delta:
            continue
        tempLength = len(nowPizzas | nextValue[1])
        if tempLength > nowLength:
            nowLength = tempLength
            deltaBestIndex = delta

    if deltaBestIndex == -1 and (Team[1] != 0):
        Team[1] -= 1
        finalResult.append([3] + result)
        finalScore.append(nowLength)
        continue
    
    deltaCount, deltaValue, deltaIndex = ingredient.pop(deltaBestIndex)
    result.append(deltaIndex)
    nowPizzas = nowPizzas | deltaValue
    nowLength = len(nowPizzas)
        
    finalResult.append([4] + result)
    finalScore.append(nowLength)

print(finalResult)
print(finalScore)