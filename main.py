def inputnum(text):
 x = input(text)
 while not x.isdigit():
     x= input(' This is not a valid number, please try again ')
 return int(x)

def randomnum():
 import random
 return random.randint(1,101)

def guessing_game():
 text1="Enter your number: "
 num_guess = inputnum(text1)
 random_num = randomnum()

 print(random_num)  # just for testing

 while num_guess != random_num :
   if num_guess < random_num :
    print ('to low')
    num_guess= inputnum(text1)
   elif num_guess > random_num :
    print('to high')
    num_guess= inputnum(text1)
   else:
    break
 print('you win!!!')


def even_or_odd():
 text2="Enter another number:"
 while True :
   num= inputnum(text2)
   if num %2 == 0 :
     print ('The number is even ')
   else:
     print ( 'The number is odd')

def main() :
 guessing_game()
 even_or_odd()

if __name__ == '__main__':
   main()

