number = int(input('number for which factorial will be computed: '))

import time
start_time = time.time()
def factorialRecursion(base_Number):
    if base_Number <= 1:
        print(time.time() - start_time)
        return 1
    else:
        return factorialRecursion(base_Number-1)*base_Number
print (factorialRecursion(number))

start_time2 = time.time()
result = 1;
for iter in range (2, number+1):
    result *= iter
print(time.time() - start_time2)
print (result)