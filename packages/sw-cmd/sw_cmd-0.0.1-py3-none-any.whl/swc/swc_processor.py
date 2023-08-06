from datetime import datetime


class SwcProcessor:
    def __init__(self):
        pass

    def start(self):
        start = datetime.now()
        while True:
            now = datetime.now()
            print("\r" + str(now - start), end="")
