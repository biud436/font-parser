# Introduction

This project allows you to read a real font family from the TrueType font file.

# Usage

To use this tools, you need to start with the following command:

```sh
pipenv install
pipenv run start -h
pipenv run start --font="res/NanumGothicCoding.ttf"
```

the result of parsing the font is shown below.

```sh
pipenv run start --font="res/NanumGothicCoding.ttf"

# --------------- Output --------------------- #
major_version : 1
minor_version : 0
num_of_tables : 14
padding : 128
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
[폰트명 파싱 완료]
NanumGothicCoding [1033]
나눔고딕코딩 [1042]
```
