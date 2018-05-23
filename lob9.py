from tkinter import * 
from random import *
from math import sqrt
from time import sleep

root = Tk() #Инициализация графического интерфейса
root.title('Cluster analysis')
root.geometry("500x600+40+80")

def window_deleted():
    print('Программа окончена')
    root.quit() # явное указание на выход
    
root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна

WIDTH = 400
HEIGHT = 400
dots = []
clusters = []
dbyc = []
var=IntVar()
var.set(0)

def Evklid(x1, y1, x2, y2):                    #меры расстояний
    return sqrt( ( (x1-x2) + (y1-y2) )**2 )    #Евклид 

def Chebyshev(x1, y1, x2, y2):                 #Чебышев
    return max(abs(x1-x2), abs(y1-y2))

def clusterisationStep(event):
    for i in range(0,len(dots)):
        d = []                                 #рисуем точки
        for j in range(0,len(clusters)):
            x1 = canvas.coords(dots[i])[0] + 3
            y1 = canvas.coords(dots[i])[1] + 3
            x2 = canvas.coords(clusters[j])[0] + 4
            y2 = canvas.coords(clusters[j])[1] + 4
            if var == 0:
                d.append(int(Evklid(x1, y1, x2, y2))) 
            else:
                d.append(int(Chebyshev(x1, y1, x2, y2)))
        index = d.index(min(d))
        fill_ = canvas.itemcget(clusters[index], 'fill')
        canvas.itemconfig(dots[i],fill=fill_, outline=fill_,tags=str(index))
        dbyc[i] = index
        a = canvas.itemcget(dots[i],'tag')
    sleep(2)
    for i in range(0,len(clusters)):
        b = canvas.find_withtag(str(i))
        if dbyc.count(i) > 0:
            sumx = 0
            sumy = 0
            for j in range(0,len(dots)):
                if dbyc[j] == i:
                    sumx += canvas.coords(dots[j])[0] + 3
                    sumy += canvas.coords(dots[j])[1] + 3
            new_x = int(sumx/dbyc.count(i))
            new_y = int(sumy/dbyc.count(i))
            canvas.coords(clusters[i], new_x-4, new_y-4, new_x+4, new_y+4)
                                
def randColour():
    a = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
    colour = '#'
    for i in range(6):
        seed()
        colour += a[randint(0,15)]      #задаем цвета для кластеров
    return colour

def fillRandomDot(event):
    seed()
    x = randint(5, WIDTH-5)
    y = randint(5, HEIGHT-5)
    dotX.delete(0, END)
    dotY.delete(0, END)
    dotX.insert(0, str(x))
    dotY.insert(0, str(y))
    
def fillRandomCluster(event):
    seed()
    x = randint(5, WIDTH-5)
    y = randint(5, HEIGHT-5)
    clusterX.delete(0, END)
    clusterY.delete(0, END)
    clusterX.insert(0, str(x))
    clusterY.insert(0, str(y))
    
def addDot(event):
    x = int(dotX.get())
    y = int(dotY.get())
    #dot = canvas.create_oval(x-3,y-3,x+3,y+3,fill='black',outline='black')
    dots.append(canvas.create_oval(x-3,y-3,x+3,y+3,fill='black',outline='black'))
    dbyc.append(0)
    #print(canvas.coords(dot))
    
def addCluster(event):
    x = int(clusterX.get())
    y = int(clusterY.get())
    colour = randColour()
    #cluster = canvas.create_rectangle(x-4,y-4,x+4,y+4,fill=colour,outline=colour)
    clusters.append(canvas.create_rectangle(x-4, y-4, x+4, y+4, fill=colour, outline=colour))
    
def clearCanvas(event):
    canvas.delete('all')

canvas = Canvas(root, width=WIDTH, height=HEIGHT) #Инициализируем 400*400
textLabel1 = Label(root, text="Точки:   X:")
textLabel2 = Label(root, text='Кластер:   X:')
dotX = Entry(root, width=10)
dotY = Entry(root, width=10)
clusterX = Entry(root, width=10)
clusterY = Entry(root, width=10)
textY1 = Label(root, text=' Y:')
textY2 = Label(root, text=' Y:')
addDotButton = Button(root, text='Добавить')
addClusterButton = Button(root, text='Добавить')
randomDotButton = Button(root, text='Генерировать')
randomClusterButton = Button(root, text='Генерировать')
clearButton = Button(root, text='Очистить', bg='red')
startButton = Button(root, text='Пуск', bg='red')
successLabel = Label(root, text="Завершено")
rad0 = Radiobutton(root, text="Евклид", variable=var, value=0)
rad1 = Radiobutton(root, text="Чебышев", variable=var, value=1)

randomClusterButton.bind("<Button-1>", fillRandomCluster)
addDotButton.bind("<Button-1>", addDot)
randomDotButton.bind("<Button-1>", fillRandomDot)
addClusterButton.bind("<Button-1>", addCluster)
clearButton.bind("<Button-1>", clearCanvas)
startButton.bind("<Button-1>", clusterisationStep)
chooseLabel = Label(root, text="Метрика:")

textLabel1.grid(row=1, column=1, sticky='e')
textLabel2.grid(row=3, column=1, sticky='e')
dotX.grid(row=1,column=2)                   #ввод X, Y
dotY.grid(row=2,column=2)
clusterX.grid(row=3,column=2)               #ввод X,Y для кластеров
clusterY.grid(row=4,column=2)
textY1.grid(row=2, column=1, sticky='e')
textY2.grid(row=4, column=1, sticky='e')
addDotButton.grid(row=1, column=4)
addClusterButton.grid(row=3,column=4)
randomDotButton.grid(row=1, column=5)
randomClusterButton.grid(row=3, column=5)
clearButton.grid(row=5, column=7)
canvas.grid(row=6, column=1,columnspan=6)
startButton.grid(row=5, column=3, columnspan=6)
rad0.grid(row=7, column=2)
rad1.grid(row=7, column=4)
chooseLabel.grid(row=7, column=1, sticky='e')

root.mainloop()

textLabel1.grid(row=1, column=1, sticky='e')
textLabel2.grid(row=2, column=1, sticky='e')
dotX.grid(row=1,column=2)                   #ввод X, Y
dotY.grid(row=1,column=4)
clusterX.grid(row=2,column=2)               #ввод X,Y для кластеров
clusterY.grid(row=2,column=4)
textY1.grid(row=1, column=3, sticky='e')
textY2.grid(row=2, column=3, sticky='e')
addDotButton.grid(row=1, column=6)
addClusterButton.grid(row=2,column=6)
randomDotButton.grid(row=1, column=5)
randomClusterButton.grid(row=2, column=5)
canvas.grid(row=6, column=1,columnspan=6)
startButton.grid(row=4, column=1, columnspan=6)
rad0.grid(row=3, column=2)
rad1.grid(row=3, column=4)
chooseLabel.grid(row=3, column=1, sticky='e')