# 문제 1
def solution(n):
    a= "1"
    b = "2"
    if n == 1:
        answer = 1
    elif n == 2:
        answer =2
    else:
        for i in range(3 , n):
            for j in range(i , n-i):
                pass
    
    return answer


# 문제 2
def solution(num):

    count = 0

    for i in range(1,num+1):
        sum = 0
        for j in range(i, num+1):
            sum += j

            if sum == num:
                count += 1

            if sum > num :
                break

    return count


# 문제 3
def solution(num):
    a = 0
    b = 1
    i = 0

    while i < num-1 :
        result = (a + b) % 1234567
        a = b
        b = result
        i = i+1    
    return(result)
