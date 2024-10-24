# problem 1
def solution(answers):
    people = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    rank = []
   
    for idx, i in enumerate(people):
        cnt = 0
        for j in range(len(answers)):
            if i[j % len(i)] == answers[j]:
                cnt += 1
        rank.append((idx + 1, cnt))
    
    rank = sorted(rank, key=lambda x: x[1], reverse=True)
    
    result = []
    for person in rank: 
        if person[1] == rank[0][1]:
            result.append(person[0])

    return result
  
# problem 2
import datetime

def solution(a, b):

    date = datetime.date(2016, a, b)

    day_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    return day_week[date.weekday()]

# problem 3
def solution(food):
    result = []

    for i in range(1, len(food)):
        cnt = food[i] // 2
        if cnt != 0:
            result.append(str(i) * cnt)
    
    result1 = result[::-1]
    answer = ''.join(result) + '0' + ''.join(result1)

    return answer
