#number_guessing_game
print(' Welcome!')#starting line
print('Please guess a random number between 1 and 10')
import random 
y=random.randint(1,10)#generating a random number
#defning a function to check if the entered number is correct or not
inps=[]
def inputs(): 

 while  True:
     x=int(input('enter a number'))
     if x>10 :
      
      print('the value is too large.')
      inps.append(x)
     elif x>0 and x!=y:
      
      print('make another guess')
      inps.append(x)
     elif x<0:
      print('number is too small.')
      inps.append(x)
     
     elif x==y:
       print('congratulations...you guessed the right number')
       inps.append(x)
       break
#number of guesses
def inp():
  attempts=len(inps)
  print('the number of guesses u made are,',attempts)
#run game
inputs()
inp()
