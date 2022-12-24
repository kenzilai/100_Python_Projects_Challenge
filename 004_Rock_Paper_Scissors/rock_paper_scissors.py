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

choice_img = [rock, paper, scissors]
my_choice = int(input("Rock, Paper, Scissors, what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if my_choice >= 3 or my_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You chose:")
    print(choice_img[int(my_choice)])
    
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choice_img[int(computer_choice)])

    if my_choice == 0 and computer_choice == 1:
        print("You lose.")
    elif my_choice == 1 and computer_choice == 2:
        print("You lose.")
    elif my_choice == 2 and computer_choice == 0:
        print("You lose.")

    elif my_choice == 0 and computer_choice == 2:
        print("You win!")
    elif my_choice == 1 and computer_choice == 0:
        print("You win!")
    elif my_choice == 2 and computer_choice == 1:
        print("You win!")
        
    else:
        print("It's a draw.")