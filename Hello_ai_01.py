import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # 'load_dotenv'만 입력하고 '()'를 입력 안하면 함수를 실행한 것이 아니다.

# dict과 같은 구조
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", default=None) or None


# 명시적으로 api key를 지정하지 않으면, OpenAI 내부에서 자체적으로 OPENAI_API_KEY 환견변수 값을 찾는다.
# 그러나 엉뚱한 키가 입력되지 않도록 관리 측면에서 이와 같은 방법으로 KEY를 지정하는 것이 좋다.
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role" : "system", "content" : "당신은 한국서부발전(에너지기업)의 '지피티(이름)' 감독입니다."},
        {"role" : "user", "content" : "자기소개를 해주세요. 이름으로 3행시도 해주세요."}
        # role : system, user, assistant etc.
    ]
)

print("response.usage :", response.usage)
print(response.choices[0].message.content)