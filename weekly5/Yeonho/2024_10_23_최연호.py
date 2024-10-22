# 문제1
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):

    dic = {}  

    for i in range(len(tangerine)):
        if tangerine[i] not in dic:
            dic[tangerine[i]] = 1
        else:
            dic[tangerine[i]] += 1


    dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    count = 0
    for t in dic:
        k -= t[1]
        count += 1
        if k <= 0:
            break
    return count

# 문제2
# https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    answer= []
    top=[]


    for i in range(len(score)):
       
        if len(top) < k:
            top.append(score[i])
        else:
          
            if score[i] > min(top):
                top.remove(min(top))
                top.append(score[i])   
        
        answer.append(min(top))
    
    return answer



# 문제3
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):

    a = bin(n)
    count1 = 0
    for x in a:
        if x == '1':
            count1 += 1

    k = 0
    while True:
        k += 1
        b = bin(n + k)
        count2 = 0
        for x in b:
            if x == '1':
                count2 += 1
        
        if count1 == count2:
            break

    return n + k


print(solution(78))
