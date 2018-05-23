from tkinter import *
import tkinter.filedialog
from numpy.f2py.crackfortran import dimensionpattern

root = Tk()
root.title('Hopfield Network')
root.geometry("400x460+100+40")

def window_deleted():
    print('Программа окончена')
    root.quit() # явное указание на выход
root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна

wid = 6
heig = 6
dim = wid * heig
idol = []*3          #инициализируем эталоны
for i in range(3):
    idol.append([-1]*36)
testArr = [-1]*36 

def getWeigth(W, X):        #функция вычисляющая матрицу весов W = X*Xтанспозир.
    for i in range(dim):
        for j in range(dim):
            if i == j:
                W[i][j] = 0
            else:
                W[i][j] += X[i] * X[j]  


def NET(W, X, distortedArr, arr):
    count = 0
    #if recursion == 32:
    #    return False

    while (distortedArr != X) & (count < 32):
        for i in range(dim):
            arr.append(distortedArr[i])
        #правило Хебба (обучение за один такт)
        for i in range(dim):
            net = 0
            for j in range(dim):
                net += arr[j] * W[j][i]
            if net > 0:
                distortedArr[i] = 1
            elif net < 0:
                distortedArr[i] = -1  
        count += 1
        print('epos', count)

    return distortedArr

def Clear(event):
    testArr = [-1]*36
    idol = []*3          
    for i in range(3):
        idol.append([-1]*36)
    WorkingSet()
    
def Begin(event, idolNum):
    testArr = [-1]*36
    idol = []*3          
    for i in range(3):
        idol.append([-1]*36)
    display['text'] = '1'
    count = int(display['text'])
    label_res['text'] = '_________________'
    WorkingSet()

def Load(event, count): 
    count += 1
    display['text'] = count
    learnBtn.bind("<Button-1>", lambda event, learnBtn=learnBtn: Load(event, int(display['text'])))
    WorkingSet()     
   
def Bit(event, button, idolNum):
    num = -1
    if count < 4:
        if idolNum == 1:
            num = 0
            if button['bg'] == 'SystemButtonFace':
                button['bg'] = 'red'
                idol[num][button['text'] - 1] = 1
            else:
                button['bg'] = 'SystemButtonFace'
                idol[num][button['text'] - 1] = -1
            print ('изменили: ', button['text'], 'pxl') #log'и в консоль
        elif idolNum == 2:
            num = 1
            if button['bg'] == 'SystemButtonFace':
                button['bg'] = 'red'
                idol[num][button['text'] - 1] = 1
            else:
                button['bg'] = 'SystemButtonFace'
                idol[num][button['text'] - 1] = -1
            print ('изменили: ', button['text'], 'pxl') #log'и в консоль
        elif idolNum == 3:
            num = 2
            if button['bg'] == 'SystemButtonFace':
                button['bg'] = 'red'
                idol[num][button['text'] - 1] = 1
            else:
                button['bg'] = 'SystemButtonFace'
                idol[num][button['text'] - 1] = -1
            print ('изменили: ', button['text'], 'pxl')  #log'и в консоль
        else:
            print('Введенный образец - не эталон!')
            if button['bg'] == 'SystemButtonFace':
                button['bg'] = 'black'
                print ('изменили: ', button['text'], 'pxl') #log'и в консоль
                testArr[button['text'] - 1] = 1
            else:
                button['bg'] = 'SystemButtonFace'
                testArr[button['text'] - 1] = -1

def PrintResult(arr):
    for line in range(wid):
        for col in range(heig):
            if arr[line*wid + col] == -1:
                btn1 = Button(bottom_frame, text=(line*wid + col + 1), width=3, height=1, bg='SystemButtonFace')
                btn1.grid(row=line, column=col) 
            elif arr[line*wid + col] == 1:
                btn1 = Button(bottom_frame, text=(line*wid + col + 1), width=3, height=1, bg='red')
                btn1.grid(row=line, column=col)
      
