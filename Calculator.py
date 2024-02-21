from math import *
import tkinter

def clicked(event):
    button_name = event.widget.cget("text")
    if button_name == "Clear":
        text.set("")
    elif button_name == "Cut":
        if text.get() == "Error":
            text.set("")
        else:
            text.set(text.get()[0 : -1])
    elif button_name == "=":
        old_text = text.get()
        if old_text != "":
            if "**" in old_text or "//" in old_text:
                text.set("Error")
            else:
                while "!" in old_text:
                    position = old_text.find("!")
                    old_text = old_text[: position] + ")" + old_text[position + 1 :]
                    for i in range(position, -1, -1):
                        if old_text[i] in ["+", "-", "*", "/", "^"]:
                            old_text = old_text[: i + 1] + "factorial(" + old_text[i + 1 :]
                            break
                    if i == 0:
                        old_text = "factorial(" + old_text
                try:
                    text.set(eval(old_text.replace("^", "**")))
                except:
                    text.set("Error")
    else:
        if text.get() == "Error":
            text.set("")
        text.set(text.get() + button_name)

window = tkinter.Tk()
window.title("Calculator")
window.geometry("+520+130")
window.resizable("False", "False")
window.call("wm", "iconphoto", window._w, tkinter.PhotoImage(file = "Calculator.png"))
text = tkinter.StringVar()
screen = tkinter.Entry(window, textvariable = text, width = 30, font = ("Calibiri", 23))
screen.grid(row = 0, column = 0, columnspan = 8)
button_list = ["7", "8", "9", "/", "(", "log10", "log", "Clear",
               "4", "5", "6", "*", ")", "sin", "sinh", "Cut",
               "1", "2", "3", "-", "^", "cos", "cosh", "e",
               ".", "0", "=", "+", "!", "tan", "tanh", "pi"]
for i in range(0, 32):
    button = tkinter.Button(window, text = button_list[i], width = 6, height = 3)
    button.config(font = ("Calibiri", 11), fg = "black", bg = "grey")
    button.bind("<Button-1>", clicked)
    button.grid(row = i // 8 + 1, column = i % 8)
window.mainloop()