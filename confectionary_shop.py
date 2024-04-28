menu = {"mango":50,
     "apple":65,
     'dairymilk':20,
     "maggie":10,
     "biscuit":10,
     "tea":40,
     "faluda malai mar ke ":45,
     "iphone":150000,
     "mango sack":45,
     "musammi":50  }
amount = int(input("enter your amount : "))
print(menu)
selected_products = {}
buying_products = int(input("how many product you want to buy : "))

i = 1

while i<=buying_products :
    item = input("enter your buying product : ").lower().strip()
       
    item_qun = int(input("enter your quantity : "))    
    selected_products[item] = item_qun
    i+=1
    # print("the products you are buying are : \n",selected_products)  #have to be correct       
            
more = input("do you want to add more (y/n): ")

t= 1
if more == "y":
    buying_p = int(input("how many more products do you want to buy : "))
    while t <= buying_p:
        item = input("enter your buying product : ").lower().strip()
        item_qun = int(input("enter your quantity : "))
        selected_products[item] = item_qun
        t+=1

sum = 0   
print("products you are buying : ",selected_products)
for k1,v1 in selected_products.items():
    total = 0 
    total = total + menu[k1]*v1
    print(k1,":",total)
    sum = sum + menu[k1]*v1
print("total amount is : ",sum)
print('rest amount in card : ',amount-sum)
    


                
    

