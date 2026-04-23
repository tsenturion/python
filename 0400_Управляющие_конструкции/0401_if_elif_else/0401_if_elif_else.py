"""
0401_if_elif_else
"""

flag1 = True
flag2 = False

# age = int(input("Введите ваш возраст: "))

# if age < 18:
#     print("несовершеннолетний")
# else:
#     print("совершеннолетний")

mark = int(input("Введите число: "))

if mark < 0:
    print("Ошибка: оценка не может быть отрицательной")
    
elif mark > 100:
    print("Ошибка: оценка не может быть больше 100")

elif mark >= 90 and mark <= 100:
    print("Отлично")

elif mark >= 75 and mark <= 89:
    print("Хорошо")

elif mark >= 60 and mark <= 74:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")