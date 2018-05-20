import os

stro = ''
tec = 0
best = 0
start_path = '.'
for root, dirs, files in os.walk(start_path):
    print (root)
    print(len(dirs))
    print(dirs)
    stro = str(root)
    for letter in stro:
        if letter == '/':
            tec += 1
            print (tec)
    if tec >= best:
        best = tec
        print ('BEST ' + str(best))
    tec = 0
print (best)
        
        
   
   
