import random

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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

computer_choice = random.randint(0, 2)

if user_choice == computer_choice:
    result = "Match Draw"
elif user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
    result = "You win!"
else:
    result = "Computer wins!"

if user_choice == 0:
    print(f"You choose: \n{rock}")
elif user_choice == 1:
    print(f"You choose: \n{paper}")
else:
    print(f"You choose: \n{scissors}")

if computer_choice == 0:
    print(f"Computer choose: \n{rock}")
elif computer_choice == 1:
    print(f"Computer choose: \n{paper}")
else:
    print(f"Computer choose: \n{scissors}")

print(result)