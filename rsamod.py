import math
import random

def inverse(x,y):
    d=pow(x,-1,y)
    return d
    
        
           


def geeratee():
    res=[]
    for e in range(99999):
        if(math.gcd((3466*1008),e)==1):
            res.append(e)
            
        else:
            continue
    i=random.randint(0,len(res))
    return res[i]
 



def encryption(msg):
    p=3467
    q=1009
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
    #print(d)
    plaintxt=(pow(int(cipher),d))%n
    return plaintxt

#print("decrypt=",decryption(863993,3415624))