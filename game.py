# Creating a personal Pokemon game with Charmander, Squirtle and Bulbasaur 
from data import moves, pokedex

def start_game():
  player1 = ""
  choice = input("Who would you like to play as?\n1. Bulbasaur\n2. Charmander\n3. Squirtle")
  if int(choice) == 1:
    player1 = pokedex.Bulbasaur
  if int(choice) == 2:
    player1 = pokedex.Charmander
  if int(choice) == 3:
    player1 = pokedex.Squirtle
  print(player1.name)


