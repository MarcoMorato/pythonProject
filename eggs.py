import random

str1 = '123456789'

str2 = 'qwertyuiopasdfghjklzxcvbnm'

str3 = str2.upper()
print(str3)
# Выведет: 'QWERTYUIOPASDFGHJKLZXCVBNM'

# Соединяем все строки в одну
str4 = str1+str2+str3
print(str4)
# Выведет: '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

# Преобразуем получившуюся строку в список
ls = list(str4)
print (ls)
# Тщательно перемешиваем список
random.shuffle(ls)
# Извлекаем из списка 12 произвольных значений
psw = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
print(psw)
# Выведет: '1t9G4YPsQ5L7'
