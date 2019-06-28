from tkinter import *
import math

window = Tk()
window.geometry('500x600')
window.title('Calculator')
window.configure(background='black')
global commandline
commandline = []

def addnum(num):
    global commandline
    if len(commandline) < 1:
        commandline.append([])
    if type(commandline[-1]) == str:
        commandline.append([])
    commandline[-1].append(str(num))
    output.config(text=commandline)

def operation(op):
    global commandline
    if [commandline[-1] != o for o in ['+','-','*','/','=']]:
        tempnum = ''
        for c in commandline[-1]:
            tempnum = tempnum + str(c)
        commandline[-1] = int(tempnum)
        commandline.append(op)
        output.config(text=commandline)

def calculate():
    global commandline
    # pop last entity if operator
    if type(commandline[-1]) == str:
        commandline.pop(-1)

    # combine numbers
    if type(commandline[-1]) == list:
        tempnum = ''        # try to get down to one line
        for c in commandline[-1]:
            tempnum = tempnum + str(c)
        commandline[-1] = int(tempnum)
    
    # looking at bodmas as well
    com = 0
    while com < len(commandline) - 1:
        if commandline[com] == '/':
            operation = commandline[com + 1] / commandline[com - 1]
            commandline.pop(com+1)
            commandline.pop(com)
            commandline.pop(com-1)
            commandline.insert(com-1,str(operation))   # index,element
            com = 0

        if commandline[com] == '*':
            operation = commandline[com - 1] * commandline[com + 1]
            commandline.pop(com + 1)
            commandline.pop(com)
            commandline.pop(com - 1)
            commandline.insert(com-1,str(operation))
            com = 0

        com += 1
            
    com = 0
    while com < len(commandline) - 1:
        if commandline == '+':
            operation = commandline[com - 1] + commandline[com + 1]
            commandline.pop(com + 1)
            commandline.pop(com)
            commandline.pop(com - 1)
            commandline.insert(com-1,str(operation))
            com = 0
            
        if commandline == '-':
            operation = commandline[com - 1] - commandline[com + 1]
            commandline.pop(com + 1)
            commandline.pop(com)
            commandline.pop(com - 1)
            commandline.insert(com-1,str(operation))
            com = 0

        com += 1
            
    for com in range(len(commandline)):
        if commandline[com] == '+' or com == '-':
            pass
            # do these things
    output.config(text=commandline)
    

button0 = Button(window, text='0', bg='black',fg='white',command=lambda:addnum(0))
button1 = Button(window, text='1', bg='black',fg='white',command=lambda:addnum(1))
button2 = Button(window, text='2', bg='black',fg='white',command=lambda:addnum(2))
button3 = Button(window, text='3', bg='black',fg='white',command=lambda:addnum(3))
button4 = Button(window, text='4', bg='black',fg='white',command=lambda:addnum(4))
button5 = Button(window, text='5', bg='black',fg='white',command=lambda:addnum(5))
button6 = Button(window, text='6', bg='black',fg='white',command=lambda:addnum(6))
button7 = Button(window, text='7', bg='black',fg='white',command=lambda:addnum(7))
button8 = Button(window, text='8', bg='black',fg='white',command=lambda:addnum(8))
button9 = Button(window, text='9', bg='black',fg='white',command=lambda:addnum(9))

buttondecimal = Button(window, text='.', bg='black', fg='white')
buttondel = Button(window, text='del', bg='black', fg='white')

buttonequal = Button(window, text='=', bg='red', fg='white',command=lambda:calculate())
buttonplus = Button(window, text='+', bg='black', fg='white',command=lambda:operation('+'))
buttonminus = Button(window, text='-', bg='black', fg='white',command=lambda:operation('-'))
buttonmultiply = Button(window, text='*', bg='black', fg='white',command=lambda:operation('*'))
buttondivide = Button(window, text='/', bg='black', fg='white',command=lambda:operation('/'))


output = Label(window, text='Output', bg='white',fg='black')
output.place(x=0, y=0, width=500, height=200)

button0.place(x=100,y=500,height=100,width=100)
button1.place(x=0,y=400,height=100,width=100)
button2.place(x=100,y=400,height=100,width=100)
button3.place(x=200,y=400,height=100,width=100)
button4.place(x=0,y=300,height=100,width=100)
button5.place(x=100,y=300,height=100,width=100)
button6.place(x=200,y=300,height=100,width=100)
button7.place(x=0,y=200,height=100,width=100)
button8.place(x=100,y=200,height=100,width=100)
button9.place(x=200,y=200,height=100,width=100)

buttonequal.place(x=300,y=400,width=100,height=200)
buttonplus.place(x=300,y=300,width=100,height=100)
buttonminus.place(x=300,y=200,width=100,height=100)
buttondivide.place(x=400,y=200,width=100,height=100)
buttonmultiply.place(x=400,y=300,width=100,height=100)
buttondecimal.place(x=0,y=500,width=100,height=100)
buttondel.place(x=200,y=500,width=100,height=100)

window.mainloop()

