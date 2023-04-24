from coffee_machine.menu import Menu, MenuItem         # 사전에 만들어진 coffee machine menu 파일에, Menu와 MenuItem 클래스 불러오기 
from coffee_machine.coffee_maker import CoffeeMaker    # 사전에 만들어진 coffee machine coffee_maker 파일에, CoffeMaker 클래스 불러오기 
from coffee_machine.money_machine import MoneyMachine  #  사전에 만들어진 coffee machine money_machine 파일에 MoneyMachine 클래스 불러오기 

# 1. 불러온 클래스를 통해 각각의 객체 생성
money_machine = MoneyMachine()    # 현재 돈 상황, 동전 가격의 정의, pament를 위한 MoneyMachine 객체 생성 
coffee_maker = CoffeeMaker()      # 현재 재료 상황, 재료 소진 관리, 커피 만들기를 위한 CoffeeMaker 객체 생성 
menu = Menu()                     # 커피 메뉴 당 소진되는 재료, 재료상황에 맞게 커피 주문 상황 확인을 위한 Menu 객체 생성 

# 2. 동작 코드 
is_on = True     # 반복문을 위한 준비 (while)

# 반복문 - 만약 True이면 False가 나올 때 까지 계속 반복
while is_on:
    options = menu.get_items()                                         # 메뉴 이름을 출력하기 위해 menu 객체에 get_items() 메소드 활용 
    choice = input(f"What would you like? ({options}): ").lower()      # 각 옵션 입력을 위한 input 창 (커피 메뉴 및 재료 상황 확인 )
    
    # 입력된 값에 따라 동작 
    if choice == "off":                   # 만약 "off"를 입력하면 
        is_on = False                     # while 문 종료 - 커피머신 종료 
    elif choice == "report":              # 만약 "report"를 입력하면
        # 생성된 coffee_maker, money_machine 객체 중 report 메소드 활용 
        coffee_maker.report()             # 현재 남아 있는 재료 확인 
        money_machine.report()            # 현재 커피머신 내 수금된 돈(커피머신 이용 금액) 확인 
    else:                                 # 그밖에 - 만약 커피 메뉴를 입력하면 
        drink = menu.find_drink(choice)   # 생성된 객체 안에 find_drink()라는 메소드 활용 -> find_drink()안에 파라미터로 음료 이름 입력 e.g "latte"
        # 조건문 작성 - 만약 재료가 충분하고 동전도 금액에 맞게(혹은 그 이상) 입력이 되었다면 ->
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)       # 커피 만들기!
        
        # 아래 처럼 쓸 수도 있음
        # is_enought_ingredients = coffee_maker.is_resource_sufficient(drink)  # 생성된 coffee_maker 객체 안에 is_resource_sufficient() 메소드 활용 - 파라미터로 drink 입력 
        # is_payment_successful = money_machine.make_payment(drink.cost)       # 생성된 money_machine 객체 안에 make_payment() 메소드 활용 - 파라미터로 drink.cost 입력 
        # if is_enought_ingredients and is_payment_successful:                 # 조건문 작성 - 만약 재료가 충분하고 동전도 금액에 맞게(혹은 그 이상) 입력이 되었다면
            # coffee_maker.make_coffee(drink)                                  # 커피 만들기! 