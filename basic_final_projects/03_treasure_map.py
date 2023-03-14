# excerise 3 - Treasure Map Exercise - other way 
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# 지도 그리기
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

# 위치 지정 
position = input("Where do you want to put the treasure? ")

# 수평 column 역할
horizonal = int(position[0])  
# 수직 - row 역할
vertical = int(position[1])  

# 해당 위치에 X 표시 
select_row = map[vertical - 1]
select_row[horizonal - 1] = "X"

# 최종 결과 
print(f"{row1}\n{row2}\n{row3}")