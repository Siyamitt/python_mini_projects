import random

option = ("rock","paper","scissor")
comp_win = 0
player_win = 0

while True:
    print(
        '''
        Enter 1 for rock.
        Enter 2 for paper.
        Enter 3 for scissor
        Enter 4 for Exit.
        ''')
    
    computer = random.choice(option)
    print()
    player = int(input("Enter your choice : "))
    print()
    if player > 4:
        print("Invalid Number.")
        continue
    elif player == 4:
        print(f"your score : {player_win}\ncomputer score : {comp_win}")
        print()
        if comp_win  > player_win:
            print("OOPs, computer have won it.")
        elif player_win>comp_win:
            print("Yay! you winned it")
        else:
            print("its a tie.")
        break
    else:
        
        if player == 1 and computer == "paper":
            print(f"computer VS player")
            print(f"{computer} VS rock")
            print(computer," wins!")
            print()
            comp_win+=1
        elif player == 1 and computer == "scissor":
            print(f"computer VS player")
            print(f"{computer} VS rock")
            print("rock wins!")
            print()
            player_win+=1
        elif player == 2 and computer  == "rock":
            print(f"computer VS player")
            print(f"{computer} VS paper")
            print("paper wins!")
            print()
            player_win+=1
        elif player == 2 and computer == "scissor":
            print(f"computer VS player")
            print(f"{computer} VS paper")
            print("scissor wins!")
            print()
            comp_win+=1
        elif player == 3 and computer == "rock":
            print(f"computer VS player")
            print(f"{computer} VS scissor")
            print("rock")
            print()
            comp_win+=1
        elif player == 3 and computer == "paper":
            print(f"computer VS player")
            print(f"{computer} VS Scissor")
            print("scissor wins! ")
            print()
            player_win+=1
            
        else:
            print(f"computer VS player")
            print(f"{computer} VS {computer}")
            print("Its tie.")
        print()
        print(f"Your current score : {player_win}\nComputer current score : {comp_win}")
        print()
        if comp_win > player_win:
            print("computer is winning")
        elif player_win> comp_win:
            print("you are winning")
        else:
            print("Game is Tieing.")
        print()



    

