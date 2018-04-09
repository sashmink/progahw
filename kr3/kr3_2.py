#я не успела доделать вторую задачу, поэтому эта программа выводит набор строк, содержащих нужные нам морфологические сведения

import re

#читает файл в набор строк (работает)
def lire():
    with open ('isl.xml', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

#ищет строки с "<w lemma=" (работает)
def second(lines):
    neob_str = []
    for line in lines:
        poisk = re.search(r'lemma=', line)
        if poisk:
            neob_str.append(line)
            poisk = ''
    return neob_str

#ищет морфологию и создает словарь (вот здесь есть проблема, которую я не успела найти)
#def morf(neob_str):
#    morf = {}
#    for st in neob_str:
#        poisk = re.search(r'type="([a-z])*"', st)
#        result = poisk.group()
#        print(result)
#    return morf

#записывает пары ключ-значения построчно в файл (работает)
def ecrire(morf):
    with open("result.txt", "a", encoding="utf-8") as r:
        for key, value in morf.items():
            r.write(key, value)

def main():
    a = second(lire())
    print (a)

if __name__ == '__main__':
    main()
        
