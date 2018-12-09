import random


# by ulgoon
# assign answer with randint between 1 to 100
# print answer
# print(answer)

answer = random.randint(1,100)

print(answer)

# user try count
trial_cnt = 5

while trial_cnt > 0:
    # user input answer
    num_guess = int(input("Take a guess between 1 and 100 : "))

    trial_cnt -= 1