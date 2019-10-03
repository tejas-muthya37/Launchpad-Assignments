#Guess The Number Challenge! 
import random
a = random.randrange(1,10)
b = int(input('Enter your prediction : '))
if a==b:
	print('Your guess is spot on!')
else:
	print('Better luck next time!')