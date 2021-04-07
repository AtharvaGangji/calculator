import tkinter as tk
from tkinter import *
from tkinter import messagebox

xpo = tk.Tk()
xpo.title("Calculator")
xpo.geometry("300x400+300+300")
xpo.resizable(0,0)

val = ""
operation = None
A = 0

# funtions

def op_clicked(xposive):
    global operation, A
    global mad, val
    if xposive == 1:
        operation = "+"
        mad.set(operation)
        A = int(val)
        val = ""
    if xposive == 2:
        operation = "-"
        mad.set(operation)
        A = int(val)
        val = ""

def b_0_click():
    global val
    global mad
    val = val + "0"
    mad.set(val)


def b_1_click():
    global val
    global mad
    val = val + "1"
    mad.set(val)

def b_2_click():
    global val
    global mad
    val = val + "2"
    mad.set(val)

def b_3_click():
    global val
    global mad
    val = val + "3"
    mad.set(val)

def b_4_click():
    global val
    global mad
    val = val + "4"
    mad.set(val)

def b_5_click():
    global val
    global mad
    val = val + "5"
    mad.set(val)

def b_6_click():
    global val
    global mad
    val = val + "6"
    mad.set(val)

def b_7_click():
    global val
    global mad
    val = val + "7"
    mad.set(val)

def b_8_click():
    global val
    global mad
    val = val + "8"
    mad.set(val)

def b_9_click():
    global val
    global mad
    val = val + "9"
    mad.set(val)

def c_click():
    global val
    val = ""
    mad.set(val)


mad = StringVar()

OP = "#789999"
last_line_bg = None

l_1 = tk.Label(xpo, bg = "black", font = ("Arial", 20), anchor = SE, textvariable = mad, fg = "white")
l_1.pack(expand = True, fill = "both")

l_3 = tk.Label(xpo)
l_3.pack(expand = True, fill = "both")

l_4 = tk.Label(xpo)
l_4.pack(expand = True, fill = "both")

l_5 = tk.Label(xpo)
l_5.pack(expand = True, fill = "both")

l_6 = tk.Label(xpo)
l_6.pack(expand = True, fill = "both")

b_1 = tk.Button(l_5, text = "1", relief = GROOVE, border = 0, command = lambda: b_1_click())
b_1.pack(side = "left", expand = True, fill = "both")

b_2 = tk.Button(l_5, text = "2", relief = GROOVE, border = 0, command = lambda: b_2_click())
b_2.pack(side = "left", expand = True, fill = "both")

b_3 = tk.Button(l_5, text = "3", relief = GROOVE, border = 0, command = lambda: b_3_click())
b_3.pack(side = "left", expand = True, fill = "both")

b_4 = tk.Button(l_4, text = "4", relief = GROOVE, border = 0, command = lambda: b_4_click())
b_4.pack(side = "left", expand = True, fill = "both")

b_5 = tk.Button(l_4, text = "5", relief = GROOVE, border = 0, command = lambda: b_5_click())
b_5.pack(side = "left", expand = True, fill = "both")

b_6 = tk.Button(l_4, text = "6", relief = GROOVE, border = 0, command = lambda: b_6_click())
b_6.pack(side = "left", expand = True, fill = "both")

b_7 = tk.Button(l_3, text = "7", relief = GROOVE, border = 0, command = lambda: b_7_click())
b_7.pack(side = "left", expand = True, fill = "both")

b_8 = tk.Button(l_3, text = "8", relief = GROOVE, border = 0, command = lambda: b_8_click())
b_8.pack(side = "left", expand = True, fill = "both")

b_9 = tk.Button(l_3, text = "9", relief = GROOVE, border = 0, command = lambda: b_9_click())
b_9.pack(side = "left", expand = True, fill = "both")

b_equal = tk.Button(l_6, text = "=", bg = "yellow", relief = GROOVE, border = 0)
b_equal.pack(side = "right", expand = True, fill = "both")

b_0 = tk.Button(l_6, text = "0", relief = GROOVE, border = 0, bg = last_line_bg, command = lambda: b_0_click())
b_0.pack(side = "left", expand = True, fill = "both")

b_plus = tk.Button(l_6, text = "+", relief = GROOVE, border = 0, bg = last_line_bg, command = lambda: op_clicked(1))
b_plus.pack(side = "left", expand = True, fill = "both")

b_minus = tk.Button(l_3, text = "-", bg = OP, relief = GROOVE, border = 0, command = lambda: op_clicked(2))
b_minus.pack(side = "left", expand = True, fill = "both")

b_divide = tk.Button(l_4, text = "/", bg = OP, relief = GROOVE, border = 0)
b_divide.pack(side = "left", expand = True, fill = "both")

b_multiply = tk.Button(l_5, text = "*", bg = OP, relief = GROOVE, border = 0)
b_multiply.pack(side = "left", expand = True, fill = "both")

b_c = tk.Button(l_6, text = "c", relief = GROOVE, border = 0, bg = last_line_bg,command = lambda: c_click() )
b_c.pack(side = "left", expand = True, fill = "both")

xpo.mainloop()