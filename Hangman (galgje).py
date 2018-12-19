import random
print("Welcome to hangman")
secretwords = ('world', 'letter', 'desperate')
word = random.choice(secretwords)
print("_ " * len(word))
playerinput = input("Type a letter ")


