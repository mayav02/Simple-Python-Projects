import random
print("Welcome to a little guessing game!")
random_num = random.randint(1, 10)
user = 0

while user != random_num:
    user = int(input("Enter a number between 1 and 10: "))
    if user < random_num:
        print("Try again. Too low.")
    elif user > random_num:
        print("Try again. Too high.")


print(f"Yaasss! You guessed the number {random_num} correctly! ")
    



