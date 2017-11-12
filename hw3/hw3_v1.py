stroka = input('введите строку: ')
print(stroka)
stroka = list(stroka)
for num, element in enumerate(stroka):
    stroka = stroka[:-1]
    itog = ''.join(stroka)
    print(itog)
