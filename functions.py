'''
Created on 4 апр. 2017 г.
@author: Сергей
'''
import math
import matplotlib.pyplot as plotF

p = 11
X = [0]*40
d = 0
w = [0.0]*(p + 1)
a = -2
b = 2
n = 0.5

def prediction(X, w, t): #возвращаем квадратичную E
    net = 0
    d = 0.0
    net += sum(X[i]*w[i] for i in range(p+1))
    d = t - net
    i = 0
    for i in range(p + 1):
        w[i] += (d * n * X[i])
    return d ** 2

def net(X, w): #Считаем net
    net = 0
    net += sum(X[i]*w[i] for i in range(p + 1))
    return net

def learning(num_of_epos):   
    N = 20
    F = []
    i = 0
    for i in range(N): #равномерно разбиваю на известные точки 
        F.append(math.sin((a + i - 1)))
        #F.append(a + i - 1)
        i += 1
        
    print()
    print("Number of epos: ", num_of_epos)
    
    epo = 0
    for epo in range(num_of_epos):
        e = 0.0
        i = 0
        j = 1
        for i in range(N - p):
            for j in range(p + 1):
                X[j] = F[i + j - 1]
            w = [0]*(p + 1) 
            d = prediction(X, w, F[i + p])/(N - p)
            e += d
        
    print("ε = ", math.sqrt(e))

    for i in range(p): #просматриваем "окно"
        print('w[%s] = %.3f' %(i, w[i]), end=' ')
        
    x = a
    i = N - p 
    j = 1
    print("\nx:       y:       σ:")
    for i in range(2*N - p - 1):
        for j in range(p + 1):
            X[0] = 1
            X[j] = F[i + j - 1]
        y = net(X, w)
        x += 0.25
        mistake = (math.sin(x) - 1) - y
        F.append(y)
        print(y)
        #print("%.2f   %.7f   %.7f" %(x, y, mistake))
     
  
  
  
  
      
'''
def learning(epos):
    e = 0.00000
    ep = 0
    for ep in range(epos):
        i = 0
        j = 0
        for i in range(20):
            X[i] = math.sin(a + (i*(b - a)/20) - 1) #(b - a)/20 - равное количество шагов в интервал 
         
        i = 0
        for j in range(ep):
            for i in range(20 - p):
                net = 0.0
                net = sum(X[i + itern]*w[itern] for itern in range(p))
                d[i] = X[i + p] - net
                
                num = 0
                if d != 0:
                    for num in range(p):
                        w[num] += X[i + num] * d[i] * n 
    
        e = 0
        i = 20 - p    
        for i in range(40 - p):
            net = 0.0
            for itern in range(p):
                net += X[i + itern]*w[itern]
            X[i + p] = net
            y[i + p - 20] = math.sin(b + (i + p - 20)*(b - a)/20) 
            f = y[i + p - 20] - X[i + p] 
            e += f ** 2
               
        i = 20
        for i in range(40):
            print('ε = %.7f' %(math.sqrt(e))) 
              
        w = [0]*10
        f = 0
        e = 0
        net = 0
    #plotF.plot(X, y)  
    #plotF.show()             
    '''