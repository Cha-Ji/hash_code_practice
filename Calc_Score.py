# 점수 계산하기
def Calc_Score(ingredientNum):
    ans = 0
    for i in range(len(ingredientNum)):
        ans += ingredientNum[i] * ingredientNum[i]
    print("점수: \t", ans)

    return ans