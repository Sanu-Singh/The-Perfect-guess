# the perfect guess
# let computer choose a no from 1 to 100 and user have to guess it.

import random
randomNumber = random.randint(1, 100)
#print(randomNumber)
userguess=None
guesses=0

while(userguess !=randomNumber):
 userguess = int(input("Guess the No: "))
 guesses +=1
 if (userguess == randomNumber):
    print("Congratulation! you guessed right.")
 else:    
    if (userguess>randomNumber):
       print("Sorry! guess a lower no.")
    else:
       print("Sorry! guess a higher no.")

print(f"you have guessed in {guesses} guesses.")       

with open("highscore.txt", "r") as f:
    highscore= int(f.read())

if(guesses<highscore):
  print("Congratulations! you set a new high score")
  with open("highscore.txt","w") as f:
    f.write(str(guesses))