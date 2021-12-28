
import random
import tinydb
import csv


username = input('Enter your username')
round_number = input('how many rounds do you want to play: ')

#this is not used
move_choices = ['rock','scissor','paper']
user_move_list = []

score = 0

def round_process():
    global score
    global user_move_list

    move = input("Input your move as rock,scissor, or paper")
    user_move_list.append(move)

    x = random.choice(['rock','scissor','paper'])

    x = str(x)
    print('This is the move given by the machine: ' + x)


    if move == x:
        score = score

    if move!= x:
        if (x == 'rock' and move == 'scissor'):
            score = score - 1

        if (x == 'scissor' and move == 'rock'):
            score = score + 1

        if(x== 'paper' and move == 'scissor'):
            score = score + 1

        if(x == 'scissor' and move == 'paper'):
            score = score - 1
        if(x == 'paper' and move =='rock'):
            score = score - 1

        if(x == 'rock' and move == 'paper'):
            score = score + 1


for i in range(int(round_number)):
    round_process()

print('your score is: ' + str(score))
print(user_move_list)

column_names =[1,2,3,4]

with open('moves_record.csv', 'a') as f:
    write = csv.writer(f)
    write.writerow(column_names)
    write.writerow(user_move_list)

