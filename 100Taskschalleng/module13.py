line = str(input())

digits = 0
letters = 0
"""only Ascii"""
for idx in range(0, len(line)):
    if ((line[idx] >= 'a' and line[idx] <= 'z')or(line[idx] >= 'A' and line[idx] <= 'Z')):
        letters+=1
    elif (line[idx] >= '0' and line[idx] <= '9'):
        digits+=1

print("letters: " + str(letters) + "\ndigits: " + str(digits))