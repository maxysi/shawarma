import tkinter
from tkinter import *
Window = tkinter.Tk()
Window.geometry("300x200")
Window.title("Табличні величини")
lbl = Label(Window, text="Введіть список значень:")
lbl.place(x=120,y=240)
text = Text(Window, height=5, width=42, bg="white",font=("Arial 11"))
text.place(x=0,y=70)
frame=Frame(Window,bd=0.5,relief="solid")
frame.place(x=5,y=200)
def Start(event):
    inputList = text.get(0.0,tkinter.END)
    outputList = []
    for i in range(len(inputList) -1,-1,-1):
        if inputList[i] > chr(47) and inputList[i] < chr(58):
            outputList.append(inputList[i])
            for i in range(len(outputList)):
                label1 = Label(frame, text=outputList[i]).grid(row=0, column=i)
            btn=Button(Window, text="Виконати", command=Start)
            btn.place(x=5,y=300)