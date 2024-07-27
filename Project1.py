import random
import math

#Taking user input lower value and upper alue
lower = int(input('Enter a Lower bound : ' ))
upper = int(input('Enter a Upper bound : ' ))

#Generating random number using randit function.
#randiit fn generates random number between the given range of numbers.
X = random.randint(lower,upper)

#Finding out user having total chances to guess number
#math.log() - computes the logarithm of 'x' with the specified base.
total_chances = math.ceil(math.log((upper - lower) + 1, 2))
print("You have only", total_chances, "chances")

count = 0
flag = False

#Iterate till count<total chances becomes false
while (count < total_chances):
    count += 1

    guess_no = int(input())

    if (X == guess_no):
        print("Congratulations! You did a great job.\n You did it in", count, "try")
        flag = True
        break

    elif(X > guess_no):
        print("You guessed too small")
        print("You have remained", total_chances-count, 'chances')

    elif(X < guess_no):
        print("You guessed too high")   
        print("You have remained", total_chances-count, 'chances')  

#Prints the computer generated number
if not flag:
    print("\n The number is %d" % X)
    print("\t Better Luck Next Time")          
    
    
