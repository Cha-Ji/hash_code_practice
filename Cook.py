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
(관 음 중) 손~
"""
from Calc_Score import Calc_Score

def Cook(teamList):
    # can cook?
    
    for team in teamList:
      1
    # 재료로 치환
    # ingredient = []
    
    #  
    return 