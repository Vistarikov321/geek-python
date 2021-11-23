# password = input("Введите пароль >>> ")
#
# original_password = "correct"
#
# if original_password == password:
#     print("Верно")
# else:
#     print("Неверно")
#

age = input("Введите ваш возраст >>> ")

age = int(input("Введите ваш возраст >>> "))

if age >= 14:
    print("Можете получить паспорт")
    if 20 <= age < 45:
        print("Можете получить паспорт")
elif age < 1:
    print("custom")
else:
    print("Паспорт получить нельзя!")
