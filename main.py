import sys
from Read_File import Read_File
from Calc_Score import Calc_Score
from Div_Team import Div_Team
from Cook import Cook

input = sys.stdin.readline

# firstLine = list(map(int, input().split()))
# pizzaCount = firstLine[0]
# Team = firstLine[1:]

Team, pizzaCount, ingredient, ingredientNum = Read_File("파일 이름")

Div_Team("피자")

Cook("팀 조합") # return [pizza1, pizza3, pizza7]

Calc_Score("팀 배열")
# (결과) 피자 나눠주기
print(Div_Team())


