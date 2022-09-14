import time

class Timer:
    __startTime = 0
    __endTime = 0
    def start(self):
        self.__startTime = time.time()

    def end(self):
        self.__endTime = time.time()
        print(self.__endTime -  self.__startTime)