def Compare(event):
    arr = [-1]*dim
    label_res['text'] = '' #чистим поле, если будет проверка нескольких образцов
    PrintResult(arr)
    W = [0] * dim          #инициализируем матрицы весов
    for i in range(dim):
        W[i] = [0] * dim
            
    getWeigth(W, idol[0])
    getWeigth(W, idol[1])
    getWeigth(W, idol[2])
    
    for i in range(3):  #log'и в консоль
        print(idol[i])   
    print('Проверка:') 
    i = 0
    while i < 36:
        print(testArr[i:i + 6])
        i += 6 
    print('Распознавание:') 
    
    check = True  
    for num in range(3):
        for i in range(dim):
            arr[i] = testArr[i]
            
        arr = NET(W, idol[num], arr, [])
        print(check)
        if (arr != idol[num]):
            label_res['text'] += ('Распознать эталон %i не удалось\n' %(num+1))
            print('Распознать эталон %i не удалось' %(num+1))
        else:
            label_res['text'] += ('Распознан эталон %i\n' %(num+1))
            PrintResult(arr)
            '''
            i = 0
            while i < 36:
                print(arr[i:i + 6])     #берем со срезом     #вывод в консоль
                i += 6
                
            # ищем какой именно эталон удалось распознать    
            probability = [0]*3             #вероятность распознавания
            if arr == idol[0]:
                probability[0] = 1
                label_res['text'] += ('\nРаспознан эталон # %i' %(1))
                print('Распознан эталон # %i' %(i + 1))
                PrintResult()
            if arr == idol[1]:
                probability[1] = 1
                label_res['text'] += ('\nРаспознан эталон # %i' %(2))
                print('Распознан эталон # %i' %(i + 1))
                
            if arr == idol[2]:
                probability[2] = 1
                label_res['text'] += ('\nРаспознан эталон # %i' %(3))
                print('Распознан эталон # %i' %(i + 1))
            '''
                
    '''
    #тест на эталонных образцах
    check = [0] * dim
    for i in range(dim):
        check[i] = [0] * dim
    
    for i in range(3):
        check[i] = NET(W, idol[i], idol[i], [], 0)
        if check[i] == False:
            label_res['text'] = 'Распознать %i-й эталон образец не удалось' %(i + 1)
        else:
            label_res['text'] += '\nЭталон #%i  распознан' %(i + 1)
    '''
    Load(event, int(display['text']))   # очищаем поле для след. образца
    compareBtn.bind("<Button-1>", Compare)
                    
def WorkingSet():       #перерисовка поля 
    for i in range(wid):
        for j in range(heig):
            btn = Button(top_frame, text=(i*wid + j + 1), width=3, height=1)
            btn.grid(row=i, column=j)
            btn.bind("<Button-1>", lambda event, btn=btn: Bit(event, btn, int(display['text'])))
    if int(display['text']) < 4:
        label_hint['text'] = 'note: Ввод данных для трёх эталонных образцов'
        learnBtn['bg'] = 'red'
        compareBtn['bg'] = 'SystemButtonFace'
    else: 
        label_hint['text'] = 'note: Образец для распознавания'
        learnBtn['bg'] = 'SystemButtonFace'
        compareBtn['bg'] = 'red'
        
panelFrame = Frame(root, bg = 'gray')
panelFrame.pack(side = 'top', fill = 'x')


clearBtn = Button(panelFrame, height = 2, text = 'clear')
beginBtn = Button(panelFrame, height = 2, text = 'begin again')
clearBtn.bind("<Button-1>", Clear)
beginBtn.bind("<Button-1>", lambda event, beginBtn=beginBtn: Begin(event, int(display['text'])))
clearBtn.pack(side=RIGHT)
beginBtn.pack(side=RIGHT)

learnBtn = Button(panelFrame, height = 2, text = 'remember')
compareBtn = Button(panelFrame, height = 2, text = 'recognize')
learnBtn.bind("<Button-1>", lambda event, learnBtn=learnBtn: Load(event, count))
compareBtn.bind("<Button-1>", Compare)
learnBtn.pack(side=LEFT)
compareBtn.pack(side=LEFT)

label_top =Label(root, text='Для загрузки нового образца нажмите "Запомнить":')
label_top.pack(fill='x')
display = Label(root, font=('Helvetica', 16), bd=3, width=20, text='1')
display.pack(fill='x')
count = int(display['text'])

top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

label_hint =Label(root, text='1-3 ввод данных для трёх эталонных образцов')
label_hint.pack(fill='x')
WorkingSet()

mainFrame = Frame(root, height = 5, bg = 'gray')
mainFrame.pack(fill = 'x')

label_bottom =Label(root, text='Результат:')
label_bottom.pack(fill='x')
label_res =Label(root, text='_________________')
label_res.pack(fill='x')

root.mainloop()