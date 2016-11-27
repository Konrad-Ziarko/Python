numbers = []
numbers2 = []
import time
start_time = time.time()
for number in range (1000, 3001):
    tmp = number
    while tmp > 0:
        if not tmp%2:
            tmp = int (tmp / 10)
        else:
            tmp = -1
    if tmp != -1:
        numbers.append(number)
print(time.time() - start_time)
start_time2 = time.time()
for number in range (1000, 3001):
    string = str(number)
    for idx in range(0, 4):
        if not int(string[idx])%2:
            if idx==3:
                numbers2.append(number)
            pass
        else:
            break
print(time.time() - start_time2)
print (numbers)
print (numbers2)