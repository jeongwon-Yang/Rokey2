# #===========================================================================
# # #problem_1
# 라운드 수를 맞추자

def solution(N, A, B):
    round_count = 0        # 라운드 수
    
    while A != B:  # A와 B가 서로 만날 때까지
        A = (A + 1) // 2      # 
        B = (B + 1) // 2
        round_count += 1      # 라운드 진행할때 마다 카운트
    
    return round_count

# print(solution(8, 3, 7))


# #===========================================================================
# # #problem_2

def sol(q):
    result = []
    
    for i in q:
        parts = i.split()    # 공백으로 나눔
        X = int(parts[0])    # 첫번째 숫자 
        operator = parts[1]  # 두번째 연산자
        Y = int(parts[2])    # 세번째 숫자
        Z = int(parts[4])    # 연산 결과
        
        if operator == '+':
            if X + Y == Z:
                result.append("O")
            else:
                result.append("X")
        elif operator == '-':
            if X - Y == Z:
                result.append("O")
            else:
                result.append("X")
    
    return result

# result =  ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
# result1 = ["3 - 4 = -3", "5 + 6 = 11"]

# print(sol(result1))
