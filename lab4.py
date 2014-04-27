from math import *

class Poly :
    coef = []
    def __init__(self, coef0) :
        self.coef = coef0

    def eval(self, x, iDerivative=0) :
        sum = 0
        for i in range(0, len(self.coef)-iDerivative) :
            sum += self.coef[i+iDerivative]*self.find_der_mult(i+iDerivative,iDerivative)*(x**i)
        return sum

    def find_der_mult(self, ix, iDerivative) :
        if iDerivative==0 :
            return 1
        return ix*self.find_der_mult(ix-1,iDerivative-1)

class Func :
    xk = [] #starting x
    dk = [] #gradient coeff
    coeff1 = [4,1]
    coeff2 = [-5,-6]
    def __init__(self, xk0, dk0) :
        self.xk = xk0
        self.dk = dk0
    def eval(self, x) :
        sum = 0
        for i in range(0, len(self.coeff1)) :
            sum += self.coeff1[i]*(self.xk[i]+self.dk[i]*x+self.coeff2[i])**2
        return sum

def golden(a, b, func, eps, minx) :
    while (b-a>eps) :
        ratio = (b-a)/((sqrt(5)+1)/2)
        x1 = b-ratio
        x2 = a+ratio
        if func.eval(x1) > func.eval(x2) :
            a = x1
        else :
            b = x2
    minx[0] = (a+b)/2
    #miny[0] = eval(minx[0]);

def unite_lists(l1,l2) :
    list = []
    i = 0
    for l1c in l1 :
        list.append([l1[i],l2[i]])
        i+=1
    return list

def sqr(x) :
    return x*x

def subtract_lists(l1,l2) :
    sum = 0
    for i in unite_lists(l1,l2) :
        sum += sqr(i[0]-i[1])
    return sqrt(sum)

def Koshi(xk, g, eps, x) :
    a = -99
    b = 99
    while 1 :
        dk = []
        for i in unite_lists(g,xk) :
            dk.append(-i[0].eval(i[1]))
        lambdak = [[]]
        golden(a,b,Func(xk,dk),eps,lambdak)
        print xk,dk,lambdak
        #count next xk
        xk1 = []
        for i in unite_lists(dk,xk) :
            xk1.append(i[1]+lambdak[0]*i[0])
        x[0] = xk[1]
        if abs(subtract_lists(xk1,xk))<eps :
            return
        xk = xk1

#gradient of function 4(x1-5)^2+(x2-6)^2
g = [Poly([-40,8]),Poly([-12,2])]
xk = [0,0]
eps = 1e-5
x = [[]]
Koshi(xk,g,eps,x)
print(x)
