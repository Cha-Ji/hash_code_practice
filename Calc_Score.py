# 점수 계산하기
def Calc_Score(ingredient):
    ans = 0
    for i in range(len(ingredient)):
        ans += ingredient[i] * ingredient[i]
    # print("점수: \t", ans)

    return ans