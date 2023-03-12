def dic(dic1,dic2):
     dic={}
     for i in dic1:
          dic[i]=dic1[i]
     for j in dic2.keys() :
          if dic.get(j,"non")=="non":
               dic[j]=dic2[j]
          else :
               dic[j]+=dic2[j]
     return dic           
     
print(dic({'a':10,'b':20},{'a':20,'b':30,'d':40}))