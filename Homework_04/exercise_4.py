from random import randint

N = randint(0, 100)
K = int(input("Guess a number from 0 to 100: "))
while K != N:
    if K < N:
        print("Didn't guess, the number is less than the guessed number")
    else:
        print("Didn't guess, the number is more than the guessed number")
    K = int(input("Try again: "))

print("Congratulations.You guessed!")

print(K)
print(N)
