import webbrowser
from tkinter import Button
from tkinter import Frame
from tkinter import Label
from tkinter import SUNKEN
from tkinter import Tk


def test_link():
    webbrowser.open_new_tab("https://www.google.fr")


window = Tk()

window.title("Bataille Navale")
window.geometry("1024x768")
window.minsize(1024, 768)
window.iconbitmap("logo.ico")
window.config(background="#6E7785")

frame = Frame(window, bg="#6E7785", bd=1, relief=SUNKEN)

label_title = Label(frame, text="Bataille Navale", font=("Helvetica", 40), bg="#6E7785")
label_title.pack()

label_subtitle = Label(frame, text="Bienvenue", font=("Helvetica", 25), bg="#6E7785")
label_subtitle.pack()

button = Button(
    frame,
    text="Commencer à jouer",
    font=("Helvetica", 25),
    bg="#6E7785",
    fg="white",
    command=test_link,
)
#  button.pack(pady=25, fill=X) que vaut X
frame.pack(expand=True)

window.mainloop()
