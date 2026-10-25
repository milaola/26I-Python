import random 

difficulty = input ("Enter your choice e.g. 1, 2, or 3:")

if difficulty == "1":
    max_attempts = 10

else:
    print("Invalid choice. Please select 1, 2 or 3")
    max_attempts = 0

hidden_number= random.randint(1,100)
attempts = 0

