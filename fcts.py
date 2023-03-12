def somli(liste1,liste2):
    li=[]
    if   len(liste1) >= len(liste2) :
        for i in range(len(liste1)):
            if i<len(liste2):
               li.append(liste1[i]+liste2[i])
            else : li.append(liste1[i])
    else  :
        for i in range(len(liste2)):
            if i<len(liste1):
               li.append(liste1[i]+liste2[i])
            else : li.append(liste2[i])
    return li;
print(somli([1,2,3],[1,2,3]))