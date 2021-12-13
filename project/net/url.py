import requests

class Uri:
    def __init__(self, url):
        self.url = url
        self.method = "GET"
        self.headers = {}

    def get(self):
        if self.url is None:
            raise Exception("URL is not defined")

        response  = requests.get(self.url)
        return response.text

    
    def post(self):
        if self.url is None:
            raise Exception("URL is not defined")

        response  = requests.post(self.url)
        return response.text

    def check_true_type_font(self):
        if self.url is None:
            raise Exception("URL is not defined")

        response  = requests.get(self.url)
        if "font/ttf" in response.headers["Content-Type"]:
            return response
        else:
            raise Exception("Content-Type is not font/ttf")
