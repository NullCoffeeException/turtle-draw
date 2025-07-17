# Turtle-Draw

&nbsp;이미지를 클릭하여 선택한 후, 실행 버튼을 눌러 python turtle을 작동시키는 간단한 GUI 프로그램입니다.

&nbsp;Python으로 제작되었으며, CustomTkinter와 Pillow, Turtle을 사용하여 제작되었습니다.

<br>

---

## 사용 방법

1. 총 4개의 이미지가 있습니다. 원하는 이미지를 클릭합니다.
2. 하단의 '실행' 버튼을 클릭합니다.
3. 실행이 끝난 후에는 창을 닫고 다시 다른 이미지를 선택한 후 '실행' 버튼을 눌러 이미지를 그릴 수 있습니다.

<br>

---

## 설치 방법

1. release 폴더 안에 있는 turtle_draw.exe 파일을 실행하여 바로 사용이 가능합니다. (release 폴더 안에서 실행해야 정상적으로 작동합니다)
2. 또는 pyinstaller로 직접 빌드하여 사용이 가능합니다. 아래 코드를 참고해 주세요.

```bash
# 의존성 설치
pip install -r requirements.txt
pip install pyinstaller

pyinstaller main.py
```
