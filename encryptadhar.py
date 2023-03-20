import math
import random

def inverse(x,y):
    res = pow(x, -1, y)
    return res



def geeratee():
    res=[]
    for e in range(9999):
        if(math.gcd((3465*1008),e)==1):
            res.append(e)
            
        else:
            continue
    i=random.randint(0,len(res))
    return res[i]
geeratee()


def encryption(msg):
    p=14771
    q=54163
    n=p*q
    phin=(p-1)*(q-1)
    print(phin)
    e=geeratee()
    cipher=(pow(int(msg),e))%n
    result=str(e)+"-"+str(cipher)
    return result

#c=(encryption(88))
#print(c)

def decryption(e,cipher):
    n=3467*1009
    phin=(3466*1008)
    d=inverse(int(e),phin)
    plaintxt=(pow(int(cipher),d))%n
    return plaintxt

#print("decrypt=",decryption("631-23050"))