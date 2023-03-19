import random

class Robot(object):
    def __init__(self):
        self.legacy = set()
        self.reset()

    def reset(self):
        while True:
            self.name = ''.join([chr(random.randint(65, 90)) for i in range(2)]) \
                + ''.join([str(random.randint(0, 9)) for i in range(3)])
            if self.name not in self.legacy:
                break
        self.legacy.add(self.name)


