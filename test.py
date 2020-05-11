from classes import *

porte_avions_player = Ship("Porte-Avions", 5, 1, "P")
croiseur_player = Ship("Croiseur", 4, 1, "C")
contre_torpilleur_player = Ship("Contre-torpilleur", 3, 1, "V")
sous_marin_player = Ship("Sous-marin", 3, 1, "S")
torpilleur_player = Ship("Torpilleur", 2, 1, "R")

porte_avions_computer = Ship("Porte-Avions", 5, 1, "P")
croiseur_computer = Ship("Croiseur", 4, 1, "C")
contre_torpilleur_computer = Ship("Contre-torpilleur", 3, 1, "V")
sous_marin_computer = Ship("Sous-marin", 3, 1, "S")
torpilleur_computer = Ship("Torpilleur", 2, 1, "R")

player_ship_list = [porte_avions_player, croiseur_player, contre_torpilleur_player, sous_marin_player, torpilleur_player]
computer_ship_list = [porte_avions_computer, croiseur_computer, contre_torpilleur_computer, sous_marin_computer, torpilleur_computer]
spot = ""

player_tab = Plateau(10)
computer_tab = Plateau(10)
game_player_tab = Plateau(10)
computer_player_tab = Plateau(10)

print("Bienvenue dans le jeu de bataille navale")
computer_tab.init_computer_board(player_ship_list)
computer_tab.print_tab()