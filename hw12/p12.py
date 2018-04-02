import re

a = 0
with open("bruney.htm", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        crit = re.search('Столица', line)
        a += 1
        if crit:
            tsel = lines[a+1]
            result_raw = re.search('>[А-Я][А-Яа-я-]*<', tsel)
            result = result_raw.group()
            result = result[1:-1]
            break
print('ОТВЕТ', result)
with open("stolitsa.txt", "w", encoding="utf-8") as f:  
    f.write(result)
            
