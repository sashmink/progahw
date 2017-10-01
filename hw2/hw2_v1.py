slovo = input ('Введите слово: ')
a = 0
for a in range (0, len(slovo)):
    if (a+1) % 2 == 0:
        if slovo[a] != "а" and slovo[a] != "к":
            print (slovo[a])
    a += 1

