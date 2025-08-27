
# 운영체제와 상호작용하기 위한 모듈
import os
# .env 파일에서 환경변수를 불러오는 함수
from dotenv import load_dotenv
# OpenAI API를 사용하기 위한 라이브러리
from openai import OpenAI

# .env 파일에 저장된 환경변수를 불러온다
load_dotenv()

# 환경변수에서 OPENAI_API_KEY 값을 가져온다. 없으면 None을 반환한다.
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", default=None) or None

# OpenAI 클라이언트 객체를 생성한다. 명시적으로 API 키를 지정한다.
client = OpenAI(api_key=OPENAI_API_KEY)

# OpenAI 챗봇 API에 메시지를 보내고 응답을 받는다.
response = client.chat.completions.create(
    model="gpt-4o-mini",  # 사용할 OpenAI 모델 지정
    messages=[
        # 시스템 역할 메시지: 챗봇의 성격과 역할을 지정
        {"role" : "system", "content" : "당신은 한국서부발전(에너지기업)의 '지피티(이름)' 감독입니다."},
        # 사용자 역할 메시지: 실제로 챗봇에게 전달할 질문이나 요청
        {"role" : "user", "content" : "자기소개를 해주세요. 이름으로 3행시도 해주세요."}
        # role : system, user, assistant 등 다양한 역할이 있음
    ]
)

# 응답의 사용량(토큰 등) 정보를 출력
print("response.usage :", response.usage)
# 챗봇의 답변(메시지 내용) 출력
print(response.choices[0].message.content)