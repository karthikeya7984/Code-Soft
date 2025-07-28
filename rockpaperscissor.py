import random
print("Let's play a game rock paper scissor")
rps=int(input("Select a number 0 is rock, 1 is paper, 2 is Scissors."))
rps_list = random.randint(0,2)
if rps == rps_list:
    print("Draw")
elif (rps == 0 and rps_list == 2) or  (rps == 1 and rps_list == 0) or (rps == 2 and rps_list == 1) :
    print("You Won")
elif rps > 2 or rps < 0 :
    print("You entered invalid number")
else:
    print("You lose")
