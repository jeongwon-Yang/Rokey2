# problem 1
def solution(n):
    lst= []
    count1 = 0
    for i in range(n):
        lst.append(1)
        count1 += 1

    while lst.count(1) >= 2 :
        lst.remove(1)
        lst.remove(1)
        lst.append(2)
       
    if 1 not in lst:
        count1 += 1
    
    return count1

# problem 2
def solution(n):
    end_n = 1
    result = 0
    while end_n != n:
        sum_n = 0
        for i in range(end_n,n):
            sum_n += i
            
            if sum_n == n:
                result +=1
                break
            
            elif sum_n > n:
                break
                
        end_n +=1

    
    
    return result+1

# problem 3

def solution(n):
    a, b = 0, 1
    while n >= 2:
        a, b = b, (a+b)
        n -= 1

        print(a,b)
    
    return b % 1234567

print(solution(5))
