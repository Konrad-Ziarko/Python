import time

number = int(input('number for computing: '))
start_time = time.time()
integrals = {}
for iter in range(1, number+1):
    integrals[iter] = iter*iter
print(time.time() - start_time)
print (integrals)
