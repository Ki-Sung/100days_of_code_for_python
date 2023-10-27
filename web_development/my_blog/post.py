# 블로그 포스트 제어 클래스 
class Post:
    # 초기화 함수
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title 
        self.subtitle = subtitle
        self.body = body