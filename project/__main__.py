
from font.Font import Font
from parser.OptionParserBuilder import OptionParserBuilder

class EntryPoint:
    @staticmethod
    def main():
        OptionParserBuilder.build()
        font = Font("나눔고딕", 12)
        print(font.name)
        print(font.size)

if __name__ == '__main__':
    EntryPoint.main()
