def Extended(a, b): 
    # Base Case 
    if a == 0 :  
        return b,0,1
             
    gcd,x1,y1 = Extended(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y


def gcd(a,b):
    gcd_matrix=Extended(a,b)
    return gcd_matrix[0]

def inverse(x,y):
    res = pow(x, -1, y)
    return res

