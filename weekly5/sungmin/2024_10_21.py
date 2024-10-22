# #===========================================================================
# # #problem_1

# 가져가는 갯수가 적어야하니까 
# 최대한 5가 많이 들어가야한다 생각해서 
# 3을 먼저 빼고 5로 나누고 몫을 저장

def f(n):
    bags = 0            # 저장할 변수
    while n >= 0:       # 음수 
        if n % 5 == 0:      
            bags += n // 5
            return bags
        n -= 3
        bags += 1
    return -1  # 나눌 수 없는 경우

n = int(input("설탕의 무게 n을 입력하세요: "))
result = f(n)
if result != -1:
    print(result)
else:
    print(-1)

# #===========================================================================
# # #problem_2

n = int(input())

members = []

for i in range(n):
    age,name = input().split()  #공백 기준 분리
    # name = input()
    members.append((int(age), i, name))  # 나이,가입 순,이름 
    
# print(members)
members.sort() # 나이순으로 정렬
print()

for k in members:  
    print(k[0], k[2])  #나이,이름 출력

# #===========================================================================
# # #problem_3
