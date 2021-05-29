from tkinter import*

def pressed(n):
    global equation_text

    equation_text = equation_text + str(n)
    equation.set(equation_text)


def clear():
    global equation_text

    equation.set("")

    equation_text = ""


def equals():

    global equation_text

    
    try:

        total = str(eval(equation_text))

        equation.set(total)

        equation_text = total
    except ZeroDivisionError:

        equation.set("Can't divide by zero.")

        equation_text = " "

    except SyntaxError:

        equation.set("Something isn't right.")

        equation_text = " "


#Now do window stuff

window = Tk()
window.title("Calculator")
window.geometry("500x500")

equation_text = " "
equation = StringVar()
label = Label(window,textvariable=equation,font=('consolas',20), bg="white",width=24,height=2)
label.pack()


#buttons unfortunately, can automate the process
frame = Frame(window)
frame.pack()


b1 = Button(frame,text=1,height=4,width=9,font=35,
            command=lambda: pressed(1))
b1.grid(row=0,column=0)

b2 = Button(frame,text=2,height=4,width=9,font=35,
            command=lambda: pressed(2))
b2.grid(row=0,column=1)

b3 = Button(frame,text=3,height=4,width=9,font=35,
            command=lambda: pressed(3))
b3.grid(row=0,column=2)

b4 = Button(frame,text=4,height=4,width=9,font=35,
            command=lambda: pressed(4))
b4.grid(row=1,column=0)


b5 = Button(frame,text=5,height=4,width=9,font=35,
            command=lambda: pressed(5))
b5.grid(row=1,column=1)

b6 = Button(frame,text=6,height=4,width=9,font=35,
            command=lambda: pressed(6))
b6.grid(row=1,column=2)

b7 = Button(frame,text=7,height=4,width=9,font=35,
            command=lambda: pressed(7))
b7.grid(row=2,column=0)

b8 = Button(frame,text=8,height=4,width=9,font=35,
            command=lambda: pressed(8))
b8.grid(row=2,column=1)

b9 = Button(frame,text=9,height=4,width=9,font=35,
            command=lambda: pressed(9))
b9.grid(row=2,column=2)


b0 = Button(frame,text=0,height=4,width=9,font=35,
            command=lambda: pressed(0))
b0.grid(row=3,column=0)

plus = Button(frame,text='+',height=4,width=9,font=35,
            command=lambda: pressed('+'))
plus.grid(row=0,column=3)


minus = Button(frame,text='-',height=4,width=9,font=35,
            command=lambda: pressed('-'))
minus.grid(row=1,column=3)

multiply = Button(frame,text='*',height=4,width=9,font=35,
            command=lambda: pressed('*'))
multiply.grid(row=2,column=3)

divide = Button(frame,text='/',height=4,width=9,font=35,
            command=lambda: pressed('/'))
divide.grid(row=3,column=3)


equal = Button(frame,text='=',height=4,width=9,font=35,
            command=equals)
equal.grid(row=3,column=2)


decimals = Button(frame,text='.',height=4,width=9,font=35,
            command=lambda: pressed('.'))
decimals.grid(row=3,column=1)


clear = Button(window,text='clear',height=4,width=12,font=35,
            command=clear)
clear.pack()




window.mainloop()