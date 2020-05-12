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
#Placement des navires de l'IA
computer_tab.init_computer_board(player_ship_list)
computer_tab.print_tab()

#Placement des navires du joueur
element = 0
while element < len(player_ship_list):
  is_good = False
  while is_good == False:
    spot = input("Saisir la position du {} ({} cases) : ".format(player_ship_list[element].name, player_ship_list[element].lenght))
    is_good = player_tab.place_ship(spot, player_ship_list[element])
    if is_good == True:
      element += 1
    player_tab.print_tab()
    if is_good == False:
      print("Saisie incorrecte, réessayez")

win = False
number_of_destroyed = 0
#Boucle de jeu
while win == False:
  #Boucle du joueur
  player_tab.print_tab()
  is_good = False
  while is_good == False:
    player_input = input("Coordonnées de tir : ")
    char, is_good = game_player_tab.play_position(computer_tab.tab, player_input)
    if is_good:
      for element in computer_ship_list:
        if char == element.char:
          element.is_touched()

      game_player_tab.print_tab()
      computer_tab.print_tab()
  ships_remaining = 5
  for element in computer_ship_list:
    if element.get_is_destroyed():
      ships_remaining -= 1
  if ships_remaining == 0:
    win = True
    print("Vous avez Gagné")
    break

  #boucle de l'ordinateur
  is_good = False
  while is_good == False:
    computer_input = random.choice('ABCDEFGHIJ') + str(random.randint(0, 9))
    char, is_good = computer_player_tab.play_position(player_tab.tab, computer_input)
    if is_good:
      for element in player_ship_list:
        if char == element.char:
          element.is_touched()

  ships_remaining = 5
  for element in player_ship_list:
    if element.get_is_destroyed():
      ships_remaining -= 1
  if ships_remaining == 0:
    win = True
    print("L'ordinateur à Gagné")
    break
game_player_tab.print_tab()
computer_player_tab.print_tab()
input()
