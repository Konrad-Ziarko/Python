x,y = input().split(",")

tab = []
for i in range (0, int(x)):
    temp = []
    for j in range (0,int(y)):
        temp.append(i*j)
    tab.append(temp)
print (tab)