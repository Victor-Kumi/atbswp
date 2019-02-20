import random



def guessProper():
    global guess
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

def randomToss():
    global toss
    toss = random.randint(0, 1) # 0 is tails, 1 is heads

    #convert 0 and 1 to tails and heads respectively.
    if toss == 1:
        toss = 'heads'
    else:
        toss = 'tails'

guess = ''
guessProper()
toss = ''
randomToss()

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = ''
    guessProper()
    randomToss()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
