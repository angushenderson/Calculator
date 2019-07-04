# calculator in python tkinter
# Angus Henderson
from tkinter import *
import math

window = Tk()
window.geometry('500x600')
window.title('Calculator')
window.configure(background='black')
global commandline, highest
highest = 0
commandline = []

def decimal():
    global commandline
    if len(commandline) == 0:
        commandline.append([])
        commandline[-1].append('0')
    if type(commandline[-1]) == str:
        commandline.append([])
    commandline[-1].append('.')
    print(commandline[-1])
    drawoutput()

def combinenums():
    global commandline, highest
    tempnum = ''
    tf = False
    temphighest = 0
    if type(commandline[-1]) == float:
        commandline[-1] = str(commandline[-1])
    for c in commandline[-1]:
        tempnum = tempnum + str(c)
        if tf:
            temphighest += 1
        if c == '.':       # loops in this order for a reason dont move or have to add in extra line
            tf = True
    if temphighest > highest:
        highest = temphighest
    if type(commandline[-1]) != str:
        commandline[-1] = float(tempnum)

def addnum(num):
    global commandline
    run = False
    # only add if previous is a symbol or no previous i,e start fo list.
    # if empty. mudt be numbver first
    if len(commandline) == 0:
        run = True

    if len(commandline) > 0:
        if type(commandline[-1]) == list or type(commandline[-1]) == str:
            run = True
        #if type(commandline[-1]) == float:    # this line not necessary however good to overwrite everygthon
        #    run = False

    if run:
        if len(commandline) < 1:
            commandline.append([])
        if type(commandline[-1]) == str:
            commandline.append([])

        commandline[-1].append(str(num))
        drawoutput()

def operation(op):
    global commandline, decimal
    if len(commandline) > 0:
        if len(commandline) > 0:
            if type(commandline[-1]) != str:
                combinenums()
                commandline.append(op)
                drawoutput()

def delete():
    global commandline, highest
    if type(commandline[-1]) == list:
        if len(commandline[-1]) > 0:
            commandline[-1].pop()
    elif type(commandline[-1]) == float:
        str(commandline[-1]).pop()
    else:
        commandline.pop()
    if len(commandline) == 0:
        highest = 0
    drawoutput()

def calculate():
    global commandline, highest

    if type(commandline) == list:
        combinenums()
    # pop last entity if operator
    if len(commandline) >= 3:
        if type(commandline[-1]) == str:
            commandline.pop(-1)

        # combine numbers
        if type(commandline[-1]) == list:
            tempnum = ''        # try to get down to one line
            for c in commandline[-1]:
                tempnum = tempnum + str(c)
            commandline[-1] = float(tempnum)
        
        # looking at bodmas as well
        com = 0
        while com < len(commandline) - 1:
            if commandline[com] == '/':
                operation = float(commandline[com - 1]) / float(commandline[com + 1])
                operation = round(operation,highest)
                commandline.pop(com+1)
                commandline.pop(com)
                commandline.pop(com-1)
                commandline.insert(com-1,operation)   # index,element
                com = 0

            if commandline[com] == '*':
                operation = float(commandline[com - 1]) * float(commandline[com + 1])
                operation = round(operation,highest)
                commandline.pop(com + 1)
                commandline.pop(com)
                commandline.pop(com - 1)
                commandline.insert(com-1,operation)
                com = 0

            com += 1
                
        com = 0
        while com < len(commandline) - 1:
            if commandline[com] == '+':
                operation = float(commandline[com - 1]) + float(commandline[com + 1])
                operation = round(operation,highest)
                commandline.pop(com + 1)
                commandline.pop(com)
                commandline.pop(com - 1)
                commandline.insert(com-1,operation)
                com = 0
                
            if commandline[com] == '-':
                operation = float(commandline[com - 1]) - float(commandline[com + 1])
                print(operation)
                operation = round(operation,highest)
                commandline.pop(com + 1)
                commandline.pop(com)
                commandline.pop(com - 1)
                commandline.insert(com-1,operation)
                com = 0

            com += 1

    drawoutput()

def drawoutput():      # fix this shambles of what you think you can call code
    global commandline  # its operators that are giving me hassle printing 01
    out = ''            # also figure out hoe to remove decimal and one if no numbers after point
    tempnum = ''
    for c in range(len(commandline)):
        add = True
        if type(commandline[c]) == float:   # for full complete numbers
            afterdec = str(commandline[c] - int(commandline[c]))[1:]
            length = len(str(commandline[c]))

            if afterdec == '.0':
                beforedec = (len(str(commandline[c])) - 2)
                out = out + str(commandline[c])[:beforedec]

            else:
                out = out + str(float(commandline[c]))
        
        if type(commandline[c]) == str:
            out = out + str(commandline[c])
            
        if type(commandline[c]) == list:
            for cc in commandline[c]:
                tempnum = tempnum + str(cc)
            out = out + tempnum
    print(commandline)
    output.config(text=out)
 

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

buttondecimal = Button(window, text='.', bg='black', fg='white',command=lambda:decimal())
buttondel = Button(window, text='del', bg='black', fg='white',command=lambda:delete())

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

