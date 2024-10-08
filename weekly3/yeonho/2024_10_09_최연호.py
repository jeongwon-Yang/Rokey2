#  2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천



#     아이디의 길이는 3자 이상 15자 이하여야 합니다.
#     아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
#     단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
#===========================================================================================================================================================
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
#===========================================================================================================================================================

# 예를 들어, new_id 값이 "...!@BaT#*..y.abcdefghijklm" 라면, 위 7단계를 거치고 나면 new_id는 아래와 같이 변경됩니다.

# 1단계 대문자 'B'와 'T'가 소문자 'b'와 't'로 바뀌었습니다.
# "...!@BaT#*..y.abcdefghijklm" → "...!@bat#*..y.abcdefghijklm"

# 2단계 '!', '@', '#', '*' 문자가 제거되었습니다.
# "...!@bat#*..y.abcdefghijklm" → "...bat..y.abcdefghijklm"

# 3단계 '...'와 '..' 가 '.'로 바뀌었습니다.
# "...bat..y.abcdefghijklm" → ".bat.y.abcdefghijklm"

# 4단계 아이디의 처음에 위치한 '.'가 제거되었습니다.
# ".bat.y.abcdefghijklm" → "bat.y.abcdefghijklm"

# 5단계 아이디가 빈 문자열이 아니므로 변화가 없습니다.
# "bat.y.abcdefghijklm" → "bat.y.abcdefghijklm"

# 6단계 아이디의 길이가 16자 이상이므로, 처음 15자를 제외한 나머지 문자들이 제거되었습니다.
# "bat.y.abcdefghijklm" → "bat.y.abcdefghi"

# 7단계 아이디의 길이가 2자 이하가 아니므로 변화가 없습니다.
# "bat.y.abcdefghi" → "bat.y.abcdefghi"

# 따라서 신규 유저가 입력한 new_id가 "...!@BaT#*..y.abcdefghijklm"일 때, 네오의 프로그램이 추천하는 새로운 아이디는 "bat.y.abcdefghi" 입니다.

def solution(new_id):
    answer = ''
    # 1단계
    new_id=new_id.lower() 

    # 2단계
    twostep=['-','_','.']
    new_idlist=list(new_id)
    answer=[]
    for i in new_idlist:
        if i.isalpha() or i.isdigit() or i in twostep:
            answer.append(i)
    answer = ''.join(answer)
    
    #3단계
    while ".." in answer:
        answer=answer.replace("..",".")
        
    
    #4단계

    if answer and answer[0] == ".":
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]
        
    answer = ''.join(answer)
    
    #5단계
    answer=list(answer)
    if len(answer)==0:
        answer.append('a')
    
    #6단계
    if len(answer)>=16:
        answer=answer[0:15]
        
    if answer[-1]==".":
        answer=answer[0:14]
        
    answer = ''.join(answer)   
    
    #7단계
    if len(answer)<=2:
        a=answer[-1]
        while len(answer)<3:
            answer=answer+a
            
    
     
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
# print(solution(new_id))




#===========================================================================================================================================================

# 2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어


# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

#     1478 → "one4seveneight"
#     234567 → "23four5six7"
#     10203 → "1zerotwozero3"

# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
# s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.
# 숫자 	영단어
# 0 	zero
# 1 	one
# 2 	two
# 3 	three
# 4 	four
# 5 	five
# 6 	six
# 7 	seven
# 8 	eight
# 9 	nine


# 입출력 예
# 입력 	                출력
# "one4seveneight" 	    1478
# "23four5six7" 	    234567
# "2three45sixseven" 	234567
# "123" 	            123


def solution(s):
    answer = 0
    dic={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    result=[]
    alpha=""
    for i in s:
        if i.isdigit():
            result.append(i)
        else:
            alpha+=i
            if alpha in dic:
                result.append(str(dic[alpha]))
                alpha=""   
    answer="".join(result)
    answer=int(answer)
    return answer

s="one4seveneight"
# print(solution(s))



