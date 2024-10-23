# problem 1
def solution(n,a,b):
    count1 = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        count1 +=1

    return count1

print(solution(8,4,7))

# problem 2

def solution(quiz):
    lst = []
    for i in quiz:
        num = i.split('=')

        if '+' in num[0]:
            a, b = map(int, num[0].split(' + '))
            result = a + b
        elif '-' in num[0]:
            a, b = map(int, num[0].split(' - '))
            result = a - b

        if result == int(num[1]):
            lst.append("O")
        else:
            lst.append("X")
    
    return lst
