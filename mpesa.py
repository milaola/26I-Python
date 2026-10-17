def deposit(username, amt):
    balance = 0
    balance += amt
    print(f"Hello, {username} your new balance is {balance}")
    

try:
    user = input ("Enter your usename:")
    amount = int (input("Enter the amount to deposit:"))
    deposit ( user, amount)
except:
    print ("Invalid input")



