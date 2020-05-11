import random

class Plateau:

  def __init__(self, size):
    self.size = size
    self.tab = [[" "] * size for element in range(size)]

  def print_tab(self):
    first_line = "  | "
    for number in range(self.size):
          if number >= 10:
            first_line = first_line + str(number) + "| " 
          else:
            first_line = first_line + str(number) + " | " 
    print(first_line)
    
    point_x = 0
    letter = "A"
    while point_x < self.size:
      line = str(letter) + " | " + " | ".join(self.tab[point_x]) + " |"
      point_x += 1
      letter = chr(ord(letter[0]) + 1)
      print(line)
  
  def place_is_valid(self, inp, boat):
    #test si la chaine de caractère d'entrée est valide (forme : B2H par exemple)
    try:
      if ((inp[0].upper() in "ABCDEFGHIJ")  and 0 <= int(inp[1]) <= self.size) and (inp[2].upper() in 'HV'):
        y_pos = ord(inp[0].upper())-65
        x_pos = int(inp[1])
        if inp[2].upper() == 'H':
          horizontal = True
        else:
          horizontal = False
    except ValueError:
      return False
        
    #Test si le bateau placé ne dépasse pas le plateau de jeu et si il n'y a pas de collision
    try:
      if horizontal == True and x_pos + boat.lenght <= self.size:
        temp_str = ""
        cpt = 0
        while cpt < boat.lenght:
          temp_str = temp_str + self.tab[y_pos][x_pos]
          cpt += 1
          x_pos += 1
        if temp_str == " " * boat.lenght:
          return True 
      
      if horizontal == False and y_pos + boat.lenght <= self.size:
        temp_str = ""
        cpt = 0
        while cpt < boat.lenght:
          temp_str = temp_str + self.tab[y_pos][x_pos]
          cpt += 1
          y_pos += 1
        if temp_str == " " * boat.lenght:
          return True 
    except IndexError:
      return False
    else:
      return False

  def place_ship(self, inp, boat):
    #place la bateau après avoir vérifier si la position est valide
    if len(inp) == 3 and self.place_is_valid(inp, boat):
      y_pos = ord(inp[0].upper())-65
      x_pos = int(inp[1])
      horizontal = False
      if inp[2].upper() == 'H':
        horizontal = True
    
      if horizontal:
        element = 0
        while element < boat.lenght:
          self.tab[int(y_pos)][int(x_pos)] = boat.char
          x_pos += 1
          element += 1
      
      if horizontal == False:
        element = 0
        while element < boat.lenght:
          self.tab[int(y_pos)][int(x_pos)] = boat.char
          y_pos += 1
          element += 1
      return True
    else:
      return False

  def init_computer_board(self, boat_list):
    #Installe les navires de l'ordinateur dans son tableau de jeu
    element = 0
    while element < len(boat_list):
      is_good = False
      while is_good == False:
        spot = random.choice('ABCDEFGHIJ') + str(random.randint(0, 9)) + random.choice('HV')
        is_good = self.place_ship(spot, boat_list[element])
        if is_good == True:
          element += 1
  
  def spot_is_valid(self, inp):
    #Teste si la position de tir est valide
    if len(inp) == 2:
      try:
        if ((inp[0].upper() in "ABCDEFGHIJ")  and 0 <= int(inp[1]) <= self.size):
          y_pos = ord(inp[0].upper())-65
          x_pos = int(inp[1])
          return True
      except ValueError:
        return False
    else:
      return False
  
  def play_position(self, computer_tab, inp):
    try:
      y_pos = ord(inp[0].upper())-65
      x_pos = int(inp[1])
      if self.spot_is_valid(inp) and self.tab[y_pos][x_pos] == " ":
        if computer_tab[y_pos][x_pos] in "PCVSR":
          char = computer_tab[y_pos][x_pos]
          computer_tab[y_pos][x_pos] = "T"
          self.tab[y_pos][x_pos] = "T"
          print(y_pos)
          print ("Touché")
          return char, True

        if computer_tab[y_pos][x_pos] == " ":
          self.tab[y_pos][x_pos] = "X"
          print(y_pos)
          print("Dans l'eau")
          return " ", True
      else:
        print("Saisie invalide")
        return " ", False
    except IndexError:
      print("Saisie invalide")
      return " ", False


class Ship:
  def __init__(self, name, lenght, number, char, is_destroyed=False, shot=0):
    self.name = name
    self.lenght = lenght
    self.number = number
    self.char = char
    self.shot = shot
    self.is_destroyed = is_destroyed

  def is_touched(self):
    self.shot += 1
    if self.shot == self.lenght:
      self.is_destroyed = True
      print("{} détruit".format(self.name))
  
  def get_is_destroyed(self):
    return self.is_destroyed