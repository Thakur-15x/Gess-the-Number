import random
n=(random.randint(0,499))
def mygame():
    y = 1
    print("Number of guesses is limited to only  times: 10 \n")
    while (y <= 10):
        x = int(input("Guess the hidden number. No.can be between 0 to 499: "))
        if x < n:
            print("you enter less number please input greater number.\n")
        elif x > n:
            print("you enter greater number please input smaller number.\n")
        else:
            print(" 'YOU WON' :) \n")
            print(" guesses you took to finish.", y)
            recall()
            break
        print("No. of guesses left:", 10 - y)
        y = y + 1

    if (y > 10):
        print("GAME OVER!")
        recall()

def recall():
     a = input("Do you want to Play Again? please enter 1 for Yes and 2 for No: ")
     if a == '1':
         mygame()
     elif a == '2':
         print(" See you later Dear :)")
     else:
         recall()
mygame()

