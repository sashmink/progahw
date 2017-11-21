
# ототкрыть на запись - w (содержимое будет УНИЧТОЖЕНО,
# если не было, то будет создан), 
# ототкрыть на (ЧТО-ТО) можно дописывать в конец файла - a
# функция write понимает ТОЛЬКО СТРОКУ F.WRITE(SMTH)
# int, float ---> str()
# для списков: join()
# \n \f \r \n
# f.write(strng1 + '\n' +strng2 + '\n')
# CSV - формат записи таблиц, границы - запятые; TSV - границы - табуляции.

num = 0
with open("text1.txt", 'r', encoding="utf-8") as f:
    c = open("result1.txt", 'w', encoding="utf-8")
    for line in f:
        words = line.split()
        i = 0
        z = 0
        znaki = ',,.:;?!-——"'
        while i < len(words):
            t = words[i]
            while z < len(znaki):
                t = t.replace(znaki[z], '')
                z = z + 1
            words[i] = t
            i = i + 1
        if words[0] != '':
            result = words[0]
        else:
            result = words[1]
        c.write(str(len(words)) + '\t' + result + '\n')
        print(words)
    c.close()

    
