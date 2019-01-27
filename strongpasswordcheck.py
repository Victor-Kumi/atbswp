import re
import sys

regexObjects={'Must contain uppercase character':re.compile(r'[A-Z]+'), 'Must contain lower case character':re.compile(r'[a-z]+'), 'Must contain a digit':re.compile(r'\d+')}

def strongPasswordCheck(password):
    check=""
    for regexObject in regexObjects.items():
        key,value=regexObject
        if value.search(password) != None:
            continue
        else:
            check+=key+'\n'
            continue
    if check:       #Default check="" is bolean False which makes any other expression with value, True. OR check !="" .thus only True executes
        print('Check:\n',check, end='',sep='')
        return      
    if len(password)>7:
        print('Password is strong')
        sys.exit(0)
    else:
        print('Check:\nPassword must contain at least 8 characters')
        return 

while True:
    return_if_not_strong=strongPasswordCheck(input("Input password > "))
    


   
        


   
        
    
