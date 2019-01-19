def list_str(ls):
    if len(ls)>0:
        a=str(ls[0])+', '
        i=0
        for j in range(len(ls)-2): #this ensures that two items are left for ist and last cases.
            i+=1
            a=a+str(ls[i])+', '
        if len(ls)==1:
            return str(ls[0])
        elif len(ls)>1:
            return a+'and '+str(ls[-1])
    else:
        return 'Your list is empty'
    
#An example
#Change list value to test for various lengths of list.
print ('\'',list_str([1,2,6 ]),'\'')

