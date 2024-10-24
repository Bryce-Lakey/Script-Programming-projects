import random
smaller = int(input("Enter the lowest number: "))
larger = int(input("Enter the biggest number: "))
myNumber = random.randint(smaller, larger)
print("Think of a number between", smaller, "and", larger, "and I will try to guess what it is.")

count = 0

while smaller <= larger:
    count += 1
    for roll in range(1):
        print("My guess is", random.randint(smaller, larger), end = "")
        guess = random.randint
    feedback = str(input(", was my guess correct? "))

    if feedback == "no":
        continue
    elif feedback == "yes":
        break
    
print("I guessed your number in", count, "tries.")

    


