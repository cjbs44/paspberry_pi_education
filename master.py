import string
import random

#create a list of 4 characters
secret = [random.choice('ABCDEF') for item in range(4)]

#tell the player what is going on
print("I've selceted a 4 -character secrest code from the letters A,B,C,D,E and F.")
print("I may have repeated some.")
print("Now try and guess what I chose.")

yourguess = []
while list(yourguess) != secret:
    yourguess = input("Enter a 4-letter guess: e.g. ABCD : ").upper()
    if len(yourguess) != 4:
        continue

#turn the guess into a list, like the secret
    print("You guessed ", yourguess)

#create a list of tuples comparing the secret with the guess
    comparinglist = zip(secret, yourguess)

#create a list of the letters that match
#(this will be 4 when the lists match exactly)
    correctlist = [speg for speg, gpeg in comparinglist if speg == gpeg]

#count each of the letters in the secret and the guess
#and make a note of the fewest in each
    fewestletters = [min(secret.count(j), yourguess.count(j)) for j in 'ABCDEF']
    print("Number of correct letter is ", len(correctlist))
    print("Number of unused letters is ", len(fewestletters) - len(correctlist))

print("YOU GOT THE ANSWER : ", secret)
          
      
