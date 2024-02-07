# Introduction

This project allows you to read a real font family from the TrueType font file.

# Usage

To use this tool, you need to install dependencies using pipenv.

```sh
# if you don't have pipenv, you can install it using pip.
pip install pipenv

# install dependencies
pipenv install
```

and next, you pass the path of the font file to the tool.

```sh
To use this tools, you need to start with the following command:
pipenv run start -h
pipenv run start --font="res/NanumGothicCoding.ttf"
pipenv run start -d --font="res/NanumGothicCoding.ttf"
pipenv run start --debug --font="res/NanumGothicCoding.ttf"
```

the result of parsing the font is shown below.

```sh
# The parameter named '-d' is used to show the debug information.
pipenv run start --font="./res/NanumGothicCoding.ttf" --enabled_download --url="https://github.com/biud436/font-parser/raw/main/res/NanumGothicCoding.ttf"

# --------------- Debug Output --------------------- #
12/13 22:46:38 [NOTICE] Downloading 1 item(s)

12/13 22:46:38 [NOTICE] CUID#7 - Redirecting to https://raw.githubusercontent.com/biud436/font-parser/main/res/NanumGothicCoding.ttf

12/13 22:46:38 [NOTICE] File already exists. Renamed to /Users/u/python-projects/reading-font/NanumGothicCoding.1.ttf.

12/13 22:46:39 [NOTICE] Download complete: /Users/u/python-projects/reading-font/NanumGothicCoding.1.ttf

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
0689bc|OK  |   5.3MiB/s|/Users/u/python-projects/reading-font/NanumGothicCoding.1.ttf

Status Legend:
(OK):download completed.
폰트 객체가 생성되었습니다.
빅엔디언 방식으로 12바이트를 읽었습니다.
태그명 4바이트를 읽었습니다[12]
태그명 4바이트를 읽었습니다[28]
태그명 4바이트를 읽었습니다[44]
태그명 4바이트를 읽었습니다[60]
태그명 4바이트를 읽었습니다[76]
태그명 4바이트를 읽었습니다[92]
태그명 4바이트를 읽었습니다[108]
태그명 4바이트를 읽었습니다[124]
태그명 4바이트를 읽었습니다[140]
태그명 4바이트를 읽었습니다[156]
태그명 4바이트를 읽었습니다[172]
태그명 4바이트를 읽었습니다[188]
폰트 파싱이 완료되었습니다.
NanumGothicCoding [1033]
나눔고딕코딩 [1042]
```
