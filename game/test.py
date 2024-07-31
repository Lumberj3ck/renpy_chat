import random
from colorama import Fore, init
import time 



init()

lines = ["green", "red", "orange"]

line = random.choice(lines)

print("Press enter to start typing")
print("Input this line ")
print(line)

input()

start = time.time()
user_input = input()
end = time.time()


def display_results(user_input):
    errors = 0
    for i in range(len(line)):
        if i < len(user_input):
            if line[i] == user_input[i]:
                print(f"{Fore.GREEN}{user_input[i]}", end='')
            else:
                errors += 1
                print(f"{Fore.RED}{user_input[i]}", end="")
        else:
            errors += 1
            print(f"{Fore.RED}{line[i]}", end="")
    
    if len(line) < len(user_input):
        for i in user_input[len(line):]:
            print(f"{Fore.RED}{i}", end="")

    return errors 


errors = display_results(user_input)