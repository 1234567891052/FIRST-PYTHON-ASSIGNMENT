import random

sol = round(random.random() * 10)

def nextTurn():
    defmsg = int(input('Guess a number between 1 and 10: '))
    answer = defmsg
    i = 1
    while i in range(1, 6) :
        if i >= 5 and answer != sol:
            print('YOU LOSE!' + ' The correct answer is: ' + str(sol))
            break
        if answer == sol :
            print('YOU WIN!')
            break
        else :
            if answer > sol :
                question = int(input('Try again (Think simple): '))
            else:
                question = int(input('Try again (Think big): '))
            answer = question
        i += 1

nextTurn()
