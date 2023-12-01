rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
if choice == 0:
    print("\nYou Chose ROCK\n")
    print(rock)
elif choice == 1:
    print("\nYou Chose PAPER\n")
    print(paper)
elif choice == 2:
    print("\nYou Chose SCISSORS\n")
    print(scissors)
else:
    print("You Choose invalid number...!")

    
print ("Computer Chose:")

import random
random_number = random.randint(0,2)
if random_number == 0:
    print("ROCK\n")
    print(rock)
elif random_number == 1:
    print("PAPER\n")
    print(paper)
else:
    print("SCISSORS\n")
    print(scissors)

if choice == random_number:
    print("It's a draw...!")
elif(choice == 0 and random_number == 2) or (choice == 1 and random_number == 0) or (choice == 2 and random_number == 1):
    print("You Win...!")
elif(choice == 0 and random_number==1) or (choice == 1 and random_number == 2) or (choice == 2 and random_number == 0):
    print("Computer Won...!")
else: 
    print("You typed an invalid number, you lost...!")