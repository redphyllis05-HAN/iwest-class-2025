# iwest-class-2025 프로젝트

## 프로젝트 개요

이 프로젝트는 OpenAI의 GPT API를 활용하여 대화형 AI 챗봇을 구현하는 예제 코드 모음입니다. 주요 파일인 `Hello_ai_02.py`는 환경 변수로부터 OpenAI API 키를 불러와, 사용자의 입력에 따라 GPT 모델과 대화를 주고받을 수 있도록 설계되어 있습니다.

## 폴더 및 파일 구조

- `Hello_ai_02.py` : OpenAI GPT API를 활용한 대화형 챗봇 예제
- `Hello_ai_01.py`, `Hello_01.py`, `Hello_02.py` : 기타 예제 코드
- `utils.py` : 유틸리티 함수 모음(필요시 참고)
- `requirements.txt` : 필요한 Python 패키지 목록
- `.env` : OpenAI API 키 등 환경 변수 파일(직접 생성 필요)

## 설치 및 실행 방법

1. **Python 가상환경 생성 및 활성화**

```bash
# (macOS/Linux 기준)
python3 -m venv .venv
source .venv/bin/activate

# (Windows 기준)
python -m venv .venv
.venv\Scripts\activate
```

2. **필수 패키지 설치**

```bash
pip install -r requirements.txt
```

3. **환경 변수 파일(.env) 생성**

프로젝트 루트에 `.env` 파일을 만들고 아래와 같이 작성합니다:

```
OPENAI_API_KEY=sk-...여기에_본인의_API_키_입력...
```

4. **프로그램 실행**

```bash
python Hello_ai_02.py
```

- 종료하려면 입력창에 `quit` 또는 `exit`를 입력하거나 엔터만 누르세요.

## 주요 코드 설명

- `Hello_ai_02.py`는 OpenAI의 `openai` 라이브러리를 사용하여 GPT-4o-mini 모델과 대화합니다.
- API 키는 `.env` 파일 또는 환경 변수에서 불러옵니다.
- 대화 내역은 `messages` 리스트에 저장되어, 맥락을 유지한 채로 대화가 이어집니다.

## 참고 사항

- OpenAI API 키는 외부에 노출되지 않도록 주의하세요.
- API 사용량에 따라 비용이 발생할 수 있습니다.

## 문의

- 프로젝트 관련 문의: [프로젝트 소유자 GitHub](https://github.com/redphyllis05-HAN)