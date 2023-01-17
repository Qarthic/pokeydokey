
import sys
sys.path.append("pokeydokey\data")
import random
import choose_mon as choose

from dex_data import mon_rules as mr
from time import sleep

def mon_battle():
    player_mon = choose.player_pick_mon()
    com_mon = choose.computer_pick_mon()

    print(player_mon.name)

    print(com_mon.name)

mon_battle()