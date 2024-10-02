#====================================================================================================    
# Example 1

"""
15주차 과제
문제 15) 함수 divide(x, y) 함수를 구현한 후 연산 0으로 나누는 것에 대한 예외 처리를 수행하도록 하시오.
    - 구문은 try, except, else 블록 구현
    - 다음 두 호출에 대한 결과

divide(3.2, 2) -> 1.6
divide(5.4, 0) -> 0으로는 나눌 수 없습니다.
"""
# 사용하는 Source 예제
def solution1(x, y):

    try:
        answer = x / y
    except ZeroDivisionError:
        return "0으로는 나눌 수 없습니다."
    else:
        return answer
    
#print(solution1(4,2))


#==================================================================================================== 
# Example 2

"""
10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.

1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
 """

def solution2():
    answer=0
    set1=set()
    for i in range (1,1001):
        if i % 3 ==0:
            set1.add(i)
        if i % 5 ==0:
            set1.add(i)

    for i in set1:
        answer+=i
    return answer

#print(solution2())
    
 
 #                                                                                                                    출처:https://codingdojang.com/scode/350?langby=python#answer-filter-area
 #==================================================================================================== 
 #Example 3
"""
 문자열 형식으로 입력 받은 모스코드(dot: . dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.
 글자와 글자 사이는 공백 하나, 단어와 단어 사이는 공백 두개로 구분한다.
 
    예를 들어 다음 모스부호는 "he sleeps early"로 해석해야 한다.
         -->  .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
 """

dic={'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
       '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
       '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
       '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
       '-.--':'y','--..':'z','':' '}
 
def solution3(s):  
    answer = s.split("  ")  
    result = "" 
    for i in answer:
        answer2=i.split(" ")
        for j in answer2:
            if j in dic:
                result += dic.get(j)  
    print(result) 

#solution3(".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--")
 #                                                                                                                     출처: https://codingdojang.com/scode/469?answer_mode=hide
  #==================================================================================================== 
 