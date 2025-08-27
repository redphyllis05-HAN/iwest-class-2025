
import os
import requests

def download_file(
    file_url: str, 
    filepath: str | None = None, # 옵션 : 'filepath' 를 지정하지 않으면 디폴트로 지정해라 <default parameter>
) -> None: # 함수의 Return 값은 없으므로 'None'
    res = requests.get(file_url)
    print("res ok :", res.ok)

    if filepath is None:
        filepath = os.path.basename(file_url)

    file_content = res.content

    dir_path = os.path.dirname(filepath)
    os.makedirs(dir_path, exist_ok = True) # 'exist_ok=True' : 경로에 폴더가 있어도 오류를 발생시키지 않는다.

    # 주의 : 같은 경로의 경로일 경우, 덮어쓰기가 된다.
    with open(filepath, "wb") as f:
        f.write(file_content)
        print("saved", filepath)

def multiply(a, b):
    return a * b