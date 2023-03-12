def srta(mot):
    t=[]
    m=""
    j=0
    for i in range(len(mot)):
          
          if mot[i] =="-" or i==len(mot)-1:
            m=mot[j:i]
            t.append(m)
            j=i+1
    t=sorted(t)
    
    return '-'.join(t);

print(srta("plipu-jfkghi-fgdfg"))