# Author: Lucia Floan
# Date: Feb 21, 2025
# Title: Math Quiz

# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as
# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

import random

def math_quiz():
  number1 = random.randint(100, 999)
  number2 = random.randint(100, 999)
  print(f'{number1}\n+ {number2}\n------')

  try:
    answer = int(input('Enter the answer: '))
  except ValueError:
    print('Invalid input, please enter a number.')
    return

  if answer == number1 + number2:
    print('Congratulations, that\'s correct!')
  else:
    print(f'Incorrect, the correct answer is {number1 + number2}.')


if __name__ == '__main__':
  math_quiz()

