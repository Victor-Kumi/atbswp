import os,shutil
#Copy all .txt files in a folder path to another folder
print('Copying all txt files in hello folder tree to /home/victor/try')
for folderpath,subfolders,filenames in os.walk('/home/victor/hello'):
    #print('Copying txt files in:',folderpath,'....')

    for filename in filenames:
        if filename.endswith('.txt'):
            print('Copying', filename, 'in:',folderpath,'....')
            shutil.copy(os.path.join(folderpath,filename), '../try')

print('Done')
