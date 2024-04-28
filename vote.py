import sys
print("===================================VOTING SYSTEM===================================")
vote_1 = 0
vote_2 = 0
vote_3 = 0
vote_4 = 0

n1 =[]
y = False
while y == False:
    print('''                    Hello        
                  Welcome to Voting system 
      you are setting up a password so that only you can end the voting.
      ''')
    attempts = 0 
    password = input("Enter the password: ")
    while attempts<3:
        password_2 = input("Enter to confirm your password: ")
        if password == password_2:
            print("Ok, You have succesfully set your password.")
            print()
            y = True
            break
        else:
            print("You have entered wrong password please try again.\nYou can enter only ",3-attempts," more Time")
            print()
            attempts+=1
            continue
    else:
        print("As you entered wrong password so many time.\n we are starting the process again.\n")


attempts = 0 
while True:
    Name = input("Enter your Name : ")
    age = int(input("Enter your age : "))
    code = int(input("Enter your code: "))
    if age < 18 :
        print(Name,"You are not eligible to vote. \nTry after",18-age,"Years")
        continue
    elif code in n1 and age>18:
        print("sorry you have alerady voted.")
        print()
        continue
    else:
        print("You are eligible to vote")
        print()
        n1.append(code)

        
    print("There are 4 options to which you can vote.You have to enter Number of party you want to vote. \n1. Bhartiye Janta Party.\n2. Aam Aadmi party. \n3. Congress \n4. No One I want to vote myself.\n5. If you want to end voting. ")
    vote = int(input("Enter the party Number : "))
    if vote == 1:
        print("Are you sure you want to vote Bhartiye Janta Party?")
        while True:
            confirm_1 = input("Enter Y or N : ")
            if confirm_1.capitalize() == "Y":
                print("You have given your vote to Bhartiye janta party.")
                vote_1+=1
                break
            elif confirm_1.capitalize() == "N":
                print("Okay choose again")
                break
            else:
                print("You have Entered Invalid Option.")
                continue
    elif vote == 2:
        print("Are you sure you want to vote Aam Aadmi Party?")
        confirm_1 = input("Enter Y or N : ")
        while True:
            if confirm_1.capitalize() == "Y":
                print("You have given your vote to Aam aadmi party.")
                vote_2+=1
                break
            elif confirm_1.capitalize() == "N":
                print("Okay choose again")
                break
            else:
                print("You have entered wrong option.")
                continue
    elif vote == 3:
        print("Are you sure you want to vote Congress?")
        while True:
            confirm_1 = input("Enter Y or N : ")
            if confirm_1.capitalize() == "Y":
                print("You have given your vote Congress.")
                vote += 1
                break
            elif confirm_1.capitalize() == "N":
                print("Okay choose again")
                break
            else:
                print("You have entered wrong option")
                continue
    elif vote == 4:
        print("Are you sure you want to give your vote to Yourself")
        while True:
            confirm_1 = input("Enter Y or N : ")
            if confirm_1.capitalize() == "Y":
                print("You have given your vote to Yourself.")
                vote_4+=1
                break
            elif confirm_1.capitalize() == "N":
                print("Okay choose again")
                break
            else:
                print("You have entered wrong option.")
    elif vote == 5:
        while attempts <=3:
            user_input_password = input("Enter the password you if you want to end the voting: ")
            if password == user_input_password:
                print("Okay the voting ends here.")
                print("Vote of Bhartiye janta Party are =",vote_1)
                print("Vote of Aam Aadmi party are =",vote_2)
                print("Vote of the Congress are =",vote_3)
                print("vote of yourself are =",vote_4)
                print()
                if vote_1 > vote_2 and vote_1 >vote_3 and vote_1>vote_4:
                    print("BJP won the election.")
                elif vote_2 > vote_3 and vote_2 > vote_4:
                    print("AAP won the election.")
                elif vote_3>vote_4:
                    print("Congress won the election")
                else:
                    print("You won the election.")
                sys.exit()
            else:
                print("Sorry Try again.\nYou can try only",3-attempts," more times")
                attempts+=1
        else:
            print("Sorry your attempts are wrong so we are not ending the vote.")
    else:
        print("Invalid please Try again")
        continue