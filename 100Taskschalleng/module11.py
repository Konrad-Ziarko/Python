numbers = input().split(",")

list = []
for number in numbers:
    if not int(number, 2)%5:
        list.append(int(number, 2))
print (list)
