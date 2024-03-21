i=0
aa = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
while i < 26:
    list = [str(i) for i in input().split()]
    
    a1 = aa[i]
    with open(a1, 'w') as file:
        for i in list:
            file.write("%s\n" % i)
    print(f"List has been written to '{a1}'")
    i+=1
