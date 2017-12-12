list = []
s = ' '
while s:
    s = input('введите название языка: ')
    list.append(s)

for name in list:
    with open ("C:/Users/student/Desktop/kr/Extinct_languages.tsv", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip('\n')
            a = line.split('\t')
            if a[0] == name:
                print(a[0]+'-'+a[1]+'-'+a[2])
                break
        print ('takogo yazika net v spiske')
        break
        
