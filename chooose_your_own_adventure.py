name = input('Type Your name: ')
print('Welcome', name,'to this adventure!')

answer = input('You are on a dirt road, it has come to an end and you can go either left or right, which way would you like to go? ').lower()

if answer == 'left':
    answer = input('You come to a  river, you can walk around it, or swim across, Type walk to walk around, and swim to swim across: ').lower()

    if answer == 'swim':
        print('You swam across, and were eaten by an alligator.')

    elif answer == 'walk':
        print('You walked for many miles, lost all energy and lost the game.')

    else:
        print('Not an valid option, You Lose.')

elif answer =='right':
    answer = input('You came across a bridge, it looks very weak, do u want to cross it or head back (cross it/head back)? ').lower()

    if answer == 'cross it':
        print(' You crossed it with ur bravery, and reached the other side of the bridge.')
    
        answer = input('There you meet a stranger. Do u talkto him? (yes/No)?').lower()
        
        if answer == 'yes':
            print('You talk to the stranger, and they gave you the immortality ginseng, You Won The Game :)')

        elif answer == 'no':
            print('You ignored the stranger, he killed you in his rage. You lost :(')

        else:
            print('The option is not valid, You lost the game :(.')

    elif answer=='head back':
        print('You go back and lost the game :(')

    else:
        print('Not a valid option, you lost the game. :(')

else:
    print('Not a valid option. You Lose')


print('Thank you for joining in this amazing adventure. :)')
