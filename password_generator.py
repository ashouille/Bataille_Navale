import string
from random import randint, choice
from tkinter import *

def gen_pass():
    pass_min = 6
    pass_max = 12
    all_char = string.ascii_letters + string.punctuation + string.digits
    
    password = "".join(choice(all_char) for x in range (randint(pass_min, pass_max)))
    input_user.delete(0, END)
    input_user.insert(0, password)
        
    

windows = Tk()
windows.title("MDP generator")
windows.geometry("800x500")
windows.config(background='#688BC2')

frame = Frame(windows, bg='#688BC2')


width = 300
height = 300
image = PhotoImage(file="passkey.png").zoom(1).subsample(2)
canvas = Canvas(frame, width=width, height=width, bg='#688BC2', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg='#688BC2')

label_title = Label(right_frame, text='Mot de passe', font=('Helvetica', 20), bg='#688BC2', fg='white' )
label_title.pack()

input_user = Entry(right_frame, font=('Helvetica', 20), bg='#688BC2', fg='white' )
input_user.pack()

generate_pass_button = Button(right_frame, text='Générer', font=('Helvetica', 20), bg='#688BC2', fg='white', command=gen_pass)
generate_pass_button.pack()

right_frame.grid(row=0, column=1, sticky=W)
frame.pack(expand=YES)

#barre de menu
menu_bar = Menu(windows)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="nouveau", command=gen_pass)
file_menu.add_command(label="Quitter", command=windows.quit)
menu_bar.add_cascade(label="fichier", menu=file_menu)

windows.config(menu=menu_bar)

windows.mainloop()