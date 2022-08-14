import random

list_of_word = ['money', 'power', 'faceb']
clue = list('?????')
lives = 9

secret_word = random.choice(list_of_word)
unkonw_letter = len(secret_word)

def update_clue(guess, secret_word, clue, unknow_letter): ### this function is made to update the clue by its letter
     index = 0
     while index < len(secret_word):
          if guess == secret_word[index]:
               clue[index] = guess
               unknow_letter -= 1 
          index += 1 
     return unknow_letter
     
guessing = False
while lives > 0:
     print('Hello to the nerve-shredding game')
     print('you have ' + str(lives) + ' lives')
     print(clue)
     
     guess = input('Guess a letter or the whole word: ')
     if guess == secret_word:
          print('Correct guessing ..')
          guessing = True
          break
     
     if guess in secret_word:
          unkonw_letter = update_clue(guess, secret_word, clue, unkonw_letter)
     
     else:
          print('Incorrect answer ...')
          lives -= 1

     if unkonw_letter == 0:
          guessing = True
          break
     
if guessing:
     print('Congratulation you win you the correct word:', secret_word.capitalize())
     

else:
     print('you lost the game the correct guessing is: ', secret_word.capitalize())