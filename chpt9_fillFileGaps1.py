import os, shutil, re

lsItems = os.listdir('../try')
print(lsItems)

regexObject = re.compile(r'00\d+')
newList = []
for item in lsItems:
    if item.endswith('.txt'):
        mo = regexObject.search(item)
        if mo:
            newList.append(int(mo.group()))
print(newList)

iterationNumber = max(newList) - len(newList)

while iterationNumber > 0:
    print(iterationNumber)
    number = min(newList)

    for i in range(max(newList)):
        filename1 = 'spam00' + str(number) + '.txt'
        filename2 = 'spam00' + str(number-1) + '.txt'
        a = os.path.join('../try',filename2)
        b = os.path.join('../try',filename1)
        if os.path.exists(b) and not os.path.exists(a):
            if number > min(newList):
                shutil.move(b,a)
  
        number += 1
    iterationNumber -= 1

 
