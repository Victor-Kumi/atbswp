import os

for folderPath,subfolders,filenames in os.walk('/home/victor/hello'):
    totalFileSize = 0
    for filename in filenames:
        totalFileSize = os.path.getsize(os.path.join(folderPath,filename)) + totalFileSize
    if totalFileSize > 1000:
        print(folderPath)
        print('File size in byte',totalFileSize)
        
