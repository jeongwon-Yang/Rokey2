# 문제 1

# https://school.programmers.co.kr/learn/courses/30/lessons/82612
# 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 
# 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요

#이용금액이 3인 놀이기구를 4번 타고 싶은 고객이 현재 가진 금액이 20이라면, 총 필요한 놀이기구의 이용 금액은 30 (= 3+6+9+12) 이 되어 10만큼 부족하므로 10을 return 합니다.



def solution(price, money, count):
    
    result = 0
    for i in range(0,count):
        result += price*(i+1)
     
    if money < result:
        total= result-money
    else:
         total = 0
    answer = total

    return answer
print(solution(5,10000,2))




# 문제2

# https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 입출력 예
#    s 	   return
# "abcde" 	"c"
# "qwer" 	"we"



s = "abcde" 

def solution(s):
    half = len(s)//2
    if len(s)%2 ==0:
        answer =s[half-1]+s[half]
        
    else:
        answer = s[half]
    
    return answer




# 문제 3 

# https://school.programmers.co.kr/learn/courses/30/lessons/12922
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# 입출력 예
# n 	return
# 3 	"수박수"
# 4 	"수박수박"




def solution(n):
    word="수박"
    if n%2==0:
        answer = (word)*(n//2)
    else:
        answer = (word)*(n//2)+("수")
    return answer

solution(1)




# 문제 4

#https://school.programmers.co.kr/learn/courses/30/lessons/68644

# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에
# 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

#입출력 예
#   numbers 	    result
# [2,1,3,4,1] 	[2,3,4,5,6,7]
# [5,0,2,7] 	[2,5,7,9,12]

def solution(numbers):
    sort_num = sorted(numbers)
    # 이걸 어떻게 뽑아내야하나.....
    print(sort_num)
    answer = []
    return answer



# 문제 5

# https://school.programmers.co.kr/learn/courses/30/lessons/42748

# 문제 설명

# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

#     array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
#     1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
#     2에서 나온 배열의 3번째 숫자는 5입니다.

# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 입출력 예
#        array 	                        commands 	                return
# [1, 5, 2, 6, 3, 7, 4] 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]] 	   [5, 6, 3]


def solution(array, commands):
    answer = []
    
    ##### 문제 이해를 못함
    return answer

array = [1, 5, 2, 6, 3, 7, 4] 
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


