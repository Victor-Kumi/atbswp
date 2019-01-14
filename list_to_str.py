def list_str(ls):
    a=str(ls[0])+', '
    i=0
    for j in range(len(ls)-2):
        i+=1
        a=a+str(ls[i])+', '
    if len(ls)==1:
        return str(ls[0])
    else:
        return a+'and '+str(ls[-1])

print ('\'',list_str([1,2,6 ]),'\'')

