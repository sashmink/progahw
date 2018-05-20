import os

stro = ''
tec = 0
best = 0
start_path = '.'
for root, dirs, files in os.walk(start_path):
    stro = str(root)
    for letter in stro:
        if letter == '/':
            tec += 1
    if tec >= best:
        best = tec
    tec = 0
print (best)
        
        
   
   
