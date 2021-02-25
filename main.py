from Read_File import Read_File
from Calc_Score import Calc_Score
from Div_Team import Div_Team
from Cook import Cook
from Result import Result
# 입력받기
Team, pizzaCount, ingredient, ingredientNum = Read_File("b_little_bit_of_everything.in")


teamList = Div_Team(pizzaCount, Team)         # 분배가능한 팀 리스트

dividedTeam, scoreResult = Cook(teamList, ingredient)      # 팀을 확정

print("점수: ",scoreResult)
Result(dividedTeam)              # 결과 출력, 저장 함수

"""
입력  형식
----------------------------
5 1 2 1 
3 onion pepper olive 
3 mushroom tomato basil 
3 chicken mushroom pepper 
3 tomato mushroom basil 
2 chicken basil
"""

"""
출력 형식         | 설명
----------------------------------------------------
2               # 배달에 성공한 팀 수
2 1 4           # 2명 팀에게 배달 성공한 1, 4번 피자
3 0 2 3         # 3명 팀에게 배달 성공한 0, 2, 3번 피자
"""

