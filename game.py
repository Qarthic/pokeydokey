
import sys
sys.path.append("pokeydokey\data")

from data import pokemon_rules


pokedex = pokemon_rules.extract_from_file("pokedex.csv")

print(pokedex)