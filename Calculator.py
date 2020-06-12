#!/usr/bin/env python
# coding: utf-8

# In[145]:


from tkinter import *
import math
from tkinter import messagebox
screen = Tk()
screen.title("Calculator")
screen.maxsize(width=356,height=490)
screen.minsize(width=356,height=490)
screen.iconbitmap('calculator.ico')

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)
    
def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification',"Try Again!",master=screen)
    
tex =StringVar()
operator = ''

entry1 = Entry(screen,font=('Times',20,'bold'),bd=30,justify = 'right',textvariable=tex)
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,text="7",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click(7),activebackground='powderblue',activeforeground='black')
btn7.grid(row=1,column=0)

btn8 = Button(screen,text="8",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click(8),activebackground='powderblue',activeforeground='black')
btn8.grid(row=1,column=1)

btn9 = Button(screen,text="9",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click(9),activebackground='powderblue',activeforeground='black')
btn9.grid(row=1,column=2)

btnAdd = Button(screen,text="+",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click('+'),activebackground='powderblue',activeforeground='black')
btnAdd.grid(row=1,column=3)

btn4 = Button(screen,text="4",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click(4),activebackground='powderblue',activeforeground='black')
btn4.grid(row=2,column=0)

btn5 = Button(screen,text="5",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click(5),activebackground='powderblue',activeforeground='black')
btn5.grid(row=2,column=1)

btn6 = Button(screen,text="6",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click(6),activebackground='powderblue',activeforeground='black')
btn6.grid(row=2,column=2)

btnSub = Button(screen,text="−",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click('-'),activebackground='powderblue',activeforeground='black')
btnSub.grid(row=2,column=3)

btn1 = Button(screen,text="1",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click(1),activebackground='powderblue',activeforeground='black')
btn1.grid(row=3,column=0)

btn2 = Button(screen,text="2",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click(2),activebackground='powderblue',activeforeground='black')
btn2.grid(row=3,column=1)

btn3 = Button(screen,text="3",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click(3),activebackground='powderblue',activeforeground='black')
btn3.grid(row=3,column=2)

btnMul = Button(screen,text="X",font=('Times',20,'bold'),bd=8,padx=15,pady=16,command=lambda:click('*'),activebackground='powderblue',activeforeground='black')
btnMul.grid(row=3,column=3)

btn0 = Button(screen,text="0",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click(0),activebackground='powderblue',activeforeground='black')
btn0.grid(row=4,column=0)

btnClear = Button(screen,text="C",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command = clear,activebackground='powderblue',activeforeground='black')
btnClear.grid(row=4,column=1)

btneq = Button(screen,text="=",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command = equal,activebackground='powderblue',activeforeground='black')
btneq.grid(row=4,column=2)

btnDiv = Button(screen,text="÷",font=('Times',20,'bold'),bd=8,padx=16,pady=16,command=lambda:click('/'),activebackground='powderblue',activeforeground='black')
btnDiv.grid(row=4,column=3)

screen.mainloop()

