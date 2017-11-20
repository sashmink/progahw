#мы считаем, что длина пустой строки - 0
with open ("text.txt") as f:
    num = 0
    i = 0
    for line in f:
        words = line.split()
        num = num + len(words) 
        i = i + 1
num = num / i
print(num)
