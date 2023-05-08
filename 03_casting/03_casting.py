# 공백
var = ''
print(var)
print(type(var))

var = bool(var)
print(var)
print(type(var))

var = ' '
print(var)
print(type(var))

var = bool(var)
print(var)
print(type(var))

# 문자 > 논리 > 연산
var1 = 'True'    # True
var2 = 'False'   # True

print(var1)
print(var2)
print(type(var1))
print(type(var2))

var1 = bool(var1)
var2 = bool(var2)
print(var1 + var2)

