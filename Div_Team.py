# 가능한 팀 조합
def Div_Team(pizzaCount, Team):
    teamList = []

    for z in range(pizzaCount//4 + 1):

        rest_z = pizzaCount - z * 4
        for y in range(rest_z//3 + 1):

            rest_y = rest_z - y * 3
            x = rest_y//2
            
            teamList.append([x,y,z])

    # print("가능한 팀 배열: ", teamList)
    return teamList