"""
# Author: biud436
"""
class Font:
    def __init__(self, name, size=12):
        self.name = name
        self.size = size
        self.color = (0, 0, 0)
        self.bold = False
        self.italic = False
        self.underline = False
        self.strikethrough = False

    def set_color(self, color):
        self.color = color
    
    def set_bold(self, bold):
        self.bold = bold

    def set_italic(self, italic):
        self.italic = italic

    def set_underline(self, underline):
        self.underline = underline

    def set_strikethrough(self, strikethrough):
        self.strikethrough = strikethrough

    def set_size(self, size):
        self.size = size

    def set_name(self, name):
        self.name = name

    def parse(self, file_name):
        f = open(file_name, 'r')
        for line in f:
            puts(line)
        f.close()
