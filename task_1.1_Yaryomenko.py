import numpy as np
def findLU(a, b, c):
    l = c.copy()
    d = np.zeros(len(a), float)
    d[0] = a[0]
    u = np.zeros(len(b), float)
    u[0] = b[0]/d[0]
    for i in range(1, len(d)-1):
        d[i] = a[i] - l[i-1]*u[i-1]
        u[i] = b[i]/d[i]
    d[-1] = a[-1] - l[-1]*u[-1]
    return d,l,u
def solve_lu(a,b,c,f):
    d,l,u = findLU(a,b,c)
    y = np.zeros(len(a))
    y[0] = f[0]/d[0]
    for i in range(1, len(y)):
        y[i] = (f[i] - l[i-1]*y[i-1])/d[i]
    x = np.zeros(len(a))
    x[-1] = y[-1]
    for i in range(len(x)-2, -1, -1):
        x[i] = y[i+1] - u[i]*x[i+1]
    return x
def newA(n):
    a = 2*np.ones(n, float)
    b = -1*np.ones(n-1, float)
    c = -1*np.ones(n-1, float)
    return a,b,c
def newB(n):
    h = 1/n
    b = np.zeros(n, float)
    b[0] = -h*(1-h)
    b[n-1] = h*(n+(2-n**2)*h)
    for i in range(1,n-1):
        b[i] = 2*(h**2)
    return b
def newX(n):
    h = 1/n
    x = np.zeros(n,float)
    for i in range(0, n, 2):
        x[i] = i*h*(1-i*h)
    return x
if __name__=='__main__':
    n = 2
    a,b,c = newA(n) 
    f = newB(n)   
    x = solve_lu(a,b,c,f)
    print(x, '\n')
    new_x = newX(n)
    print(new_x)
    print(x == new_x, '\n')
    d, l, u = findLU(a, b, c)
    det = np.prod(d)
    print(det == n+1, '\n')
