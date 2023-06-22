## Nato 알파벳 음성기호 프로젝트 
# Todo
# 1. 데이터프레임을 딕셔너리 형식으로 반환 - 딕셔너리 컴프리헨션 사용
# 2. 사용자가 입력하는 단어로부터 음성 규약 단어들의 리스트 만들기 - 리스트 컴프리헨션 사용

# 데이터 불러오기 
import pandas as pd 

data = pd.read_csv('data/nato_phonetic_alphabet.csv')

# 데이터프레임을 딕셔너리 형식으로 변환 
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# 사용자가 입력한 단어로부터 음성 규약 단어들 리스트 만들기 
word = input("Enter a word: ").upper()      # 입력창 만들기 
output_list = [phonetic_dict[letter] for letter in word]  # 음성 규약 단어 리스트 저장
print(output_list)                          # 결과물 출력