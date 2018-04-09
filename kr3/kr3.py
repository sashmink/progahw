import re

#функция, которая записывает ответ в текстовый файл
def res(result):
    with open("result.txt", "w", encoding="utf-8") as r:
        r.write(str(result))
    
amount = 0
with open ('isl.xml', encoding='utf-8') as f:
    for line in f:
        poisk = re.search('\</teiHeader\>', line)
        if poisk:
            break
        amount += 1
print (amount)
res(amount)


