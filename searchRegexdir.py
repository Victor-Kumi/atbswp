import re, os, sys

#Accepts directory path as terminal argument.
regexToken = input('Enter tokens to match:\n')
for item in os.listdir(sys.argv[1]):
    if re.compile(r'.txt$').search(item): #same as 'if re.compile(r'.txt').search(item) != None:'
        with open(item) as txtfile:
            matchObject=re.compile(regexToken).findall(txtfile.read())
            print('List contains result after matching regex tokens',regexToken,'in',item)
            print(matchObject)
            print('')
            

        


