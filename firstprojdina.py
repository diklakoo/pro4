def inputnum(text):
 x= int(input(text))
 return x

def randomnum():
 import random
 return random.randint(1,101)

text1="Enter your number: "
random_num = randomnum()
num_guess = inputnum(text1)

print(random_num)  # just for testing

while num_guess != random_num :
  if num_guess < random_num :
    print ( 'to low ')
    num_guess= inputnum(text1)
  elif num_guess > random_num :
    print('to high ')
    num_guess= inputnum(text1)
  else:
    break
print('you win!!!')


text2="Enter another  number:"
while True :
 num= inputnum(text2)
 if num %2 == 0 :
    print ('The number is even ')
 else:
    print ( 'The number is odd')
