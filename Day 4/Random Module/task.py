import random
print("This is a heads  or tails game")
user_input = input("please select a number between 0 and 1 ")
random_number = random.randint(0, 1)
while user_input not in ("0", "1"):
    print("wrong entry")
    user_input = input("please select a number between 0 and 1 ")
if user_input == random_number:
        print("heads")
else:
        print("tails")

