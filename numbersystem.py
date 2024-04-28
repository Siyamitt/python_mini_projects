print("Choose the order: \n1. Press A for incresing order\n2. Press b for decresing order.")
order = input("press: ")
if order.capitalize() == "A":
    print("Enter your choice : \n1. Press 1 for rowise. \n2. Press 2 for column wise.")
    choice = int(input("Press : "))
    if choice == 1:
        start = int(input("Enter the starting point of your series :  "))
        end = int(input("Enter Ending point of youre series : "))
        update = int(input("Enter the updation value : "))
        for i in range(start,end+1,update):
            print(i,end= ",")
    
    elif choice == 2:
        start = int(input("enter the starting point of your series : "))
        end = int(input("Enter the ening value of your series : "))
        update = int(input("Enter the updation value of your series : "))
        for i in range(start,end+1,update):
            print(i)
    
    else:
        print("Invalid option.")

elif order.capitalize() == "B":
    print("Enter your choice : \n1. Press 1 for rowise. \n2. Press 2 for column wise.")
    choice = int(input("Press : "))
    if choice == 1:
        start = int(input("Enter the starting point of your series :  "))
        end = int(input("Enter Ending point of youre series : "))
        update = int(input("Enter the updation value : "))
        for i in range(start,end-1,-update):
            print(i,end= ",")
    
    elif choice == 2:
        start = int(input("enter the starting point of your series : "))
        end = int(input("Enter the ening value of your series : "))
        update = int(input("Enter the updation value of your series : "))
        for i in range(start,end-1,-update):
            print(i)
    else:
        print("Invalid Option.")