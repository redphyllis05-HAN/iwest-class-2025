from urllib.parse import urljoin
import requests
# BeautifulSoup : html parser
from bs4 import BeautifulSoup
from utils import download_file # 'utils.py' 파일에서 'download_file' import

page_url = "https://www.iwest.co.kr/iwest/582/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGaXdlc3QlMkYxNDglMkYyMjUxNCUyRmFydGNsVmlldy5kbyUzRnBhZ2UlM0QxJTI2c3JjaENvbHVtbiUzRCUyNnNyY2hXcmQlM0QlMjZiYnNDbFNlcSUzRCUyNmJic09wZW5XcmRTZXElM0QlMjZyZ3NCZ25kZVN0ciUzRCUyNnJnc0VuZGRlU3RyJTNEJTI2aXNWaWV3TWluZSUzRGZhbHNlJTI2cGFzc3dvcmQlM0QlMjY%3D"

# 지정 주소로 GET 요청을 보내고 응답을 받습니다.
response = requests.get(page_url)
html: str = response.text

soup = BeautifulSoup(html, "html.parser")

tag = soup.select_one("a[href*=download]")

print(tag["href"])

download_url = urljoin(page_url, tag["href"])
print(download_url)

download_file(download_url, "./download/2025.08.27 Test/리플릿.pdf")

# 파일만 생성할뿐, 폴더를 생성해 주지 않기 때문에
# utils.py 에서 아래의 명령을 입력해준다. > 폴더를 생성하고 다운로드 수행
    # dir_path = os.path.dirname(filepath)
    # os.makedirs(dir_path, exist_ok=True)