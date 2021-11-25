import struct
from logger.Logger import Logger

class NameRecord:
    def __init__(self):
        self.platform_id = 0
        self.encoding_id = 0
        self.language_id = 0
        self.name_id = 0
        self.string_length = 0
        self.string_offset = 0
        self.name = ""
        self.hex_offset = ""

logger = Logger()

class Font:
    def __init__(self, name):
        self.name = name
        self.fonts = []

        # 폰트 인스턴스 생성
        logger.print_log(message="폰트 객체가 생성되었습니다.", color="green")

    def parse(self):
        font_name = self.name.strip()
        with open(font_name, 'rb') as f:
            logger.print_log(message="빅엔디언 방식으로 12바이트를 읽었습니다.", color="green")
            font_offset_table_buffer = f.read(12)
            major_version, minor_version, num_of_tables, padding = struct.unpack_from('>HHHH', font_offset_table_buffer)
            
            # 결과 값 출력
            logger.debug("major_version : {major_version}" .format(major_version=major_version))
            logger.debug("minor_version : {minor_version}" .format(minor_version=minor_version))
            logger.debug("num_of_tables : {num_of_tables}" .format(num_of_tables=num_of_tables))
            logger.debug("padding : {padding}" .format(padding=padding))

            is_found_name_table = False
            check_sum, offset, length = 0, 0, 0

            for i in range(num_of_tables):
                logger.print_log(message="태그명 4바이트를 읽었습니다.", color="magenta")
                tag_name = f.read(4).decode('ascii')
                data = f.read(12)

                if tag_name == 'name':
                    is_found_name_table = True
                    # 32바이트 unsigned int 형식으로 읽는다.
                    check_sum, offset, length = struct.unpack_from('>III', data)
                    break

            if not is_found_name_table:
                raise Exception('이름 테이블을 찾지 못했습니다.')

            logger.debug("check_sum : {check_sum}" .format(check_sum=check_sum))
            logger.debug("offset : {offset}" .format(offset=offset))
            logger.debug("length : {length}" .format(length=length))

            f.seek(offset)
            
            format_selector, name_record_count, storage_offset = struct.unpack_from('>HHH', f.read(6))

            logger.debug("format_selector : {format_selector}" .format(format_selector=format_selector))
            logger.debug("name_record_count : {name_record_count}" .format(name_record_count=name_record_count))
            logger.debug("storage_offset : {storage_offset}" .format(storage_offset=storage_offset))

            if format_selector != 0:
                logger.debug("langTagCount detect")
                logger.debug("langTagRecord[langTagCount] detect")                
            
            # 이름 테이블을 파싱합니다.
            name_record_table = []
            for i in range(name_record_count):
                name_record = NameRecord()
                name_record.platform_id = struct.unpack_from('>H', f.read(2))[0]
                name_record.encoding_id = struct.unpack_from('>H', f.read(2))[0]
                name_record.language_id = struct.unpack_from('>H', f.read(2))[0]
                name_record.name_id = struct.unpack_from('>H', f.read(2))[0]
                name_record.string_length = struct.unpack_from('>H', f.read(2))[0]
                name_record.string_offset = struct.unpack_from('>H', f.read(2))[0]
                name_record.name = ""

                if name_record.name_id == 4:
                    temp_file_pos = f.tell()

                    f.seek(offset + name_record.string_offset + storage_offset)

                    len_ = name_record.string_length

                    # 문자열 인코딩을 변경합니다.
                    name_record.name = f.read(len_).decode('utf-16-be').rstrip('\0')
                    name_record_table.append(name_record)
                    f.seek(temp_file_pos)
                
                for i in name_record_table:
                    logger.debug("name : {name}" .format(name=i.name))

            self.fonts = name_record_table

        return self

