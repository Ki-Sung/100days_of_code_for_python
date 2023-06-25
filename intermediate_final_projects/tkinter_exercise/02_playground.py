## 여러 인수를 받아서 그 인수만큼 모두 더하는 함수 만들기 (*args)

## solution 1
# def add(num, *args):
#     total = num
#     for n in args:
#         total = total + n
#     return total
        
# a = add(5, 4, 6, 7)
# print(a)

## solution 2

# 2. 함수 선언 
def add(*args):           # 입력한 인수로 함수 선언 (튜플 형식)
    sum_total = 0         # 더하기 위한 최초 수 선언 
    for n in args:        # 받은 인수 반복하기 
        sum_total += n    # sum_total과 n 값 더하기 
    
    return sum_total      # 최종적으로 더한 값인 sum_total로 반환

# 1. 함수안에 들어갈 인수 설정 
total = add(5, 4, 6, 7) 
print(total)

## keyword argument를 이용하여 계산기 함수 만들기 (**kwargs)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=5)

## keyword argument 클래스로 활용 - 대부분 파이썬 모듈이 이런 형식이다. 
# 차 정보에 대한 클래스 
class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')
        
# 클래스 선언 후 출력 
my_car = Car(make = "Nissan")
print(my_car.make)

my_car = Car(make = "Nissan", model="GT-R")
print(my_car.model)

my_car = Car(color="yellow")
print(my_car.color)