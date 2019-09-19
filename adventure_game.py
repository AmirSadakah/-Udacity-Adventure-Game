import random
from time import *


def attack(weapon):
    print(f"The {enemy} attacks you!")
    sleep(1)
    if weapon == "dagger":
        print(
            f"You feel a bit under-prepared for this, what with only having a tiny {weapon}.")
        sleep(1)
    choice = input("Would you like to (1) fight or (2) run away?")
    if choice == '1':
        if weapon == "dagger":
            print("You do your best...")
            sleep(1)
            print(f"but your {weapon} is no match for the {enemy}.")
            sleep(1)
            print("You have been defeated!""")
            sleep(1)
        elif weapon == "sword":
            print(
                f"As the {enemy} moves to attack, you unsheath your new sword.")
            sleep(1)
            print(
                "The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
            sleep(2)
            print(
                f"But the {enemy} takes one look at your shiny new toy and runs away!")
            sleep(2)
            print(f"You have rid the town of the {enemy}. You are victorious!")
            sleep(2)
    elif choice == '2':
        print("You run back into the field. Luckily, you don't seem to have been followed.")
        sleep(2)
        where_to()


def play_again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'n':
            print("Thanks for playing! See you next time.")
            sleep(2)
            return 'game_over'
        elif choice == 'y':
            print("Excellent! Restarting the game ...")
            sleep(2)
            weapon = 'dagger'
            return 'running'


def where_to():
    print("  ")
    print("Enter 1 to knock on the door of the house.")
    sleep(2)
    print("Enter 2 to peer into the cave.")
    sleep(2)
    print("What would you like to do?")
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")

    if choice == '1':
        house()
    elif choice == '2':
        cave()


def house():
    print("You approach the door of the house.")
    sleep(2)
    print(
        f"You are about to knock when the door opens and out steps a {enemy}.")
    sleep(2)
    print(f"Eep! This is the {enemy}'s house!")
    sleep(2)
    attack(weapon)


def cave():
    global cave_visited
    global weapon
    print("You peer cautiously into the cave.")
    sleep(2)
    if cave_visited:
        print("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        sleep(1)
    elif cave_visited is False:
        print("It turns out to be only a very small cave.")
        sleep(1)
        print("Your eye catches a glint of metal behind a rock.")
        sleep(1)
        print("You have found the magical Sword of Ogoroth!")
        sleep(1)
        print(
            f"You discard your silly old {weapon} and take the sword with you.")
        sleep(1)
        weapon = "sword"
    cave_visited = True
    print("You walk back out to the field.")
    sleep(2)
    where_to()


game_state = 'running'
while game_state == 'running':

    enemies = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
    enemy = random.choice(enemies)
    weapon = 'dagger'
    cave_visited = False
    print("""
   __   ____ _  _ ____ _  _ ____ __  __ ____ ____     ___   __   __  __ ____ 
  /__\ (  _ ( \/ | ___| \( |_  _|  )(  |  _ ( ___)   / __) /__\ (  \/  | ___)
 /(__)\ )(_) )  / )__) )  (  )(  )(__)( )   /)__)   ( (_-./(__)\ )    ( )__)          
(__)(__|____/ \/ (____|_)\_)(__)(______|_)\_|____)   \___(__)(__|_/\/\_|____)
                        __________________________
                       |OFFo oON                  |
                       | .----------------------. |
                       | |  .----------------.  | |
                       | |  |                |  | |
                       | |))|                |  | |
                       | |  |                |  | |
                       | |  |                |  | |
                       | |  |                |  | |
                       | |  |                |  | |
                       | |  |                |  | |
                       | |  '----------------'  | |
                       | |__GAME BOY____________/ |
                       |          ________        |
                       |    .      (Amir)         |
                       |  _| |_   """"""""   .-.  |
                       |-[_   _]-       .-. (   ) |
                       |   |_|         (   ) '-'  |
                       |    '           '-'   A   |
                       |                 B        |
                       |          ___   ___       |
                       |         (___) (___)  ,., |
                       |        select start ;:;: |
                       |                    ,;:;' /
                       |                   ,:;:'.'
                       '-----------------------`
      """)
    print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    sleep(2)
    print(
        f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.")
    sleep(2)
    print("In front of you is a house.")
    sleep(2)
    print("To your right is a dark cave.")
    sleep(2)
    print(
        f"In your hand you hold your trusty (but not very effective) {weapon}.")
    sleep(2)
    where_to()

    game_state = play_again()
