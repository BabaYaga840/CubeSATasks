import numpy as np

read = open("encoded.txt","r")
write = open("reconciled_message.txt","a")
errors=0
def getHmat():
    G=np.ones((7,3),int)
    for i in range(3):
        G[i][i]=0
    for i in range(3):
        for j in range(3):
            if i!=j:
                G[j+4][i]=0
    return G
    #print(G)

a=0
H=getHmat()
M=np.zeros(7,int)
for i in range(25000):
    msg=int(read.read(7))
    for i in range(7):
        M[6-i]=int(msg%10)
        msg=msg/10


    modt=lambda t: t%2
    S=M.dot(H)
    D=M[:4]#np.array(M[i] for i in range(4))
    #print(D)
    S=np.array([modt(x) for x in S])

    if S[0]==0:
        if S[1]*S[2]:
            D[0]=1-D[0]
            errors=errors+1
    elif S[1]:

        if S[2]:
            D[3]=1-D[3]
            errors=errors+1
        else:
            D[2]=1-D[2]
            errors=errors+1
    elif S[2]:
        D[1]=1-D[1]
        errors=errors+1
    for i in range (4):
        write.write(str(D[i]))
    a=a+7
    read.seek(a)
print("bit error rate:", errors/100000)
read.close()
write.close()
