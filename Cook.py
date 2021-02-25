""""
피자 분배
피자의 총 개수가 다 배달돼야지 최대 값이 나올 것이다 (아마두)
a_example에서 5(피자 총 개수), 1,2,1(2명팀, 3명팀, 4명팀의 수)
5개의 피자를 나누는 조합을 Cook에서 결정
예를 들어 2명인 팀 1, 3명인 팀 2 (새 캘린더 꺼내 올해도 가네)
값을 저장할 때 [1,1,0] 으로 저장

return 값은 피자의 조합들을 담은 리스트로 반환?

 두명 팀엔 피자 2개 보내야하고 세명 팀엔 피자를 3개 보내야함
 그러면 pizzaList[0]이 2명팀 pizzaList[1]이 3명팀 
 5개의 피자를 분배하는 방법?
  2, 3
  0, 4
  2, 2
  team = [[1,1,0], [0,0,1],[2,0,0]]  -> Div_Team
  재료 = [[3,3,0], [0,0,4]] -> Cook
  score = max(3*3*3 + 3*3*3 + 0 , score) -> Calc_Score
 """


"""
# i) 피자를 최대한 많이 배달한다. 
#    - pizzaList[i][j] : 
        i개의 경우의 수
        j+2명 팀에 배달할 피자 개수
# ii)

"""
from Calc_Score import Calc_Score
from itertools import combinations

def Cook(teamList, ingredient):
    index = [x for x in range(len(ingredient))]

    # 재료들을 마구잡이로 집어넣어보자!!
    ingredient_2 = list(combinations(index, 2))
    count_2 = []
    for a, b in ingredient_2:
        count_2.append([[a, b], len(set(ingredient[a]) | set(ingredient[b]))])
    
    ingredient_3 = list(combinations(index, 3))
    count_3 = []
    for a, b, c in ingredient_3:
        count_3.append([[a, b, c], len(set(ingredient[a]) | set(ingredient[b]) | set(ingredient[c]))])

    ingredient_4 = list(combinations(index, 4))
    count_4 = []
    for a, b, c, d in ingredient_4:
        count_4.append([[a, b, c, d], len(set(ingredient[a]) | set(ingredient[b]) | set(ingredient[c]) | set(ingredient[d]))])

    count_2.sort(key = lambda x: -x[1])
    count_3.sort(key = lambda x: -x[1])
    count_4.sort(key = lambda x: -x[1])
    # print("count_2 : 2", count_2)
    # print("count_3 : 3", count_3)
    # print("count_4 : 4", count_4)

    # 결과 값?
    teamResult = []
    scoreResult = 0

    counts = [count_2, count_3, count_4]

    for team in teamList:

        for r in range(2):

            for t in range(3):

                result = []
                score = []
                i = t

                idx = set()

                for _ in range(3):
                    countArray = counts[i]

                    temp = 0

					# team의 갯수만큼 피자를 뽑았다면? 다음 team에서 피자를 뽑는다
                    for index, value in countArray:
                        if team[i] <= temp:
                            break

                        isIn = False
                        tempIdx = set()

                        for x in index:
                            if x in idx:
                                isIn = True
                                break
                            else:
                                tempIdx.add(x)
                        
                        if not isIn:
                            idx = idx | tempIdx
                            temp += 1
                            result.append([i + 2] + list(index))
                            score.append(value)
                    i = (i + 1 + r) % 3

                if Calc_Score(score) > scoreResult:
                    scoreResult = Calc_Score(score)
                    teamResult = result
                    
    # print(finalResult)
    # print(scoreResult)

    # 6개의 배열 중에 가장 스코어가 높은 것을 결과로 가져야한다
    # 문제 : 결과값 출력으로 어떤 피자인지 줘야한다 (우리는 이를 넘겨주지 않았음... 결과 값만 도출해냄)
    
    return teamResult, scoreResult