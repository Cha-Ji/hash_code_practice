# 결과 출력 함수
def Result(team):
    # team[i][0] : i팀 인원
    # team[i][1:]: i팀에게 배달 성공한 피자
    team.sort()
    length = len(team)
    
    print("===========저장될 결과===========")
    print('팀 수: \t\t', len(team))        # 배달에 성공한 팀 수
    for i in team:
        print(i[0],"명 팀:\t" ,end=" ")   
        for j in i[1:]:
            print(j, "\t", end=" ")
        print()
    print("=================================")

    # 결과 저장
    with open("Submission.text", 'w') as f:
        # 총 인원
        f.write(str(length)+ "\n")

        for member in team:

            # i팀 인원
            f.write(str(member[0])+ " ")

            for i in member[1:]:

                # 각 재료, 마지막에 공백이 포함된다 => 출력 형식 주의
                f.write(str(i)+" ")
            
            f.write("\n")
        