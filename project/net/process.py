
import os
import sys
import time
import subprocess

class FontDownloader:
    def __init__(self, url) -> None:
        
        # wget run
        if sys.platform == 'darwin' or sys.platform == "linux":
            self.wget = 'curl'
        elif sys.platform == 'win32':
            self.wget = 'powershell.exe wget'

        # terminal command called "aria2c" exists?
        if self.check_araic2c():
           self.wget = 'aria2c'

        # wget url
        self.wget_url = url or 'https://github.com/biud436/font-parser/raw/main/res/NanumGothicCoding.ttf'

        # os exec and redirect to stdout
        p = subprocess.Popen(self.wget + ' ' + self.wget_url, shell=True, stdout=sys.stdout, stderr=sys.stderr)
        
        # wait for process end
        p.wait()

        filename = self.wget_url.split('/')[-1]

        if sys.platform == 'darwin' or sys.platform == "linux":
            os.system('cp ' + filename + ' ./res/c_' + filename)
        elif sys.platform == 'win32':
            os.system('copy ' + filename + ' ./res/c_' + filename)


    def check_araic2c(self):
        result = 0

        if sys.platform == 'darwin' or sys.platform == "linux":
            result = os.system('aria2c > /dev/null 2>&1')
        else:
            result  = os.system('aria2c > nul 2>&1')

        if result:
            return True
        else:
            return False


            