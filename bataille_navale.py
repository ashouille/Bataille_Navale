from classes import Plateau, random, Ship, finished

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

player_tab = Plateau(10)
computer_tab = Plateau(10)
game_player_tab = Plateau(10)
computer_player_tab = Plateau(10)

print('Bienvenue dans le jeu de bataille navale')
# Placement des navires de l'IA
computer_tab.init_computer_board(player_ship_list)
computer_tab.print_tab()

# Placement des navires du joueur
element = 0
while element < len(player_ship_list):
    is_good = False
    while not is_good:
        spot = input(
            'Saisir la position du {} ({} cases) : '.format(
                player_ship_list[element].name, player_ship_list[element].lenght
            )
        )
        is_good = player_tab.place_ship(spot, player_ship_list[element])
        if is_good:
            element += 1
        player_tab.print_tab()
        if not is_good:
            print('Saisie incorrecte, réessayez')
    player_tab.print_tab()

win = False
# Boucle de jeu
while not win:
    # Boucle du joueur
    is_good = False
    while not is_good:
        player_tab.print_tab()
        game_player_tab.print_tab()
        player_input = input('Coordonnées de tir : ')
        is_good = game_player_tab.play_position(
            computer_tab.tab, player_input, computer_ship_list
        )
    if finished(computer_ship_list):
        print('Vous avez Gagné')
        break

    # boucle de l'ordinateur
    is_good = False
    while not is_good:
        computer_input = random.choice('ABCDEFGHIJ') + str(random.randint(0, 9))
        is_good = computer_player_tab.play_position(
            player_tab.tab, computer_input, player_ship_list
        )
    if finished(player_ship_list):
        print("L'ordinateur à Gagné")
        break

game_player_tab.print_tab()
computer_player_tab.print_tab()
input()
