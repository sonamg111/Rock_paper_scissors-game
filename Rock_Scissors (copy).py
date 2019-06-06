import random
my_list=["rock","paper","scissor"]
computer=random.choice(my_list)
while True:
	user_input=raw_input("enter tha rock,sesior,paper")
	if user_input not in my_list:
		print"invalid input"
	elif user_input==computer:
		print"Draw"
	elif user_input=="paper" and computer=="rock":
		print"win"
	elif user_input=="rock" and computer=="scissor":
		print"win"	
	elif user_input=="scissor" and computer=="paper":
		print"win"
	else:
		print"loss"
	again_input=raw_input("do you want to play again(yes/no)")
	if again_input=="yes":
		continue
	else:
		break					