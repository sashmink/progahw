def reading():
    f = open('table2.txt', encoding="utf-8")
    order = []
    for line in f:
        t = line.split('\t')
        order.append(t[3])
    f.close()
    return order

def slovar(order):
    freq = {}  
    for word in order:
       if word in freq:   
           freq[word] += 1 
       else:  
           freq[word] = 1 
    return freq

def find(freq):
    m = []
    for key in sorted(freq, key=freq.get, reverse=True):
        m.append(key)
        print(key)
    return m[0]

order = reading()
freq = slovar(order)
result = find(freq)
    
