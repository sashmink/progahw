def read_file():
#читает файл, название которого вводит пользователь,
#возвращает массив из слов этого файла без знаков препинания
    f = open(input('введите имя файла: '), encoding="utf-8")
    words = []
    for line in f:
        line = line.replace(', ', ' ')
        line = line.replace('; ', ' ')
        line = line.replace(': ', ' ')
        line = line.replace('. ', ' ')
        line = line.replace(', ', ' ')
        line = line.replace('! ', ' ')
        line = line.replace('? ', ' ')
        line = line.replace('- ', ' ')
        line = line.replace(' -', ' ')
        line = line.replace(' — ', ' ')
        line = line.replace(' - ', ' ')
        line = line.replace(' "', ' ')
        line = line.replace('" ', ' ')                           
        p = line.split() 
        words = words + p   
    f.close()
    return words
def freq_dictionary(words):
#составляет словарь количества словооупотреблений
    freq = {}  
    for word in words:
        if word in freq:   
              freq[word] += 1 
        else:  
            freq[word] = 1 
    return freq

def find_ing(freq):
#считает количество форм на -ing
    summ = 0
    for key, value in freq.items():
        if key[len(key)-1] == 'g' and key[len(key)-2] == 'n' and key[len(key)-3] == 'i':
            summ = summ + value
    return summ

def find_form(freq):
#узнаёт, сколько раз встречается заданная пользователем форма
    a = 0
    slovo = input('введите слово на -ing: ')
    for key, value in freq.items():
        if key == slovo:
            a = value
            break
    return a

words = read_file()
freq = freq_dictionary(words)
ing = find_ing(freq)
print("всего форм на -ing: " + str(ing))
result = find_form(freq)
print ("вот сколько раз встречается ваше слово: " + str(result))


