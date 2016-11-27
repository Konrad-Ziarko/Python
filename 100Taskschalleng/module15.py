heads, legs = input("How many heads and legs we count ").split(" ")

tmpHeads = int(heads)
tmpLegs = int(legs)

chickens = rabbits = 0
while tmpHeads*2 < tmpLegs:
    rabbits+=1
    tmpHeads-=1
    tmpLegs-=4
chickens = tmpHeads

print ("Rabbits: %d\nChickens: %d" % (rabbits, chickens))