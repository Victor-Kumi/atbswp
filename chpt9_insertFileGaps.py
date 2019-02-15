import os, re, shutil

lsItems = os.listdir('../try') #txts;containing folder
print(lsItems)

regexObject = re.compile(r'00\d+')
newList = []
for item in lsItems:
    if item.endswith('.txt'):
        mo = regexObject.search(item)
        if mo:
            newList.append(int(mo.group()))
print(newList)

fileToAdd = '../try/spamfolder/spam002.txt'
sameFileName = os.path.join('../try', os.path.basename(fileToAdd))

#Code to implement depends on whether file numbering is ordered or not.
orderedNumbering = True
start = min(newList)
for i in range(len(newList)):
    orderedNumbering = orderedNumbering and os.path.exists('../try/spam00'+str(start)+'.txt')
    start += 1 

#If numbered files not ordered, 
#just rename the existing file with same basename as fileToAdd, 
#to highest numbered file.
if not orderedNumbering and os.path.exists(sameFileName): 
    shutil.move(sameFileName, os.path.join('../try', 'spam00'+str(max(newList)+1)+'.txt'))
    shutil.move(fileToAdd, '../try') 

#If ordered, then change ordering 
#by pushing one step forward each number after fileToAdd number.
elif orderedNumbering and os.path.exists(sameFileName): 
    number = max(newList)
    for i in range(max(newList)):
        filename1 = 'spam00' + str(number+1) + '.txt'
        filename2 = 'spam00' + str(number) + '.txt'
        a = os.path.join('../try',filename2)
        b = os.path.join('../try',filename1)
        if number >= int(regexObject.search(fileToAdd).group()):
            shutil.move(a,b)
            number -= 1
    shutil.move(fileToAdd, '../try')
        
            

        
