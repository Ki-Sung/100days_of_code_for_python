## coffee machine project

## 1. Make 3 hot flavours
# 1-1. Espresso - 500ml water, 18g coffe, $1.50
# 1-2. Latte - 200ml water, 24g coffee, 150ml milk, $2.50
# 1-3. Capucino - 250ml water, 24g coffee, 100ml milk, $3.00

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

## 2. Coin Operated

# program requirements
# 1. print report
# 2. check resources sufficient?
# 3. Process coins