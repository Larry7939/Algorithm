n = input()
for i in range(1,int('F',16)+1):
    print("%s*%X=%X"%(n,i,int(n,16)*i))