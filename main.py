from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Меньше")
    return turns - 1
  elif guess < answer:
    print("Больше")
    return turns - 1
  else:
    print(f"Ты угадал числом было {answer}.")

def set_difficulty():
  level = input("Выбери сложность: легкая и сложная: ")
  if level == "легкая":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  print("Добро пожаловать в игру угадай число")
  print("Я загадал случайное число от 1 до 100")
  answer = randint(1, 100)
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"У тебя есть {turns} попыток угадать число")

    guess = int(input("Предположи что это за число: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("Ты проиграл")
    elif guess != answer:
      print("Попробуй еще раз")

game()
