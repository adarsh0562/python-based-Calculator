# name of item,quantity of item,rate per item
# calculate total bill and discount of 20%
# deducted and show total bill

from tkinter import *

root = Tk()

root.title("Calculator 1.0 - ( By Adarsh Raj )")
root.configure()
# root.geometry("400x400+100+100")

root.minsize(width=360, height=240)
root.maxsize(width=360, height=240)
t1 = Entry(root, font=("corbel", 19))
#t1.insert(0,'Developed By Adarsh Raj')
t1.grid(row=0, column=1, columnspan=3)


def clear():
    t1.delete(len(t1.get()) - 1, END)


b1 = Button(root, text="<-", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=clear)
b1.grid(row=1, column=0)
lb1 = Label(root, text=" ")
lb1.grid(row=1, column=1)
lb2 = Label(root, text=" ")
lb2.grid(row=1, column=2)


def ac():
    t1.delete(0, END)


def equal():
    global find
    eq = eval(t1.get())
    t1.delete(0, END)
    t1.insert(END, eq)
    find = False


def insertOp(op):
    global operators
    if len(t1.get()) != 0:
        if t1.get()[-1] == op:
            pass
        elif t1.get()[-1] in operators:
            t1.delete(len(t1.get()) - 1, END)
            t1.insert(END, op)

        else:
            t1.insert(END, op)
    elif len(t1.get()) == 0:
        if operators[1] == op:
            t1.insert(END, op)


find = True


def insertData(d):

    global find
    global operators
    if len(t1.get()) != 0:
        if t1.get()[-1] in operators:
            t1.insert(END, d)
        elif t1.get()[-1].isdigit:
            if find == False:
                t1.delete(0, END)
                find = True
            t1.insert(END, d)
    elif len(t1.get()) == 0:
        t1.insert(END, d)


b2 = Button(root, text="X", width=10, height=2, fg="blue", bg="red", font=("arial black", 8), command=ac)
b2.grid(row=1, column=3)
b3 = Button(root, text="1", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8),
            command=lambda: insertData(1))  # t1.insert(END,1) .(2). t1.insert(len(t1.get()) + 1, 1)
b3.grid(row=2, column=0)
b4 = Button(root, text="2", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertData(2))
b4.grid(row=2, column=1)
b5 = Button(root, text="3", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertData(3))
b5.grid(row=2, column=2)
b6 = Button(root, text="+", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertOp('+'))
b6.grid(row=2, column=3)
b7 = Button(root, text="4", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertData(4))
b7.grid(row=3, column=0)
b8 = Button(root, text="5", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertData(5))
b8.grid(row=3, column=1)
b9 = Button(root, text="6", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertData(6))
b9.grid(row=3, column=2)
b10 = Button(root, text="-", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertOp("-"))
b10.grid(row=3, column=3)

b11 = Button(root, text="7", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertData(7))
b11.grid(row=4, column=0)
b12 = Button(root, text="8", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertData(8))
b12.grid(row=4, column=1)
b13 = Button(root, text="9", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertData(9))
b13.grid(row=4, column=2)
b14 = Button(root, text="*", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertOp("*"))
b14.grid(row=4, column=3)
b15 = Button(root, text="0", width=10, height=2, fg="blue", bg="light gray", font=("arial black", 8), command=lambda: insertData(0))
b15.grid(row=5, column=0)

operators = ['+', '-', '*', '/', "."]


def insertDot():
    global operators
    text = t1.get()
    i = 0
    for x in range(len(text)-1, -1, -1):
        if text[x] in operators:
            i = x
            break
    if "." in text[i:]:
        pass
    else:
        t1.insert(END, ".")


b16 = Button(root, text=".", width=10, height=2, fg="blue", bg="light gray",font=("arial black",8), command=lambda: insertDot())
b16.grid(row=5, column=1)
b17 = Button(root, text="=", width=10, height=2, fg="blue", bg="light gray",font=("arial black",8), command=equal)
b17.grid(row=5, column=2)
b18 = Button(root, text="/", width=10, height=2, fg="blue", bg="light gray",font=("arial black",8), command=lambda: insertOp("/"))
b18.grid(row=5, column=3)
root.mainloop()
