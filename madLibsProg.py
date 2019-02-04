import re,sys

regexObjects = {'Enter an adjective:\n':re.compile('ADJECTIVE'), 'Enter a noun\n':re.compile('NOUN'), 'Enter a verb:\n':re.compile('VERB'),
                'Enter an adverb:\n':re.compile('ADVERB')}

#Accepts two command line arguments.
#First for source file path and second for destination file path.

def madLibsProg():
    sourceFilePath = sys.argv[1]
    destinationFilePath = sys.argv[2]
    with open(sourceFilePath, 'w+') as sf:
        with open(destinationFilePath, 'w+') as df:
            sf.write('The ADJECTIVE panda walked to the NOUN and then VERB.\nA nearby NOUN was unaffected by these events.')#Pyperclip
            sf.seek(0)
            sf_lines = sf.readlines() #returns list
            for line in sf_lines:
                txtToAppend = line
                for keyRegexObject in regexObjects.items():
                    key,regexObject = keyRegexObject
                    if regexObject.search(txtToAppend) != None:
                        txtToAppend = regexObject.sub(input(key), txtToAppend)
                df.write(txtToAppend)
            df.seek(0)
            for line in df:
                print(line, end='')
            print('')


madLibsProg()
                        
                    
                
               
    

