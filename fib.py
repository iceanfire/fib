# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


def Fib(num):
    if(num<=2):
        return 1
    else:
        fNum = 1
        sNum = 1
        x = 3
        while(x<=num):
            tNum = fNum + sNum
            fNum = sNum
            sNum = tNum
            x=x+1
        return sNum

def FibR(num,x=3,fNum=1,sNum=1):
    if(num<=2):
        return 1
    else:
        tNum = fNum + sNum
        fNum = sNum
        sNum = tNum
        x = x+1
        if(x<=num):
            return FibR(num,x,fNum,sNum)
        else:
            return sNum

def FibNew(n):
    if(n==1):
        return 1 
    elif(n==2):
        return 1
    else:
        return FibNew(n-1)+FibNew(n-2)    

 
def Fiby(num):
    a,b=0,1
    for i in range(num):
        a,b = b,a+b
    return a

 
