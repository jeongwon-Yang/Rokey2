# #===========================================================================
# # #problem_1

# 점화식 f(n-1)+f(n-2)
# def solution(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2

#     a = 1
#     b = 2
#     for i in range(3, n + 1):

#         a, b = b, (a + b) % 1234567
#     return b

# print(solution(5))

# # #===========================================================================
# # # #problem_2



# # #===========================================================================
# # # #problem_3

# # 점화식 f(n-1)+f(n-2)
# def solution(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     a = 0
#     b = 1
#     for i in range(2, n + 1):

#         a, b = b, (a + b) % 1234567
#     return b

# print(solution(5))
