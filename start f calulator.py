from tkinter import *
import math

window = Tk()
window.geometry('500x600')
window.title('Calculator')
window.configure(background='black')

button0 = Button(window, text='0', bg='black',fg='white')
button1 = Button(window, text='1', bg='black',fg='white')
button2 = Button(window, text='2', bg='black',fg='white')
button3 = Button(window, text='3', bg='black',fg='white')
button4 = Button(window, text='4', bg='black',fg='white')
button5 = Button(window, text='5', bg='black',fg='white')
button6 = Button(window, text='6', bg='black',fg='white')
button7 = Button(window, text='7', bg='black',fg='white')
button8 = Button(window, text='8', bg='black',fg='white')
button9 = Button(window, text='9', bg='black',fg='white')

buttondecimal = Button(window, text='.', bg='black', fg='white')
buttondel = Button(window, text='del', bg='black', fg='white')

buttonequal = Button(window, text='=', bg='red', fg='white')
buttonplus = Button(window, text='+', bg='black', fg='white')
buttonminus = Button(window, text='-', bg='black', fg='white')
buttonmultiply = Button(window, text='*', bg='black', fg='white')
buttondivide = Button(window, text='/', bg='black', fg='white')


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



