def inputnum():
 x= int(input("Enter your number: "))
 return x

def randomnum():
 import random
 return random.randint(1,101)

random_num = randomnum()
num_guess = inputnum()

print(random_num)  # just for testing

while num_guess != random_num :
  if num_guess < random_num :
    print ( 'to low ')
    num_guess= inputnum()
  elif num_guess > random_num :
    print('to high ')
    num_guess= inputnum()
  else:
    break
print('you win!!!')