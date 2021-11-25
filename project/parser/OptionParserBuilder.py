import argparse

class OptionParserBuilder:
    @staticmethod
    def build():
        parser = argparse.ArgumentParser(description='폰트를 분석하는 프로그램입니다.')
        parser.add_argument("-f", "--font", help="type the name of TTF file", required=True)
        
        # 디버그 모드 토글
        parser.add_argument("-d", "--debug", help="toggle debug mode", action="store_true")

        args = parser.parse_args()
        return args