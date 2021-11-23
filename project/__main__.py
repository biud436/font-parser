
from font.Font import Font
from parser.OptionParserBuilder import OptionParserBuilder

class EntryPoint:
    @staticmethod
    def main():
        args = OptionParserBuilder.build()
        font_name = args.font.strip()
        font_size = int(args.font_size.strip())
        font = Font(font_name or "나눔고딕", font_size or 12)
        print(font.name)
        print(font.size)

if __name__ == '__main__':
    EntryPoint.main()
