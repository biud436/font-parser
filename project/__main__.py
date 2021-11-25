from font.Font import Font
from parser.OptionParserBuilder import OptionParserBuilder
import platform

from logger.Logger import Logger

logger = Logger()

class EntryPoint:
    
    @staticmethod
    def main():
        # 옵션 파서 생성
        args = OptionParserBuilder.build()
        font_name = args.font.strip()
        is_debug =args.debug

        Logger.DEBUG_FLAG = is_debug == True

        # 폰트 파싱 객체 생성
        font = Font(font_name or "나눔고딕")
        font.parse()

        # 필터링
        results = filter(lambda x: x.language_id == 1033 or x.language_id == 1042, font.fonts)
        
        # 폰트 파싱 완료
        if platform.system().lower().find("windows") != -1:
            print("윈도우즈")

        logger.print_log(message="폰트 파싱이 완료되었습니다.", color="green")
        for font in list(results):
            print("{font_name} [{language_id}]".format(font_name=font.name, language_id = font.language_id))


if __name__ == '__main__':
    EntryPoint.main()
