# problem 1
def solution(k, tangerine):
    dic1 = {}
    for i in tangerine:
        if i not in dic1:
            dic1[i] = 1
        elif i in dic1:
            dic1[i] += 1
    
    
    list_dic1 = sorted(dic1.items(), key = lambda x:x[1],reverse=True)
    
    sum = 0
    result = 0
    for j in list_dic1:
        sum += j[1]
        result += 1
        if sum == k:
            return result
    else:
        return 1
      
# problem 2
def solution(k, score):
    lst = []
    result = []
    for i in score:
        lst.append(i)
        lst = sorted(lst, reverse = True)
        result.append(lst[0:k][-1])
    return result

# problem 3

def solution(n):
    bin_num = bin(n)[2:]

    while True:
        n +=1
        next_num = bin(n)[2:]

        if one_count_fuc(bin_num) == one_count_fuc(next_num):
            return n
        
def one_count_fuc(bin_num):
    return bin_num.count('1')
