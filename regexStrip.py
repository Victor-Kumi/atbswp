import re

def regexStrip(string, strip):
    if not strip:                            #strip=="" is falsy
        for newstring in re.compile(r'\S.*\S').findall(string):
            print (newstring)

    elif strip:
        newstring=re.compile('[^{}]'.format(strip)).findall(string)
        #print(newstring)
        print(''.join(newstring))    


regexStrip('  If you want to lstrip and rstrip space\n Enter "" as second argument\n Else enter characters to strip as second argument.  ', '')
print('')
regexStrip('If you want to lstrip and rstrip space\n Enter "" as second argument\n Else enter characters to strip as second argument. ', 'If')
