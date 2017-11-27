list = []
s = ' '
while s:
    s = input('введите слово: ');
    list.append(s)
with open("result.txt", "a", encoding = "utf-8") as f:
    for i in list:
        d = len(i)
        res = ''
        while d > 0:
            if d % 3 != 0:
                res = res + str(i[d-1])
                print(res)
            d = d - 1
    f.write(str(res))
    f.write("/n")
        
 
   

    


