import numpy as np

read = open("file.txt","r")
write = open("write.txt","a")

a=0

def getgenmat():
    G=np.zeros((4,7),int)
    for i in range(4):
        G[i][i]=1
    for i in range(4):
        for j in range(3):
            if i!=j:
                G[i][j+4]=1
    return G
    #print(G)


G=getgenmat()

for i in range(25000):
    msg=int(read.read(4))
    M=np.array([int(msg/1000),int((msg/100))%10,int((msg/10))%10,int(msg%10)])

    modt=lambda t: t%2
    C=M.dot(G)

    C=np.array([modt(x) for x in C])
    for i in range (7):
        write.write(str(C[i]))
    a=a+4
    read.seek(a)

read.close()
write.close()
