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
    output.config(text=commandline)

    # next time change things to accomodate float. change things to add
    # as strings then change to either int or float depenfing on if has
    # decimal place or not

def combinenums():
    global commandline, highest
    tempnum = ''
    tf = False
    temphighest = 0
    for c in commandline[-1]:
        tempnum = tempnum + str(c)
        if tf:
            temphighest += 1
        if c == '.':       # loops in this order for a reason dont move or have to add in extra line
            tf = True
    if temphighest > highest:
        highest = temphighest
    commandline[-1] = float(tempnum)
    print("new floating numner: ",commandline[-1])

def addnum(num):
    global commandline
    
    run = False

    # only add if previous is a symbol or no previous i,e start fo list.

    # if empty. mudt be numbver first
    if len(commandline) == 0:
        run = True

    if len(commandline) > 0:
        print("lengh working")
        if [('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0' or '.' or '/' or '*' or '+' or '-' or '=') in commandline[-1]]:
            run = True
            print("number add true")
        
    if run:
        print("runnniiiiinnnnnggggggggg")
        if len(commandline) < 1:
            commandline.append([])
        if type(commandline[-1]) == str:
            print("second string detected")
            commandline.append([])
    
        commandline[-1].append(str(num))
        print(commandline)
        output.config(text=commandline)

def operation(op):
    global commandline, decimal
    print("operations: ",commandline)
    continuee = True
    if len(commandline) < 1:
        print("to short to continue")
        continuee = False
    if continuee:
        print("continuing")
        if len(commandline) > 0:
            if commandline[-1] != '/' or commandline[-1] != '*' or commandline[-1] != '+' or commandline[-1] != '-' or commandline[-1] != '=':
                combinenums()
                commandline.append(op)
                output.config(text=commandline)

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
                commandline.insert(com-1,str(operation))   # index,element
                com = 0

            if commandline[com] == '*':
                operation = float(commandline[com - 1]) * float(commandline[com + 1])
                operation = round(operation,highest)
                commandline.pop(com + 1)
                commandline.pop(com)
                commandline.pop(com - 1)
                commandline.insert(com-1,str(operation))
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
                commandline.insert(com-1,str(operation))
                com = 0
                
            if commandline[com] == '-':
                operation = float(commandline[com - 1]) - float(commandline[com + 1])
                print(operation)
                operation = round(operation,highest)
                commandline.pop(com + 1)
                commandline.pop(com)
                commandline.pop(com - 1)
                commandline.insert(com-1,str(operation))
                com = 0

            com += 1

    highest = 0     
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

buttondecimal = Button(window, text='.', bg='black', fg='white',command=lambda:decimal())
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

