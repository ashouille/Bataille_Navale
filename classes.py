import random


def has_won(tab):
    ships_remaining = 5
    for element in tab:
        if element.is_destroyed:
            ships_remaining -= 1
    if ships_remaining == 0:
        return True
    return False


class Plateau:
    def __init__(self, size):
        self.size = size
        self.tab = [[' '] * size for _ in range(size)]
        self.x_pos = 0
        self.y_pos = 0
        self.horizontal = False

    def print_tab(self):
        first_line = '  | '
        for number in range(self.size):
            if number >= 10:
                first_line = first_line + str(number) + '| '
            else:
                first_line = first_line + str(number) + ' | '
        print(first_line)

        point_x = 0
        letter = 'A'
        while point_x < self.size:
            line = str(letter) + ' | ' + ' | '.join(self.tab[point_x]) + ' |'
            point_x += 1
            letter = chr(ord(letter[0]) + 1)
            print(line)

    def _place_is_valid(self, inp, boat):

        # Test si la chaine de caractère d'entrée est valide (forme : B2H par exemple)
        # Si True, defini les variables x_pos, y_pos et horizontal
        if (
                len(inp) == 3
                and inp[0].upper() in 'ABCDEFGHIJ'
                and inp[1].isdigit()
                and inp[2].upper() in 'HV'
        ):
            self.y_pos = ord(inp[0].upper()) - 65
            self.x_pos = int(inp[1])
            self.horizontal = False
            if inp[2].upper() == 'H':
                self.horizontal = True
        else:
            return False

        # Si la taille du navire dépasse du plateau, retourne False
        if (self.horizontal and self.x_pos + boat.lenght >= self.size or
            not self.horizontal and self.y_pos + boat.lenght >= self.size
        ):
            return False

        # Pour chaque coordonnée du navire, ajoute les caractère haut, bas
        # gauche et droite dans ship_around
        ship_around = ''
        for elt in range(boat.lenght):

            if self.horizontal:
                temp_x = self.x_pos + elt
                temp_y = self.y_pos

            if not self.horizontal:
                temp_y = self.y_pos + elt
                temp_x = self.x_pos

            if temp_x - 1 >= 0:
                ship_around += self.tab[temp_y][temp_x - 1]
            if temp_x + 1 < self.size:
                ship_around += self.tab[temp_y][temp_x + 1]

            if temp_y - 1 >= 0:
                ship_around += self.tab[temp_y - 1][temp_x]
            if temp_y + 1 < self.size:
                ship_around += self.tab[temp_y + 1][temp_x]

        # Si aucun caractère n'est trouvé dans ship_around, retourne True
        for element in 'PCVSR':
            if element in ship_around:
                return False
        return True

    def place_ship(self, inp, boat):
        # place la bateau après avoir vérifier si la position est valide
        if self._place_is_valid(inp, boat):
            if self.horizontal:
                for element in range(boat.lenght):
                    self.tab[self.y_pos][self.x_pos + element] = boat.char
            if not self.horizontal:
                for element in range(boat.lenght):
                    self.tab[self.y_pos + element][self.x_pos] = boat.char
            return True
        return False

    def init_computer_board(self, boat_list):
        # Installe les navires de l'ordinateur dans son tableau de jeu
        element = 0
        while element < len(boat_list):
            is_good = False
            while not is_good:
                spot = (
                        random.choice('ABCDEFGHIJ')
                        + str(random.randint(0, 9))
                        + random.choice('HV')
                )
                is_good = self.place_ship(spot, boat_list[element])
                if is_good:
                    element += 1

    def _spot_is_valid(self, inp):
        # Teste si la position de tir est valide
        if len(inp) == 2:
            if (inp[0].upper() in 'ABCDEFGHIJ'
                    and inp[1].isdigit()
                    and self.tab[self.y_pos][self.x_pos] == ' '
            ):
                self.y_pos = ord(inp[0].upper()) - 65
                self.x_pos = int(inp[1])
                return True
        return False

    def play_position(self, computer_tab, inp):
        if self._spot_is_valid(inp):
            if computer_tab[self.y_pos][self.x_pos] in 'PCVSR':
                char = computer_tab[self.y_pos][self.x_pos]
                computer_tab[self.y_pos][self.x_pos] = 'T'
                self.tab[self.y_pos][self.x_pos] = 'T'
                print('Touché !')
                return char, True

            if computer_tab[self.y_pos][self.x_pos] == ' ':
                self.tab[self.y_pos][self.x_pos] = 'X'
                print("Dans l'eau !")
                return ' ', True
        print('Saisie invalide')
        return ' ', False

class Ship:
    def __init__(self, name, lenght, char, number=0, is_destroyed=False, shot=0):
        self.name = name
        self.lenght = lenght
        self.char = char
        self.number = number
        self.shot = shot
        self.is_destroyed = is_destroyed

    def is_touched(self):
        self.shot += 1
        if self.shot == self.lenght:
            self.is_destroyed = True
            print(f'Vous avez coulé le {self.name} adverse !')

    def get_is_destroyed(self):
        return self.is_destroyed
