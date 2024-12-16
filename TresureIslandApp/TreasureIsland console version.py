import sys

def start_game():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` ",__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    user_name = input("What is your name?\n").strip()
    print(f"Hello {user_name}. Welcome to Lalaworld.")
    
    choose_key()

def choose_key():
    print("You stumbled upon a box with three keys: Scarlet, Emerald, and Golden. Each key has special powers.")
    key_choice = input("Which key do you choose? Scarlet, Emerald, or Golden?\n").strip().lower()

    if key_choice == "scarlet":
        scarlet_key_storyline(key_choice)
    elif key_choice == "emerald":
        emerald_key_storyline(key_choice)
    elif key_choice == "golden":
        print("You've been struck by lightning and died. Game Over!")
        play_again()
    else:
        print("Invalid choice. The End.")
        play_again()

def scarlet_key_storyline(key):
    print("\"Thanks for choosing me. I am Scarlet, your helper.\" she said. \"Welcome to Volcano, the heart of the forest.\"")
    river_choice = input("You find yourself in front of a river. Do you want to wait for a boat or swim? (wait/swim)\n").strip().lower()

    if river_choice == "swim":
        print("You were eaten by hidden piranhas. Game Over!")
        play_again()
    elif river_choice == "wait":
        print("You waited for Scarlet to return under a tree nearby. Hours passed by and you fell asleep. You woke up at the voice of Scarlet calling your name.")
        print("\"Thanks for patiently waiting. Here's a scroll containing the secret password.\"")
        print("\"I am the bravest at heart\"")
        fairyland_storyline(key)
    else:
        print("Invalid choice. The End.")
        play_again()

def emerald_key_storyline(key):
    print("\"Ho ho ho! I am Tino, your helper. Welcome to the Forbidden Forest.\"")
    direction_choice = input("You come to a fork in the road. Do you go left or right? (l/r)\n").strip().lower()

    if direction_choice == "r":
        fairyland_storyline(key)
    elif direction_choice == "l":
        print("You encounter hungry vampires who take your key and leave you lost. Game Over!")
        play_again()
    else:
        print("Invalid choice. The End.")
        play_again()

def fairyland_storyline(key):
    print("Welcome to Fairyland. You need a password to enter.")
    password = input("What is the password?\n").strip()
    if password.lower() == "i am the bravest at heart":
        print("You may enter.")
        lion_encounter(key)
    else:
        print("Wrong password. Arrows fire at you. Game Over!")
        play_again()

def lion_encounter(key):
    print("You encountered a lion guarding the entrance to a cave.")
    has_key = input("Do you have the key? (y/n)\n").strip().lower()

    if has_key == "y":
        if key == "scarlet":
            print("The lion allows you to pass but you encounter a ferocious Taurus and die. Game Over!")
        elif key == "emerald":
            print("The lion guides you to the treasure. YOU WIN! Congratulations!")
        else:
            print("Invalid key. The lion eats you. Game Over!")
    else:
        print("The lion eats you. Game Over!")
    play_again()

def play_again():
    replay = input("Do you want to play again? (yes/no)\n").strip().lower()
    if replay == "yes":
        start_game()
    else:
        print("Thanks for playing. Goodbye!")
        sys.exit()

# Start the game
start_game()
