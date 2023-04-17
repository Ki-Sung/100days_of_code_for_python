import os
import random
from higher_lower import art
from higher_lower import game_data

# 1. 로고 출력 
print(art.logo)              # 시작 로고 

# 2. 팔로우 데이터 불러오기 
data = game_data.data

game_over = False
score = 0
while not game_over:
    # 3. 초반에 랜덤하게 두 대결 상대를 출력 
    compare = random.choice(data)
    print("Compare A: " + compare['name'] + ", " + compare['description'] + ", " + "from " + compare['country'])
    print(art.vs)                # vs 로고 
    against = random.choice(data)
    print("Against B: " + against['name'] + ", " + against['description'] + ", " + "from " + against['country'])
    
    # 4. 선택할 수 있게 input 할 사항 넣기
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == 'A':
        choice_result = compare['follower_count']
        print(choice_result)
    else:
        choice_result = against['follower_count']
        print(choice_result)
        
    if choice_result > compare['follower_count']:
        score += 1
        print(f"you got it Current score: {score}")
    elif choice_result > against['follower_count']:
        score += 1
        print(f"you got it Current score: {score}")
    else:
        os.system('clear')
        print(f"Sorry, that's wrong. Final score:{score}")
        game_over = True