'''
Created on 3 апр. 2018 г.
@author: dmred
'''
import math
import matplotlib.pyplot

print('ITIB Laboratory work #2. Application of a single-layer neural network with a linear activation function for the prediction of time series')

W = [0]*15 #|
X = [0]*40 #|===|заготовочки list'ов
y = [0]*20 #|===|заготовочки list'ов
d = [0]*20 #|
p = 4 #ширина "окна"
n = 0.2 #норма обучения
a = 0.0
b = 4.0
f = 0.0
eps = 0.0
net = 0.0
step = (b - a) / 20 #расстояние по икс между дискретными точками

lolik=100000 #(максимум инта)

for p in range(15): 
    era = 5000 #количество эпох
    j = 0

    for j in range(20): #считаем вектор дискретных точек
        X[j]= 0.5 * math.cos(0.5 * (a + j*step)) + (-math.sin(a+j*step))
    j = 0
    i = 0
    for j in range(era): #обучение: считаем net, потом видроу-хофф
        for i in range(20-p):
            net = 0.0
            o = 0
            for o in range(p):
                net += W[o] * X[i + o]
            d[i] = X[i + p] - net   
            u = 0
            if d[i] != 0:
                for u in range(p):
                    W[u] = W[u] + X[i + u] * d[i] * n

    i = 0
    for i in range(20): #просто печатаем инфу
        print('X: %.6f' %(X[i]))
    print('W:')
    for i in range(p):
        print('[%.3f' %(W[i]), end=']')
    
    i = 20 - p
    for i in range(40 - p): #40, тк считаем 20 точек в новом промежутке
        net = 0.0
        o = 0
        for o in range(p):
            net = net + W[o] * X[i + o]
        X[i + p] = net
        y[i + p - 20] = 0.5 * math.cos(0.5 * (b + (i + p - 20)*step)) + (-math.sin(b + (i + p - 20)*step))
        f = y[i + p - 20] - X[i + p] #метрика между прогнозом и настроя
        eps = eps + f**2 #квадратичное расстояние

    i = 20
    for i in range(40): #вывод данных
        print('X[', i, ']: ', X[i],'| Y:', y[i - 20] )
        print('ε =', math.sqrt(eps))
        if (math.sqrt(eps)<lolik): lolik = math.sqrt(eps) 
        #print(y[i - 20])
    
    f = 0.0             #|
    eps = 0.0           #|
    net = 0.0           #|===> чистим память - залог красивого кода
    m = 0               #|
    for m in range(p):  #|
        W[m] = 0

x =[]

#РЕЖИМ ПОСТРОЕНИЯ РЕАЛЬНОГО ГРАФИКА

y_norm = []
for i in range(20):
    x.append(a + i*step)
    #y_norm.append(math.sin(a + i*step))
    y_norm.append(0.5 * math.cos(0.5 * (a + i*step)) + (-math.sin(a+i*step)))
matplotlib.pyplot.plot(x, y_norm)
matplotlib.pyplot.xlabel(r'$x$')
matplotlib.pyplot.ylabel(r'$f(x) non-prediction$')
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()

'''
#РЕЖИМ ПРОГНОЗИРОВАНИЯ
for i in range(20):
    x.append(a + i*step+(2*b-a-b))
matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.xlabel(r'$x$')
matplotlib.pyplot.ylabel(r'$f(x) prediction$')
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()
'''

print('lolik', lolik)