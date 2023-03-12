def fon(liste):
    v=[]
    for value in liste :
        if value%2==0 :
            v.append(value);
    return v;
print(fon([1,5,6,7]))