import random

def read_file():
    d = {}
    with open(input('введите имя файла: '), encoding="utf-8") as f:
        for line in f:
            wo, p = line.split(';', maxsplit=1)
            word_dict = d.setdefault(wo, p)       
    return d

def random_word_choice(words):
    keys = list(words.keys())
    word = random.choice(keys)
    return word

def random_podskazka_choice(words, word):
    a = words[word]
    podskazki = a.split(';')
    podskazka = random.choice(podskazki)
    return podskazka


words = (read_file())
print (words)
word = random_word_choice(words)
print (word)
podskazka = random_podskazka_choice(words, word)
print (podskazka)
print ('Я загадал слово.')
print ('Подсказка: ' + podskazka + ' ...')
a = len(word)
while a:
    b = input('Поробуйте угадать: ')
    if b == word:
        print ('Поздравляю, вы угадали!')
        break
    if a != 1:
        print ('Неправильно.')
    if a == 1:
        print ('К сожалению, попытки закончились.')
    a = a - 1
   

    
