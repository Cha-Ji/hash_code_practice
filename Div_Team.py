# (효율) 팀 배분하기
# 가능한 팀 조합
def Div_Team(pizzaCount, Team):
    canTeam = []
    print(pizzaCount)
    # 2x + 3y + 4z = pizzaCount
    # z : 0 ~ p//4
    # y : 0 ~ p - z
    # x : 0 ~ p - z - y

    for z in range(pizzaCount//4):
        rest_z = pizzaCount - z
        for y in range(rest_z//3):
            rest_y = rest_z - y
            for x in range(rest_y//2):
                canTeam.append([x,y,z])

    print(canTeam)
    return canTeam