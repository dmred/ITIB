'''
Created on 13 апр. 2018 г.
@author: dmred
'''
import math

E = 1.0                 
lerningKoef = 0.2       
N = 1                   
J = 2                   
M = 1                   
Xn = [1.0, -3.0]        
Xj = [0.0]*(J + 1)      #=> объявляем все переменные
Ym = [0.0]*(M)          
Dj = [0.0]*(J)          
Dm = [0.0]*(M)          
t = 1.0                 
net = [0.0]*(J)         
eposCount = 0           

w = ([0.2, 0.2, 0.2, 0.2], [0.2, 0.2, 0.2]) #вектор весов

def f(net): # расчитываем net
    return (1 - math.exp(-net))/(1 + math.exp(-net))

def df(net): #производная net
    return 0.5*(1 - f(net)**2)

while(E > 0.001):   # хотим получить ошибку не больше 0.001
    print ('Epos #', eposCount + 1)
    '''
    Вычисляем параметры скрытого слоя
    '''
    Xj[0] = 1.0 
    for j in range(J):
        net[j] = w[0][j]*Xn[0] + w[0][j + 2]*Xn[1]
        print('net(1)%i = %.5f' %(j + 1, net[j]))
        Xj[j + 1] = f(net[j])
    print('new layer X: ', Xj)
    '''
    Вычисляем параметры выходного слоя
    '''
    for m in range(M):
        net[m] = w[1][0]*Xj[0]
        for i in range(J):
            net[m] += w[1][i + 1]*Xj[i + 1]
        Ym[m] = f(net[m])
        print('net(2)%i = %.5f' %(m + 1, net[m]))
        print('y = %.5f' %Ym[m])
        for i in range(J):   
            Dm[m] = df(net[j]) * (t - Ym[m])
        
        E = math.sqrt(Dm[m]**2)
           
        for i in range(J):
            Dj[i] = df(net[i]) * w[1][j + 1] * Dm[m]
        '''
        Коррекция весов
        '''        
        for j in range(J + M):
            w[1][j] += lerningKoef*Dm[m]*Xj[j]
            
    for j in range(J):
        w[0][j] += lerningKoef*Dj[j]*Xn[0]
        w[0][j + 2] += lerningKoef*Dj[j]*Xn[1]
    print('W: ', w)
    
    print('ε = %.7f' %E) 
    print(Xn, Xj)
    eposCount += 1
    print('_______________________________________________') 