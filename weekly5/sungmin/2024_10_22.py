# #===========================================================================
# # #problem_1

def solution(k, tangerine):
    tangerine.sort()
    a = []
    b = 0             # 귤 크기 저장 
    c = 1             # 현재 귤 크기 횟수
    for i in tangerine:
        if i == b:
            c += 1
            continue
        a.append(c)
        c = 1          # 새로운 귤크기 다시 1로 초기화
        b = i          # 새로운 귤크기 i 로 저장
    a.append(c)
    del a[0]
    a.sort(reverse=True)
    
    c = 0
    b = 0
    for i in a:
        c += i
        b += 1
        if c >= k:
            return b
# #===========================================================================
# # #problem_2

# 리스트를 유지하면서 새로운 점수가 들어 올때 리스트에 추가하고 
# 다시 리스트 유지하면서 최저점 기록

# 리스트 생성
# 리스트 정렬
# 리스트 갯수까지만 저장
# 그중 제일 작은 값 뽑기 
# 나머지는 다시 
def solution(k, score):
    lst = []
    answer = []

    for i in score:
        lst.append(i)
        lst.sort(reverse=True)  # 점수 정렬
        
        if len(lst) > k:
            lst = lst[:k]
        
        answer.append(lst[-1])

    return answer

k = 3
score = [10, 100, 20, 150, 1, 100, 200]

result = solution(k, score)

print(result)

# #===========================================================================
# # #problem_3


def f(n):
    ncount = bin(n).count('1')    # n을 2진수로 변환후 1을 count함수를 통해 1을 찿는다
    num = n+1         # n 보다 큰수 
    while True:       #무한루프
        next_num = bin(num).count('1') #n 보다 큰수를 다시 2진법 변환후 1을 count함수를 통해 1을 찿는다

        if ncount == next_num:    # 처음 n의 1과 n+1의 1의 수가 동일할때
            return num            # n+1이 저장되어 있는 num 반환
        num += 1                  # num +1 씩 중가

print(f(78))
