from tkinter import *


def btn_click(number):
    global val
    val = val+str(number)
    data.set(val)



def btn_clear():
    global val
    val = ""
    data.set("")


def btn_equal():
    global val
    result = str(eval(val))
    data.set(result)



root = Tk()
root.title("Calculator")
root.resizable(False, False)
val = ""
data = StringVar()
entry = Entry(root, textvariable=data, width=15, justify="right", font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

btn7 = Button(root, text="7", width=5, height=1, command=lambda: btn_click(7))
btn7.grid(row=1, column=0)
btn8 = Button(root, text="8", width=5, height=1, command=lambda: btn_click(8))
btn8.grid(row=1, column=1)
btn9 = Button(root, text="9", width=5, height=1, command=lambda: btn_click(9))
btn9.grid(row=1, column=2)
btn_add = Button(root, text="+", width=5, height=1, command=lambda: btn_click('+'))
btn_add.grid(row=1, column=3)

btn4 = Button(root, text="4", width=5, height=1, command=lambda: btn_click(4))
btn4.grid(row=2, column=0)
btn5 = Button(root, text="5", width=5, height=1, command=lambda: btn_click(5))
btn5.grid(row=2, column=1)
btn6 = Button(root, text="6", width=5, height=1, command=lambda: btn_click(6))
btn6.grid(row=2, column=2)
btn_sub = Button(root, text="-", width=5, height=1, command=lambda: btn_click('-'))
btn_sub.grid(row=2, column=3)

btn1 = Button(root, text="1", width=5, height=1, command=lambda: btn_click(1))
btn1.grid(row=3, column=0)
btn2 = Button(root, text="2", width=5, height=1, command=lambda: btn_click(2))
btn2.grid(row=3, column=1)
btn3 = Button(root, text="3", width=5, height=1, command=lambda: btn_click(3))
btn3.grid(row=3, column=2)
btn_mul = Button(root, text="*", width=5, height=1, command=lambda: btn_click('*'))
btn_mul.grid(row=3, column=3)


btn_c = Button(root, text="C", width=5, height=1, command=btn_clear)
btn_c.grid(row=4, column=0)
btn0 = Button(root, text="0", width=5, height=1, command=lambda: btn_click(0))
btn0.grid(row=4, column=1)
btn_equ = Button(root, text="=", width=5, height=1, command=btn_equal)
btn_equ.grid(row=4, column=2)
btn_div = Button(root, text="/", width=5, height=1, command=lambda: btn_click('/'))
btn_div.grid(row=4, column=3)
root.mainloop()
