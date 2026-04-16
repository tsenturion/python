"""
0205_bool
"""

flag1 = True
flag2 = False


"""операторы сравнения
>
<

>=
<=

==
!=
"""
a = 10
b = 3
"""
логическое выражение
"""
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

print("5 > 3", 5 > 3)
print("5 < 3", 5 < 3)
print("5 >= 3", 5 >= 3)
print("5 <= 3", 5 <= 3)
print("5 == 3", 5 == 3)
print("5 != 3", 5 != 3)

"""
False (0)
True (1)

логические операторы
and (и) (*)
or (или) (+)
not (не) (!)
"""

print(False and 5 < 4 or not True and 8 != 8 and (not 7 < 9 or a != b))
#      0 * 5 < 4 
print(True and False)
#      1 * 0
print(True or False)
#      1 + 0


print(True + True)
print(True + False)
print(False + True)
print(False + False)

print(True * True)
print(True * False)
print(False * True)
print(False * False)

x = 5
Y = 5
y = 6
print(y == Y)

print(type(5 > 3))

# bool() - функция конвертации в bool
print(bool(0))
print(bool(1))
print(bool(-1223131))

print(bool(0.0))
print(bool(1.0))
print(bool(-1223131.0))

print(bool(""))
print(bool(" "))
print(bool("test"))
print(bool("0"))
print(bool("False"))
print(bool("True"))

