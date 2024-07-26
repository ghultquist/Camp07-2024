import random

def flight():
    print()

def fight():
    print("______________________________________________")
    choice = input("You look around for a weapon... \n1.baseball bat \n2.axe \n3.your fists \nChoice: ")
    if choice == "1":
        print("You grip the bat with shaky hands and swing... The bat connects with the undead's head and sends them falling to the ground.")
    elif choice == "2":
        print("You pick up the axe confidently. You've seen a million zombie movies, so you know how to handle these things.\nYou pull the weapon back and swing forward, burying the axe into the undead's shoulder. You realize this is a critical miss when the blade is stuck.")
        print("As you struggle, the zombie lunges forward and bites into your shoulder.\nTHE END")
    elif choice == "3":
        print("")

def check_sound():
    print("______________________________________________")
    print("You follow the sound to see a zombie.")
    choice = input("What do you do? \n1.Fight \n2.Run \nChoice:")
    if choice == "1":
        print("You decide to stand your ground and fight!")
        fight()
    elif choice == "2":
        print("Between fight or flight, like a bird you fly.")
        flight()
    else:
        print("That's not an option!")
        check_sound()
    


def ignore_sound():
    print("______________________________________________")
    luck = random.randint(1,3)
    if luck == 1:
        print("You get engrossed in the film. Just as the movie reaches its climax, you hear a groan to your right.\nYou turn your head just in time to see the decaying face of a zombie as you feel a sharp bite into your shoulder.")
        print("The film plays on without you... \nTHE END")
    elif luck == 2:
        print("You get engrossed in the film. Just as the movie reaches its climax, you hear a groan to your right.\nYou turn your head to see your neighbor, Fred, zombified, ")
        print("You got to enjoy every second of the movie!\nTHE END")
    elif luck == 3:
        print("You hear another sound and are compelled to see what's going on.")
        check_sound()


def start():
    print("______________________________________________")
    print("Ough... It sure has been a long week... \nI bet you are excited to sit back and watch a good old fashioned horror film!")
    print("\nAs the monster emerges from the lake on the screen, you think you hear a crash from your kitchen.")
    choice = input("\nWhat do you do? \n1. Pause movie and approach the kitchen... \n2. Ignore. It was probably just the movie. \nChoice: ")
    if choice == "1":
        print("You steel your nerves and move towards the sounds...")
        check_sound()
    elif choice == "2":
        print("You shrug off the disturbance and focus on the flick.")
        ignore_sound()
    else:
        print("That's not an option!")
        start()

    

def main():
    print("WELCOME TO ZOMBIE CINEMA! \nPress enter to start your movie!")
    input()
    start()

main()
