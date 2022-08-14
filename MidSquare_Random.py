seed = 7182

def random():
    global seed
    s = str(seed * seed)

    while len(s) != 8:
        s = "0" + s 

    seed = int(s[2:6])

    return seed

list = []
for i in range(20):
    #print (random())
    list.append(random())

dup = {x for x in list if list.count(x)>1}
print(list)
print(len(dup))