# 반복문 03

# # 실습1
# for i in range(1, 6):
#     for j in range(i):
#         print('*', end='')
#     print()

# # 실습2
# for i1 in range(1, 6):
#     for i2 in range(6 - i1 -1):
#         print(' ', end='')
#     for i3 in range(i1):
#         print('*', end='')
#     print()

# # 실습3
# for i in range(5, 0, -1):
#     for j in range(i):
#         print('*', end='')
#     print()

# # 실습4
# for i1 in range(5, 0, -1):
#     for i2 in range(5 - i1):
#         print(' ', end='')
#     for i3 in range(i1):
#         print('*', end='')
#     print()

# # 실습5
# for i in range(1, 10):
#     if i < 5:
#         for j in range(i):
#             print('*', end='')
#     else:
#         for j in range(10-i):
#             print('*', end='')
#     print()

# # 실습6
# for i in range(1, 6):
#     for j in range(1, 6):
#         if j == i:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# 실습7
for i in range(5, 0, -1):
    for j in range(5 - i):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
