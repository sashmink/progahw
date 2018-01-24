import random

def op(x):
    if x == 1:
        f = open("marks.txt", encoding="utf-8")
        text = f.read()   
        splited_text = text.split()
        return splited_text
    if x == 2:
        f = open("adj.txt", encoding="utf-8")
        text = f.read()
        lines = text.splitlines()   
        return lines
    if x == 3:
        f = open("noun_sg.txt", encoding="utf-8")
    if x == 4:
        f = open("noun_pl.txt", encoding="utf-8")
    if x == 5:
        f = open("verb.txt", encoding="utf-8")
    if x == 6:
        f = open("loc.txt", encoding="utf-8")

def punctuation():
    x=1
    return random.choice(op(x))
    
def adj(slog):
x=2
    if slog == '3':
        return random.choice(op(x)[0].split())
    if slog == '2':
        return random.choice(op(x)[1].split())

def noun_sg(slog):
    x=3
    noun1sgm = ["ёж", "йог", "сон", "день", "глаз", "след", "знак", "грай", "ор", "щит", "лист", "дед", "граф"]
    noun2sgf = ["вода", "трава", "земля", "рыба", "сосна", "крыша", "птица", "кочка", "точка", "мама", "Куба", "трубка"]
    noun3sgm = ["Авраам", "Гевара", "Исаак", "капитан", "поползень", "коробок", "дворянин", "компотец", "шарабан", "караван", "Петербург", "поворот", "перевал", "воробей"]
    if slog == '3':
        return random.choice(noun3sgm)
    if slog == '2':
        return random.choice(noun2sgf)
    if slog == '1':
        return random.choice(noun1sgm)

def noun_pl():
    x=4
    noun2pl = ["костры", "звуки", "жёны", "груши", "моря", "дети", "слова", "камни", "дома", "ели", "ежи", "звери", "годы"]
    return random.choice(noun2pl)

def verb(slog):
    x=5
    verbfr5 = ["втянули", "учили", "кололи", "скурили", "забыли", "создали", "отпели", "касались", "обняли", "манили", "сушили", "остригли", "забудут", "запомнят", "заметят", "узреют", "умертвят", "раскрасят", "омоют", "осветят", "исцелят"]
    verb3 = ["поёт", "грядёт", "тонет", "растёт", "висит", "курит", "бежит", "плывёт", "воет", "внемлет", "парит", "молчит"]
    if slog == '5':
        return random.choice(verbfr5)+' тебя'
    if slog == '2':
        return random.choice(verb3)

def loc():
    x=6
    loc = ["Неве", "лесу", "носу", "весне", "тоске", "селе", "зиме", "мышах", "душе", "арбе", "веках", "пути", "слезе", "жизни"]
    return 'в ' + random.choice(loc)

def stroka1():
    a = random.choice([1,2,3])
    if a == 1:
        stroka1 = adj('3') + ' ' + noun_sg('2') + punctuation()
    if a == 2:
        stroka1 = adj('2') + ' ' + noun_sg('3') + punctuation()
    if a == 3:
        stroka1 = noun_sg('3') + ' ' + loc() + punctuation()
    return stroka1
        
def stroka2():
    a = random.choice([1,2,3])
    if a == 1:
        return noun_pl() + ' ' + verb('5') + punctuation()
    if a == 2:
        return verb('2')+ ' ' + ' ' + adj('2') + ' ' + noun_sg('3') + punctuation()
    if a == 3:
        return verb('2')+ ' ' + adj('3') + ' ' + noun_sg('2') + punctuation()
def stroka3(): 
    a = random.choice([1,2,3,4])
    if a == 1:
        return adj('2') + ' ' + noun_sg('1') + ' ' + loc() + '.'
    if a == 2:
        return loc() + ' ' + noun_sg('3') + '.'
    if a == 3:
        return adj('2') + ' ' + noun_sg('3') + '.'
    if a == 4:
        return adj('3') + ' ' + noun_sg('2') + '.'
    

print (stroka1())
print (stroka2())
print (stroka3())



