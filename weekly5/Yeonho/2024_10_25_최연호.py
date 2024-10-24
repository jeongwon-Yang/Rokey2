#문제1

def solution(answers):
    answer = []

    idx1,idx2,idx3 = 0,0,0
    c1,c2,c3=0,0,0
    an1=[1,2,3,4,5]
    an2=[2,1,2,3,2,4,2,5]
    an3=[3,3,1,1,2,2,4,4,5,5]

    for i in answers:
        if i == an1[idx1]:
            c1+=1  
        if i == an2[idx2]:
            c2+=1  
        if i == an3[idx3]:
            c3+=1
            
        idx1+=1
        idx2+=1
        idx3+=1 
        
        if idx1==5:
            idx1=0
        if idx2==8:
            idx2=0
        if idx3==10:
            idx3=0
            
    Max = max(c1,c2,c3)
    
    if Max == c1:
        answer.append(1)
    if Max == c2:
        answer.append(2)
    if Max == c3:
        answer.append(3)
    
    return answer


#문제2

def solution(a, b):
    answer = ''
    #  순서는 금-토-틸-월-화-수-목 순으로 가야한다.
    #  1월, 3월, 5월, 7월, 8월, 10월, 12월은 31일까지 있고, 4월, 6월, 9월, 11월은 30일까지
    #  2월은 평년에서는 28일, 윤년에서는 29일
    # 366일 전부 구해서 5월 24일이 365일 중에 며칠이 지났는지 따지는게 핵심인듯

    lst = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = []
    idx = 0
    for i in range(366):
        day.append(lst[idx])
        idx +=1
        if idx==7:
            idx=0

    # 여기서 포인트는 2월이 포함될 경우 
    total = 0
    if a<=7:
        for i in range(1,a):
            if i % 2==0:
                if i ==2:
                    total += 29
                else:
                    total += 30
            else:
                total += 31
        total += b
    else:
        for i in range(8,a):
            if i % 2==0:
                total += 31
            else:
                total += 30
        total += (213+b)

    answer= day[total -1]  

    return answer




#문제3

def solution(food):
    answer = ""
    count=1
    for i in food[1:]:
        a=i//2
        if a == 0:
            count+=1
            continue           
        else:
            answer=answer+(str(count)*a)
            count+=1
    
    answer=answer+"0"+answer[::-1]     
    return answer