# Austin Jackson
# The program is a fish that moves a distance based on user input

def main():
    # REQUIREMENT print() with end=
    print('Welcome User!', end='\n')
    print('This game is very simple')
    wave1 = '¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸'
    fish1 = '>-<(((º>'
    # REQUIREMENT input
    r_num1 = int(input('To start, please enter a number between 1 and 9 -> '))
    # REQUIREMENT '<>' + 'not' + 'or' operators
    while r_num1 < 1 or not r_num1 < 9:
        print('Make sure the number is between 1 and 9')

    num1 = int(r_num1)
    # REQUIREMENT for + in + range
    for x in range(num1):
        # REQUIREMENT string multiplication - printing the swim trail several times
        print('¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸' * (num1 - (num1-1)), sep='', end='')
    print(fish1)
    print('Perfect! \n...well... at least it worked')
    # REQUIREMENT multiplication
    print('\nYour fish has now swam about', num1 * 2, 'inches across the screen')
    r_num2 = input('\nNext, we will need another number -> ')
    r_num3 = input('oops... sorry, one more please :) -> ')
    num2 = int(r_num2)
    num3 = int(r_num3)
    print('')
    print('Now! *drum roll please* PREPARE TO BE AMAZED')
    # REQUIREMENT exponents - raising first input by the second input
    pownum = num2**num3
    # REQUIREMENT string concatenation - just adding strings
    print(wave1 * pownum + fish1)
    # REQUIREMENT subtraction - it literally does nothing here :)
    print('Through my newfound powers of exponents...,\n your fish has moved', pownum * 2 - 0, 'inches')
    fish_name = input("speaking of good ol' fishy, could you give him a name?:")
    print('Great choice!')
    print('With this, you have completed the tutorial.')
    print('Unfortunately, at this point in time, the tutorial is the entire game.')
    print('Your journey with', fish_name, 'has finished...')
    print('For now.')

    print('------------')
    print('However, this program is not over yet')
    print('Here is some simple math to send you on your way')
    # REQUIREMENT division - outputs the quotient
    print('25/5 =', int(25 / 5))
    # REQUIREMENT modulus operator - returns the remainder after division
    print('26/5 has a remainder of', 26 % 5)
    # REQUIREMENT floor division - calc. how many times divisable with no remainder
    print('5 goes into 16', 16 // 5, 'times evenly, leaving a remainder')
    print('And lastly')
    print('1 + 1 =', 1 + 1)
    print('This concludes the game')
    print('Thank you for playing!')
    print(fish_name, 'says goodbye')

    continue1 = input('Enter y if you wish to continue:')
    # REQUIREMENT relational operators - checking if the user entered 'y'
    if continue1 != "y":
        print('Thank you for playing')
    elif continue1 == 'y':
        print('congrats on making it this far')
        print('However, there is some unfortunate news...')
        print(fish_name, 'has been kidnapped')
        print('')
        print('The criminals got away but there is still time to save', fish_name)
        print(fish_name, 'is trapped behind a few locked doors')
        print('solve a puzzle to get through each door to save', fish_name)
        input('press enter to continue')
        print('The first door is locked behind a simple math problem')
        print('answer correctly and you may move on')
        answer1 = None
        while answer1 != int(((5*10)/8)*4):
            answer1 = int(input('5 multiplied by 10, divided by 8, multiplied by 4:'))
        print('Great Job!')
        print("let's move onto door 2")
        print('This one is just a question, the right answer should get you through')
        answer2 = None
        while answer2 != "the world may never know":
            answer2 = input('How many licks does it take to get to the tootsie roll center of a Tootsie Pop?:')
            print('Make sure to answer in all lowercase')
        print('That was a tough one, keep going')
        print('This next one is pretty easy')
        answer3 = None
        while answer3 != int(256):
            answer3 = int(input('How many fluid ounces are in 2 gallons?:'))
        print('You should be at the fourth and final door before', fish_name)
        print('expect this one to be difficult')
        answer4 = None
        while answer4 != "brown":
            answer4 = input('What is the rarest M&M color?:')
        print('Finally!')
        print('wait...')
        print('Why is the room empty? Where is', fish_name + '?')


########## CALL TO MAIN ##########
main()
