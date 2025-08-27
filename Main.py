import os
from dotenv import load_dotenv
from Tasks import create_email_body

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", default=None) or None

email_body = create_email_body(
    받는사람 = "오항구 대리", # Keyword Parameter
    용건 = "2025년 업무보고",
    핵심내용 = "휴가 일정 확인",
    api_key = OPENAI_API_KEY
)

print(email_body)