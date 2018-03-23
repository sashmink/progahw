#ВАЖНО эта программа написана с расчетом на то, что читаемый текст написан на русском языке
#и слова вроде "открыю", подходящие под шаблон, не встретятся в нем.
#если текст может состоять из рандомных сочетаний символов, то имеет смысл
#работать не с регулярными выражениями, а просто создать массив всех форм глагола. 

itog = []
import re
znaki = ['.',',',':',';','?','!','-','–','"']
b = 0

with open("gog3.txt", encoding="utf-8") as f:
     text = f.read()   
     splited_text = text.split()
     word = ''
     for word in splited_text:
         r = re.search('^откр[ыо][юлетйв][саштмоиыь]?[ьеийся]?[йяьс]?[я]?\W*?$', word)
         if r:
            string1 = r.group(0)
            last_symbol = string1[len(string1)-1]
            if last_symbol in znaki:
                string1 = string1[:-1]
            if string1 in itog:
                b += 1
            if b == 0 and string1 != 'открытие' and string1 != 'открытий'and string1 != 'открытии' and string1 != 'открытия':
                itog.append(string1)
            b = 0
print (itog)
