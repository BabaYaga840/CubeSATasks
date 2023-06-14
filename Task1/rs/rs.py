import numpy as np

#read = open("file.txt","r")
#write = open("write.txt","a")

#a=0

class func:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def calc(self,v):
        return self.a*v**3+self.b*v**2+self.c*v+self.d

    def print(self):
        print(self.a,"*x^3 + ",self.b,"*x^2 + ",self.c,"*x + ",self.d)

def li(n):
    a=n[0]*(-1/6)+n[1]*(1/2)+n[2]*(-1/2)+n[3]*(1/6)
    b=n[0]*(1)+n[1]*(-5/2)+n[2]*(2)+n[3]*(-1/2)
    c=n[0]*(-11/6)+n[1]*(3)+n[2]*(-3/2)+n[3]*(1/3)
    d=n[0]
    return func(a,b,c,d)

"""for i in range(25000):
    n=[]
    for j in range(4):
        msg=int(read.read(4))
        n.append(int(msg/1000*8+(msg/100)%10*4+(msg/10)%10*2+msg%10))
        a = a + 4
        read.seek(a)
        fx=li(n)

    modt=lambda t: t%2
    C=M.dot(G)

    C=np.array([modt(x) for x in C])
    for i in range (7):
        write.write(str(C[i]))


read.close()
write.close()"""

n=[13,4,15,7]
fx=li(n)
for i in range(6):
    print(int(round(fx.calc(i)))%16,fx.calc(i)%16)
fx.print()

