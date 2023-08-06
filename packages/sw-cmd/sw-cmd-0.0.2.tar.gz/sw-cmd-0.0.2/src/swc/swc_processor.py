from datetime import datetime
from time import sleep


class SwcProcessor:
    def __init__(self):
        pass

    def start(self):
        start = datetime.now()
        while True:
            now = datetime.now()
            sleep(0.1)
            print("\r" + str(now - start), end="")
