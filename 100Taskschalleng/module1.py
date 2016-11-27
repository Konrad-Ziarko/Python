import time
start_time = time.time()
numbers = []
iter = 2000
while iter <= 3200:
    if iter % 7 != 0:
        iter=iter+1
    elif iter % 7 == 0:
        if iter %5 != 0:
            numbers.append(iter)
            iter+=7
        else:
            iter+=7
print(time.time() - start_time)
print (numbers)
