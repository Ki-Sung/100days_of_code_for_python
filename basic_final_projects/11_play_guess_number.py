from guess_number import art
from random import randint

# global scop - 전역 상수 
EASY_LEVEL_TRUNS = 10
HARD_LEVEL_TRUNS = 5

# 레벨 선택 함수 
def set_difficulty():
    choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose_level == 'easy':
        return EASY_LEVEL_TRUNS
    else:
        return HARD_LEVEL_TRUNS

# 실질적으로 유저가 입력후 동작하는 함수 구현 
def check_answer(guess, answer, turns):
    """checks answer against guess. Return the number of turns remaining."""
    if guess > answer:
        print("Too hight")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it!!, The answer was {answer}")

# 게임 동작 함수 
def game():
    # Include an ASCII art logo
    print(art.logo)
    
    # 맞춰야할 숫자 출력 - 1 부터 100까지 랜덤으로 숫자 호출
    print("Welcom to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    
    # 레벨 선택 
    turns = set_difficulty()
    
    # 숫자 맞추기 반복 동작 
    guess = 0
    while guess != answer:    # 우리가 입력할 숫자와 제시된 숫자가 같지 않으면, 계속 반복
        print(f"You have {turns} attempts remaining to guess the number.")
        # 유저가 맞춰야할 숫자 입력 
        guess = int(input("Make a guess: "))
        # 횟수를 추적, 만약 틀렸다면 1개씩 차감 
        turns = check_answer(guess, answer, turns)
        if turns == 0:                                     # 만약 모두 차감되면 
            print("You've run out of guesses, yout lose")  # 해당 안내문 출력 
            return                                         # 빠져나오기 
        elif guess != answer:              # 만약 기회가 남아있다면 
            print("Guess again")           # 계속해서 진행 
            
# 코드 동작 
game()