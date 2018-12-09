import random


# by ulgoon
# assign answer with randint between 1 to 100
# print answer
answer = random.randint(1,100)
print(answer)

# user try count
trial_cnt = 5

while trial_cnt > 0:
    # user input answer
    user_answer = int(input('Enter your answer: '))

    trial_cnt -= 1

