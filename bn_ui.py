from classes import Plateau, random, Ship, finished
from tkinter import *

porte_avions_player = Ship('Porte-Avions', 5, 'P')
croiseur_player = Ship('Croiseur', 4, 'C')
contre_torpilleur_player = Ship('Contre-torpilleur', 3, 'V')
sous_marin_player = Ship('Sous-marin', 3, 'S')
torpilleur_player = Ship('Torpilleur', 2, 'R')

porte_avions_computer = Ship('Porte-Avions', 5, 'P')
croiseur_computer = Ship('Croiseur', 4, 'C')
contre_torpilleur_computer = Ship('Contre-torpilleur', 3, 'V')
sous_marin_computer = Ship('Sous-marin', 3, 'S')
torpilleur_computer = Ship('Torpilleur', 2, 'R')

player_ship_list = [
    porte_avions_player,
    croiseur_player,
    contre_torpilleur_player,
    sous_marin_player,
    torpilleur_player,
]
computer_ship_list = [
    porte_avions_computer,
    croiseur_computer,
    contre_torpilleur_computer,
    sous_marin_computer,
    torpilleur_computer,
]
spot = ''

COTE = 60
PAD = 5
SIDE = COTE + 2 * PAD

LIG = COL = 10

LARG = COL*SIDE
HAUT = LIG*SIDE
X0=Y0=SIDE//2

player_tab = Plateau(10)
computer_tab = Plateau(10)
game_player_tab = Plateau(10)
computer_player_tab = Plateau(10)

computer_tab.init_computer_board(player_ship_list)

def afficher_plateau(plateau):
    ids_cover=[]
    for ligne in range(LIG):
        L=[]
        for col in range(COL):
            centre = (col*SIDE + X0,ligne*SIDE + Y0)
            sea = PhotoImage(file="sea.png")
            id_cover = cnv.create_image(centre, image=sea)
            L.append(id_cover)
        ids_cover.append(L)
    return ids_cover

window = Tk()

window.title('Bataille Navale')
window.geometry('1024x768')
window.minsize(1024, 768)
window.iconbitmap('logo.ico')
window.config(background='#6E7785')

frame = Frame(window, bg='#6E7785', bd=1, relief=SUNKEN)

cnv = Canvas(window, width=LARG, height=HAUT, bg="grey")
afficher_plateau(computer_tab)
cnv.pack(side=LEFT)

window.mainloop()
