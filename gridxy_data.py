tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(ls_of_ls):
    colWidths = [0] * len(ls_of_ls)
    j=0
    for ls in ls_of_ls:  
        strLen=[]
        for item in ls:
            strLen.append(len(item))
        colWidths[j]=max(strLen)+1 #could just be colWidths.append(max(strLen)+1) should we have initialized colWidths=[] 
        j += 1

    k=0
    for x in range(len(ls_of_ls[0])):
        l=0
        for y in ls_of_ls:
            print (y[k].rjust(colWidths[l]), end='')
            l += 1
            #continue
        k+=1
        print('\n', end='')


printTable(tableData)
        

    
        
    

