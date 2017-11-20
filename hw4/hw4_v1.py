with open ("/Users/Sasa/progahw/text.txt") as f:
    for line in f:
        words = line.split()
        num = num + len(words) 
        i = i + 1
num = num / i
print(num)
