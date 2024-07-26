import random

#LISTS
'''animals = ["cat", "elephant", "gorilla", "tarantula"]
print(animals)
print(animals[1])
for animal in animals:
    print(animal)'''

#--------------------------------
num = random.randint(2,11)

questions = [
    "What is speed with direction called in physics? ",
    "Name a primary color: ",
    "What is the square root of " + str(num * num) + "?",
    "What is the animal Mei Lee turns into in the film Turning Red?",
    "What color are the flying pikmin in Pikmin?",
    "What country has a canal that connects the Pacific Ocean and the Atlantic Ocean?",
    "What is the classic Mario Kart map that features roaming cows and rolling hills?",
    "Name a cephalopod: "
    ]
answers = [
    "velocity",
    "red, yellow, or blue",
    str(num),
    "red panda",
    "pink",
    "Panama",
    "Moo Moo Meadows",
    "squid, octopus, nautilus, or cuttlefish"]

score = 0

students = ["Avy", "Gabe", "Owen", "Leland"]

for i in range(4):
    choice = random.choice(students)
    print(choice)
    students.remove(choice)


for i in range(len(questions)):
    print(questions[i])
    guess = input("Answer: ")
    answer = answers[i]
    if guess.lower() in answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print("The answer was " + answers[i] + "\n")
        
print("You got " + str(score) + " out of " + str(len(questions)) + "!")










