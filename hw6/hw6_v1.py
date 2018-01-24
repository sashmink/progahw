#слишком поздно увидела требование про отдельные файлы со словами. дописать не успеваю. в файле "hw6_v1_3.py" лежит прототип итоговой программы, 
#где я успела написать нужную функцию лишь для знаков препинания. остальные делаются по аналогии, я загружу правильный вариант в отедльную 
#папку на всякий случай. 

import random

def punctuation():
    marks = [".", ",", "!",",",",",",",","]
    return random.choice(marks)
    
def adj(slog):
    adj3sgf = ["жидкая", "мёрзлая", "старая", "тихая", "скучная", "круглая", "дальняя", "вечная", "летняя", "китовая"]
    adj2sgm = ["первый", "ветхий", "Ноев", "мёртвый", "пьяный", "тленный", "лётный", "беглый", "мягкий", "добрый", "сонный", "светлый", "седой", "давний", "дикий", "красный"]
    if slog == '3':
        return random.choice(adj3sgf)
    if slog == '2':
        return random.choice(adj2sgm)

def noun_sg(slog):
    noun1sgm = ["ёж", "йог", "сон", "день", "глаз", "след", "знак", "грай", "ор", "щит", "лист", "дед", "граф"]
    noun2sgf = ["вода", "трава", "земля", "рыба", "сосна", "крыша", "птица", "кочка", "точка", "мама", "Куба", "трубка"]
    noun3sgm = ["Авраам", "Гевара", "Исаак", "капитан", "поползень", "коробок", "дворянин", "компотец", "шарабан", "караван", "Петербург"]
    if slog == '3':
        return random.choice(noun3sgm)
    if slog == '2':
        return random.choice(noun2sgf)
    if slog == '1':
        return random.choice(noun1sgm)

def noun_pl():
    noun2pl = ["костры", "звуки", "жёны", "груши", "моря", "дети", "слова", "камни", "дома", "ели", "ежи", "звери", "годы"]
    return random.choice(noun2pl)

def verb(slog):
    verbfr5 = ["втянули", "учили", "кололи", "скурили", "забыли", "создали", "отпели", "касались", "обняли", "манили", "сушили", "остригли", "забудут", "запомнят", "заметят", "узреют", "умертвят", "раскрасят", "омоют", "осветят", "исцелят"]
    verb3 = ["поёт", "грядёт", "тонет", "растёт", "висит", "курит", "бежит", "плывёт", "воет", "внемлет", "парит", "молчит"]
    if slog == '5':
        return random.choice(verbfr5)+' тебя'
    if slog == '2':
        return random.choice(verb3)

def loc():
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



