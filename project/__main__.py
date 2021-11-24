from font.Font import Font
from parser.OptionParserBuilder import OptionParserBuilder

class EntryPoint:
    @staticmethod
    def main():
        args = OptionParserBuilder.build()

        font_name = args.font.strip()
        font = Font(font_name or "나눔고딕")
        font.parse()

        filter(lambda x: x.language_id == 23, font.fonts)

        print("\x1b[1;32m" + "[폰트명 파싱 완료]" + "\x1b[0m")
        for font in font.fonts:
            print("{font_name} [{language_id}]".format(font_name=font.name, language_id = font.language_id))


if __name__ == '__main__':
    EntryPoint.main()
