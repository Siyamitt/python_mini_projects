def evaluate_values(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error : {str(e)}"

while True:
    expression = input("Enter to calculate or ('exit' to quit) : ")
    if expression.lower() == "exit":
        print("GoodBye!")
        break
    result = evaluate_values(expression)
    print(f"Result: {result}" )