import re

#функция, которая читает файл
def lire():
    with open ('kom.txt', encoding='utf-8') as f:
        text = f.read()
    return text

#функция, которая находит и заменяет маленького комара на слона в тексте
def slonik(text):
    slonik = re.sub(r'\b(комар)([ауоые]?[вхм]?и?)\b', r'слон\2', text)
    return slonik

#функция, которая находит и заменяет маленького комара на слона в тексте
def slon(slonik):
    slon = re.sub(r'\b(Комар)([ауоые]?[вхм]?и?)\b', r'Слон\2', slonik)
    return slon

#функция, которая записывает ответ в файл
def ecrire(slon):
    with open("slon.txt", "w", encoding="utf-8") as r:
        r.write(slon)

def main():
    ecrire(slon(slonik(lire())))

if __name__ == '__main__':
    main()

        

            
