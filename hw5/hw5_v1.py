list = []
s = ' '
while s:
    s = input('введите слово: ')
    list.append(s)
with open("result.txt", "w", encoding = "utf-8") as f:
    for i in list:
        res = ''
        d = len(i)
        while d > 0:
            if d % 3 != 0:
                res = res + str(i[d-1])
            d = d - 1
        print(res)
        f.write(res + '\n')
        
 
   

    


