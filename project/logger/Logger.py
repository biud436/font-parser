from pyee import EventEmitter

class Logger(EventEmitter):
    DEBUG_FLAG = False

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    def __init__(self, debug_flag=True):
        self.log = []

    def print_log(self, **kwargs):
        color = "\x1b[31m"
        c = kwargs["color"]

        if c == "green":
            color = "\x1b[32m"
        elif c == "yellow":
            color = "\x1b[33m"
        elif c == "blue":
            color = "\x1b[34m"
        elif c == "magenta":
            color = "\x1b[35m"
        elif c == "cyan":
            color = "\x1b[36m"
        elif c == "white":
            color = "\x1b[37m"

        print(color + kwargs['message'] + "\x1b[0m")

    def debug(self, msg):
        if Logger.DEBUG_FLAG:
            print("\x1b[33m" + msg + "\x1b[0m") 