from tkinter import *
import parser


fontL = ('Verdana', 20)

#   Window root
root = Tk()
root.title("Calculadora")
#   WidthxHeight
root.geometry("345x275")    #   Measure when opened
root.minsize(345, 275)      #   Minimum size
root.maxsize(345, 275)      #   Maximum measure
#   Window color
root.configure(background= "gray15")


#   Display
display = Entry(root, font=fontL)
display.grid(row=1, column=0, columnspan=6, sticky=E+W)

#   Label
Label(root, font=fontL, bg= "gray15").grid(row=2, column=0, columnspan=6, sticky=E+W)


#   Functions

i = 0

def getNumbers(n):
    global i
    display.insert(i, n)
    i+=1

def getOperations(operator):
    global i
    operatorLen = len(operator)
    display.insert(i, operator)
    i+=operatorLen

def clearDisplay():
    display.delete(0, END)

def undo():
    displayState = display.get()
    if(displayState == "ERROR"):
        clearDisplay()
    elif(displayState):
        displayNewState = displayState[:-1]
        clearDisplay()
        display.insert(0, displayNewState)
    else:
        clearDisplay()
        display.insert(0, "ERROR")

def calculate():
    displayState = display.get()
    try:
        mathExpression = parser.expr(displayState).compile()
        result = eval(mathExpression)
        clearDisplay()
        display.insert(0, result)
    except Exception:
        clearDisplay()
        display.insert(0, "ERROR")

def salir():
    root.destroy()


#   Numeric Buttons
Button(root, text="1", command=lambda: getNumbers(1)).grid(row=3, column=0, sticky=E+W)
Button(root, text="2", command=lambda: getNumbers(2)).grid(row=3, column=1, sticky=E+W)
Button(root, text="3", command=lambda: getNumbers(3)).grid(row=3, column=2, sticky=E+W)

Button(root, text="4", command=lambda: getNumbers(4)).grid(row=4, column=0, sticky=E+W)
Button(root, text="5", command=lambda: getNumbers(5)).grid(row=4, column=1, sticky=E+W)
Button(root, text="6", command=lambda: getNumbers(6)).grid(row=4, column=2, sticky=E+W)

Button(root, text="7", command=lambda: getNumbers(7)).grid(row=5, column=0, sticky=E+W)
Button(root, text="8", command=lambda: getNumbers(8)).grid(row=5, column=1, sticky=E+W)
Button(root, text="9", command=lambda: getNumbers(9)).grid(row=5, column=2, sticky=E+W)

#   Operation Buttons
Button(root, text="AC", command=lambda: clearDisplay(), bg= "orange").grid(row=6, column=0, sticky=E+W)
Button(root, text="0", command=lambda: getNumbers(0)).grid(row=6, column=1, sticky=E+W)
Button(root, text="%", command=lambda: getOperations("%")).grid(row=6, column=2, sticky=E+W)

Button(root, text="+", command=lambda: getOperations("+")).grid(row=3, column=3, sticky=E+W)
Button(root, text="-", command=lambda: getOperations("-")).grid(row=4, column=3, sticky=E+W)
Button(root, text="*", command=lambda: getOperations("*")).grid(row=5, column=3, sticky=E+W)
Button(root, text="/", command=lambda: getOperations("/")).grid(row=6, column=3, sticky=E+W)

Button(root, text="🠔", command=lambda: undo()).grid(row=3, column=4, sticky=E+W, columnspan=2)
Button(root, text="exp", command=lambda: getOperations("**")).grid(row=5, column=4, sticky=E+W)
Button(root, text="^2", command=lambda: getOperations("**2")).grid(row=5, column=5, sticky=E+W)
Button(root, text="(", command=lambda: getOperations("(")).grid(row=4, column=4, sticky=E+W)
Button(root, text=")", command=lambda: getOperations(")")).grid(row=4, column=5, sticky=E+W)
Button(root, text="=", command=lambda: calculate()).grid(row=6, column=4, sticky=E+W, columnspan=2)

Label(root, font=fontL, bg= "gray15").grid(row=7, column=0, columnspan=6, sticky=E+W)

Button(root, text="Salir", command=lambda: salir(), bg="red", fg="white").grid(row=8, column=4, sticky=E+W, columnspan=2)


root.mainloop()