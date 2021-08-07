import random
num = random.randint(1,9)
c = 5
#print(num)

while c>0:
    enteredVal = int(input("Enter your guess: "))

    if (num == (enteredVal+1)) or (num == (enteredVal-1)) :
        print("Very Close")
        c -=1
        

    elif (num == (enteredVal+2)) or (num == (enteredVal-2)) :
        print("Close")
        c-=1

    elif num == enteredVal:
        print("Yay! You won!")
        choice = int(input("Want to play once more? press 1 for yes and 0 for no"))
        if choice == 1:
            c = 5            
            num = random.randint(1,9)
            #print(num)

        elif choice == 0:
            break

    else:
        print("Not Close")
        c-=1

    if c==0:
        print("You lose!")
        choice = int(input("Want to play once more? press 1 for yes and 0 for no"))
        if choice == 1:
            c = 5            
            num = random.randint(1,9)
            #print(num)

        elif choice == 0:
            break

