from pyee import EventEmitter

class Logger:
    DEBUG_FLAG = False
    emitter = EventEmitter()

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

    def get_log(self):
        return self.log

    def on(self, event, callback):
        Logger.emitter.on(event, callback)

    def emit(self, event, *args, **kwargs):
        Logger.emitter.emit(event, *args, **kwargs)

    def off(self, event, callback):
        Logger.emitter.off(event, callback)
    
    def once(self, event, callback):
        Logger.emitter.once(event, callback)
    
    def removeAllListeners(self, event):
        Logger.emitter.removeAllListeners(event)
    
    def debug(self, msg):
        if Logger.DEBUG_FLAG:
            print("\x1b[33m" + msg + "\x1b[0m") 