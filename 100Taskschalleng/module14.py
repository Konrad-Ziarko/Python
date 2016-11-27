line = str(input())

up = 0
low = 0
for idx in range(0, len(line)):
    if (line[idx].islower()):
        low+=1
    elif (line[idx].isupper()):
        up+=1

print("lowwer: " + str(low) + "\nupper: " + str(up))
