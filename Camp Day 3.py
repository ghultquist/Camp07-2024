import random

num = random.randint(1,20)
#print(num)


#FOR LOOP --> range(stop) -- range(start, stop) -- range(start, stop, step)
for i in range(0, 10, 2):
    print(i)


#WHILE LOOP
x = 10
while x < 20:
    print("Monkey Time!")
    x += 1

play = input("Would you like to play?")
while play == "yes" and x == 21:
    print("yay!")
    play = input("WOuld you like to continue?")
