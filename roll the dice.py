import random
print('''                WELCOME TO ROLL THE DICE GAME\n
                                INSTRUCTIONS
      1. You have to enter 1 if you want to play else play 2.
      2. After selecting your numbers will be added and computers also.
      3. At last whose calculated number will be greater will be the winner.
      4. You can stop the game whereever you want to stop by entering 7.
      ''')

user_sum = 0
computer_sum = 0
total_times = 0
while True:
    user_choice = random.randint(1,6)
    computer_choice = random.randint(1,6)
    choice = int(input("Enter 1 if you want to play or enter 2 if you want to end it : "))
    if choice == 1:
        print("computer choice :",computer_choice,"\nYour choice = ",user_choice)
        user_sum += user_choice
        computer_sum += computer_choice
        total_times+=1
    elif choice == 2:
        print("Okay you have ended the game.")
        print()
        print(f"     Final Results        ")
        print(f"your total = {user_sum}\ncomputer sum = {computer_sum}\n")
        if user_sum > computer_sum:
            print("You have won the game")
        elif computer_sum > user_sum:
            print("sorry you loose this game")
        else:
            print("Its a tie")
        break
    else:
        print("Invalid number.\nEnter again")
        print()
        

