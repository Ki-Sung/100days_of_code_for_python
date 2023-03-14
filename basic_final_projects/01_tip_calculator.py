# print title
print("Welcom to the tip calculator")
# input bill
bill = float(input("What was the total bill? $"))

# input tip
tip = int(input("What percentage tip would you like to give? 10%, 12? or 15%? "))

# input people
people = int(input("How many people to split the bill? "))

# calculate for total bill
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

# calculate each person
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)   # 소수점 2째자리 까지 무조건 나오게 지정
print(f"Each person sould pay: ${final_amount}")