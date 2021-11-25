# Introduction

This project allows you to read a real font family from the TrueType font file.

# Usage

To use this tool, you need to install dependencies using pipenv.

```sh
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
pipenv run start -d -f="res/NanumGothicCoding.ttf"

# --------------- Debug Output --------------------- #
폰트 객체가 생성되었습니다.
빅엔디언 방식으로 12바이트를 읽었습니다.
major_version : 1
minor_version : 0
num_of_tables : 14
padding : 128
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
check_sum : 1870634382
offset : 2777952
length : 1110
format_selector : 0
name_record_count : 23
storage_offset : 282
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : NanumGothicCoding
name : 나눔고딕코딩
name : NanumGothicCoding
name : 나눔고딕코딩
폰트 파싱이 완료되었습니다.
NanumGothicCoding [1033]
나눔고딕코딩 [1042]
```
