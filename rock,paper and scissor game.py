import random
print("---ROCK,PAPER,SCISSOR GAME---")
user_choice=input('Enter your choice rock/paper/scissor:')
choice=['rock','paper','scissor']
computer_choice=random.choice(choice)
if user_choice==computer_choice:
    print("It's a tie!")
elif user_choice=='rock' and computer_choice=='scissor':
    print("You win!")
elif user_choice=='scissor' and computer_choice=='rock':
    print("Computer wins!")
elif user_choice=='paper' and computer_choice=='rock':
    print("You win!")
elif user_choice=='rock' and computer_choice=='paper':
    print("Computer wins!")
elif user_choice=='scissor' and computer_choice=='paper':
    print("You win!")
elif user_choice=='paper' and computer_choice=='scissor':
    print("Computer wins!")
print(f'computer choice is {computer_choice}')
print('The game is over!')





