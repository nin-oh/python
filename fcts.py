def lon(*lis):
    min=max=lis[0]
    for value in lis:
        if len(value)<len(min):
          min=value
        elif len(value)>len(max):
          max=value
    return max,min;
max,min =lon([0],[1,2],[5,6,8])
print(f"la liste le plus longue: ({len(max)},{max})")"""