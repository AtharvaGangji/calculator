import tkinter as tk
from tkinter import *
from tkinter import messagebox
from playsound import playsound

# funtions


def play_sound():
    playsound('click-sound.mp3')

def input_number(number, mad):

   global val
   play_sound()
   # join string
   val = val + str(number)
   mad.set(val)

def evaluate(mad):
    global val
    # evaluate the numbers
    play_sound()
    try:
        result = str(eval(val))
        # showing the result
        mad.set(result)

        val = ""
    except:
        mad.set("Enter Valid expression")
        val = ""

def clear_input_field(equation):
   global val
   play_sound()
   val = ""
   equation.set(val)

if __name__=="__main__":

    xpo = tk.Tk()
    xpo.title("Calculator")
    xpo.geometry("300x400+300+300")
    xpo.resizable(0,0)
    val = ""
    mad = StringVar()

    OP = "#789999"
    last_line_bg = None

    l_1 = tk.Label(xpo, bg="black", font=("Arial", 20), anchor=SE, textvariable=mad, fg="white")
    l_1.pack(expand=True, fill="both")

    l_3 = tk.Label(xpo)
    l_3.pack(expand=True, fill="both")

    l_4 = tk.Label(xpo)
    l_4.pack(expand=True, fill="both")

    l_5 = tk.Label(xpo)
    l_5.pack(expand=True, fill="both")

    l_6 = tk.Label(xpo)
    l_6.pack(expand=True, fill="both")

    b_1 = tk.Button(l_5, text="1", relief=GROOVE, border=0, command=lambda: input_number(1,mad))
    b_1.pack(side="left", expand=True, fill="both")

    b_2 = tk.Button(l_5, text="2", relief=GROOVE, border=0, command=lambda: input_number(2,mad))
    b_2.pack(side="left", expand=True, fill="both")

    b_3 = tk.Button(l_5, text="3", relief=GROOVE, border=0, command=lambda: input_number(3,mad))
    b_3.pack(side="left", expand=True, fill="both")

    b_4 = tk.Button(l_4, text="4", relief=GROOVE, border=0, command=lambda: input_number(4,mad))
    b_4.pack(side="left", expand=True, fill="both")

    b_5 = tk.Button(l_4, text="5", relief=GROOVE, border=0, command=lambda: input_number(5,mad))
    b_5.pack(side="left", expand=True, fill="both")

    b_6 = tk.Button(l_4, text="6", relief=GROOVE, border=0, command=lambda: input_number(6,mad))
    b_6.pack(side="left", expand=True, fill="both")

    b_7 = tk.Button(l_3, text="7", relief=GROOVE, border=0, command=lambda: input_number(7,mad))
    b_7.pack(side="left", expand=True, fill="both")

    b_8 = tk.Button(l_3, text="8", relief=GROOVE, border=0, command=lambda: input_number(8,mad))
    b_8.pack(side="left", expand=True, fill="both")

    b_9 = tk.Button(l_3, text="9", relief=GROOVE, border=0, command=lambda: input_number(9,mad))
    b_9.pack(side="left", expand=True, fill="both")

    b_equal = tk.Button(l_6, text="=", bg="yellow", relief=GROOVE, border=0,command=lambda :evaluate(mad))
    b_equal.pack(side="right", expand=True, fill="both")

    b_0 = tk.Button(l_6, text="0", relief=GROOVE, border=0, bg=last_line_bg, command=lambda: input_number(0,mad))
    b_0.pack(side="left", expand=True, fill="both")

    b_plus = tk.Button(l_6, text="+", relief=GROOVE, border=0, bg=last_line_bg, command=lambda: input_number('+',mad))
    b_plus.pack(side="left", expand=True, fill="both")

    b_minus = tk.Button(l_3, text="-", bg=OP, relief=GROOVE, border=0, command=lambda: input_number('-',mad))
    b_minus.pack(side="left", expand=True, fill="both")

    b_divide = tk.Button(l_4, text="/", bg=OP, relief=GROOVE, border=0,command=lambda: input_number('/',mad))
    b_divide.pack(side="left", expand=True, fill="both")

    b_multiply = tk.Button(l_5, text="*", bg=OP, relief=GROOVE, border=0,command=lambda: input_number('*',mad))
    b_multiply.pack(side="left", expand=True, fill="both")

    b_c = tk.Button(l_6, text="c", relief=GROOVE, border=0, bg=last_line_bg, command=lambda: clear_input_field(mad))
    b_c.pack(side="left", expand=True, fill="both")
    xpo.mainloop()