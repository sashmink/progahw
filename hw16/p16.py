import re

def predlogi(file):
    with open(file, encoding="utf-8") as f:
        text = f.read()
        text2 = re.sub('[…!?\.*][ ]', '. ', text)
        predlogi = text2.split('. ')
        return predlogi

def slova_po_7(predlogi):
    ss7 = []
    for predlog in predlogi:
        slova = (predlog.split())
        clear = [re.sub('[,…!?\.:;—\"\()\1234567890-]', '', slovo) for slovo in slova]
        for s in clear:
            if len(s) > 7:
                ss7.append(s)
    return ss7

def zadacha(s7):
    for s in s7:
        tires = ''
        tire = 29 - len(s)
        while tire:
            tires = tires + '-'
            tire = tire - 1
        otvet = '{}{}{}'.format(s, tires, len(s))
        print(otvet)
    
def main():
    zadacha(slova_po_7(predlogi('text.txt')))

if __name__=='__main__':
    main()
