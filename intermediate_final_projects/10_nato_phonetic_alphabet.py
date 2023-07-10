## Nato 알파벳 음성기호 프로젝트 
# Todo
# 1. 데이터프레임을 딕셔너리 형식으로 반환 - 딕셔너리 컴프리헨션 사용
# 2. 사용자가 입력하는 단어로부터 음성 규약 단어들의 리스트 만들기 - 리스트 컴프리헨션 사용

# 모듈 불러오기 
import pandas as pd 

# 데이터 불러오기 
data = pd.read_csv('data/nato_phonetic_alphabet.csv')

# 데이터프레임을 딕셔너리 형식으로 변환 
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# 사용자가 입력한 단어로부터 음성 규약 단어들을 리스트로 저장할 함수 만들기 
def generate_phonetic():
        word = input("Enter a word: ").upper()      # 입력창 만들기
        try:                                        # 만약 알파벳을 입력했다면, 
            output_list = [phonetic_dict[letter] for letter in word]  # 음성 규약 단어 리스트 저장
        except KeyError:                                              # 만약 위 코드블록이 에러가 났을 경우
            print("Sorry, only letters in the alphabet please!")      # 경고창 출려과 함께 프롬프트 출력
            generate_phonetic()                                       # 프롬프트 다시 생성 - 우리가 만든 함수를 이용하여
        else:                                                         # 모든 코드 블록이 동작하면 
            print(output_list)                                        # 결과물 출력 
            
generate_phonetic()                                  # 설정한 함수 불러오기 