from font.Font import Font
from parser.OptionParserBuilder import OptionParserBuilder
import platform

class EntryPoint:
    @staticmethod
    def main():
        # 옵션 파서 생성
        args = OptionParserBuilder.build()
        font_name = args.font.strip()

        # 폰트 파싱 객체 생성
        font = Font(font_name or "나눔고딕")
        font.parse()

        # 필터링
        results = filter(lambda x: x.language_id == 1033 or x.language_id == 1042, font.fonts)
        
        # 폰트 파싱 완료

        if platform.system().lower().find("windows") != -1:
            print("윈도우즈")

        print("\x1b[1;32m" + "[폰트명 파싱 완료]" + "\x1b[0m")
        for font in list(results):
            print("{font_name} [{language_id}]".format(font_name=font.name, language_id = font.language_id))


if __name__ == '__main__':
    EntryPoint.main()
