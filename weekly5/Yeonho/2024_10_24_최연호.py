# 문제 1
def solution(n,a,b):
    answer = 1
   
    a, b = max(a, b), min(a, b)
    
    
    while  a - b != 1:
        if a % 2 == 0:
            a = a//2
        else:
            a = a//2 + 1

        if b % 2 == 0:
            b = b//2
        else:
            b = b//2 + 1
        answer += 1
    return answer

print(solution(8,2,4))

# 문제2
def solution(quiz):
    answer = []
    for string in quiz:

        st_lst = string.split(" = ")
        

        if ' + ' in st_lst[0]:
            num = st_lst[0].split(" + ")
            if int(num[0]) + int(num[1]) == int(st_lst[1]):
                answer.append("O")
            else:
                answer.append("X")
        elif ' - ' in st_lst[0]:
            num = st_lst[0].split(" - ")
            if int(num[0]) - int(num[1]) == int(st_lst[1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer
