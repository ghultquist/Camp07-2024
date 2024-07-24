'''Cast input into integer
#age = int(input("What is your age? "))
#print(" You will be " + str(age + 37) + " in 37 years!")

#Create a simple calculator that asks for 2 numbers & adds them together

'''

'''temp = int(input("Temperature please: "))
weather = input("Weather conditions (clear, cloudy, rainy, snow, and crazy): ")

if weather == "rainy":
    print("Grab an umbrella on your way out!")
elif weather == "crazy":
    print("Take precautions & PLEASE be safe...")
elif temp > 90 and weather == "clear":
    print("HOT grab LOTS of water and sunscreen!")
elif temp >90 and weather == "cloudy":
    print("Still stay hydrated, but enjoy the shade")
elif temp < 30:
    print("COLD stay inside!!!")
else:
    print("Enjoy the weather!")'''






















import random

num = random.randint(1, 8)
question = input("What is your question for the mystical magic 8-ball?")

if num == 1:
    print("Yes!")
elif num == 2:
    print("Nope!")
elif num == 3:
    print("Probably!")
elif num == 4:
    print("I don't think so...")
elif num == 5:
    print("I'm not sure!")
elif num == 6:
    print("You should hope not...")
elif num == 7:
    print("If you're feeling lucky!")
elif num == 8:
    print("try again later :/")
