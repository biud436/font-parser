import argparse

class OptionParserBuilder:
    @staticmethod
    def build():
        parser = argparse.ArgumentParser(description='폰트를 분석하는 프로그램입니다.')
        parser.add_argument("-f", "--font", help="사용할 폰트를 입력하세요", required=True)
        args = parser.parse_args()