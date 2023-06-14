#  Auto mailing 

# 1. starting_letter.txt 파일일 이용해서 편지 만들기 
# 2. invited_name.txt 안에 있는 각각의 이름으로 Deam[name] 부분의 이름을 바꾸기 
# 3. 생성된 각각의 편지들을 Output/ReadyToSend 폴더에 저장함

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHORDER = "[name]"    # 바꿀 단어 설정 (상수)

# 텍스트 파일에 있는 이름을 리스트 형식으로 저장 
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# 메일 내용 안에 이름 바꾸기 
with open("./Input/Letters/starting_letter.txt") as letter_file:   
    letter_contents = letter_file.read()                                        # 먼저 편지 내용을 읽고 
    for name in names:                                                          # 반복문을 사용해서                                                 
        strip_name = name.strip()                                               # 이름안에 있는 특수 기호, 띄어쓰기를 제거하고 
        new_letter = letter_contents.replace(PLACEHORDER, strip_name)           # [name]을 저장되어 있는 strip_name으로 바꾸기 
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as completed_letter:   
            completed_letter.write(new_letter)                                  # 바꾼 내용을 Output 폴더에 저장하기
