num = 0
with open ("C:/Users/student/Desktop/kr/Extinct_languages.tsv", encoding="utf-8") as f:
    for line in f:
        a = line.split('\t')
        for i in a:
            if i=="Critically endangered\n":
                num = num + 1
print(num)
