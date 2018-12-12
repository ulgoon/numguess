# hi im hyub
import random


# by ulgoon
# assign answer with randint between 1 to 100

answer = random.randint(1,100)

print(answer)
#by mindudekim
#print answer ahead of guessing

# by choiic
# assign user_num with input()
# check user_num is between 1 to 100
# if user_num is not valid, print some message and input user_num again.
# if user_num is not same with answer, print some message and input user_num again. 
while True:
    try:
        user_num = int(input("input your guess number(integer type, 1~100): "))
        if (user_num < 1 or user_num > 100) == True:
            print("Input number in range 1~100")
            continue
        else:
            if user_num == answer:
                print("Congratulations!! You win!!")
                break
            elif user_num > answer:
                print("Think smaller number again!, Your number is greater than the answer!")
                continue
            else:
                print("Think bigger number again!, Your number is smaller than the answer!")
                continue
    except:
        print("Input Integer number in range 1~100")
        continue
    #checked by Daeun Kim
