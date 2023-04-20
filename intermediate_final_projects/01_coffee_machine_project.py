## coffee machine project

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)”
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# 3. Print report.
# 4 Check resources sufficient?
# 5. Process coins 
# 6. Check transaction successful?
# 7. Make Coffee

## 1. 모듈 불러오기 - 메뉴 및 재료 데이터 
from coffee_data import coffee_menu
from coffee_data import menu_resource

# menu 및 재료 데이터 변수에 저장 
menu = coffee_menu.MENU
resources = menu_resource.resources

## 2. 함수 만들기 
# 2-1. 남아있는 재료를 확인하기 위한 함수 만들기 - 파라미터 (음료 재료)
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insuffition"""
    
    # 주문하고자하는 커피 메뉴 키 값을 저장하기 위해 반복문 사용 - item에 들어갈 데이터들은 메뉴의 키값(재료명)
    for item in order_ingredients:       
        # 조건문 - 만약 주문하고자하는 커피의 재료가 현재 남아있는 재료 재고보다 크거나 같을 경우 
        if order_ingredients[item] >= resources[item]:
            # 어떤 재료가 부족한지 출력 
            print(f"Sorry there is not enough {item}.")
            # 만약 조건이 맞지 않으면(재료가 부족하면) False를 return
            return False
    # 조건이 맞다면(주문이 가능하면) True를 return 
    return True

# 2-2. 동전처리를 위한 함수 만들기
def process_coins():
    """Return the total calculated from coins inserted"""
    print("Please insert coins.")   # 동전을 넣어라 안내문 출력
    # 동전 넣는 즉시 바로 계산 - Total 코인 계산 
    total = int(input("How many quarters?: ")) * 0.25    # quarters - $0.25
    total += int(input("How many dimes?: ")) * 0.1       # dimes - $0.1
    total += int(input("How many nickles?: ")) * 0.05    # nickles - $0.05
    total += int(input("How many pennies?: ")) * 0.01    # pennies - $0.01
    return total 

# 2-3. 거래 성공 여부 확인 함수 만들기 - 파라미터 (동전 토탈 금액, 음료 가격)
def is_transactions_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or Flase if money is insufficient."""
    
    # 만약 넣은 동전의 돈이 커피 값보다 높거나 같을 경우 
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)   # 거스름돈 반환 (소수 두 번째 자리 까지)
        print(f"Here is ${change} in change.")           # 거스름돈 안내 출력 
        global profit          # 전역 변수 불러오기 
        profit += drink_cost   # 불러온 전역 변수 0과 커피 값 더하기 (중첩으로 더하기)
        return True            # 지불이 수락(위의 모든 과정이 완료되면) True를 반환 
    
    # 만약 아니라면 돈이 부족하다라는 안내 문구 츨력 
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False          # 돈이 부족하면 False를 반환 

# 2-4. 커피 재조 함수 만들기 - 파라미터 (음료 이름, 음료 재료) - 음료 재조 후 재료 소진 
def make_coffee(drink_name, order_ingredients):
    """Dedust the required ingredients from the resources."""
    for item in order_ingredients:                  # 주문하고자하는 커피 메뉴 키 값을 저장하기 위해 반복문 사용
        # 남아있는 재료 - 주문한 음료 재료 
        resources[item] -= order_ingredients[item]
    
    # 재조 완료 후 커피 준비!
    print(f"Here is your {drink_name} ☕️. Enjoy!")   # 재조 완료 후 커피 준비!
    
    
## 3. 동작 코드 
# while 반복문을 위한 준비 
is_on = True
# 매출 발생을 위해 최초 0으로 선언 
profit = 0

# 반복문 - 만약 True이면 False가 나올 때 까지 계속 반복
while is_on:
    # 사용자가 어떤 것을 원하는지 묻기 위한 input 함수 사용 
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    # 만약 "off"를 입력했다면, is_on을 False로 저장 - while문 빠져나오기 
    if choice == "off":
        is_on = False
    # 만약 "report"를 입력했을 시 현재 남은 재료 상황 출력 
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Water: {resources['milk']}ml")
        print(f"Water: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    
    # 나머지 커피 메뉴에 따라 동작 
    else:
        # 커피 메뉴 데이터
        drink = menu[choice]
        # 남아있는 재료를 확인하기 위한 함수 불러오기 - 만약 남아있는 재료가 있다면,
        if is_resource_sufficient(drink["ingredients"]):
            # 동전처리를 위한 함수 불러오기 
            payment = process_coins()
            # 거래 성공 여부 확인 함수 불러오기  - 만약 거래가 성립되면,
            if is_transactions_successful(payment, drink["cost"]):
                # 커피 제조 
                make_coffee(choice, drink["ingredients"])