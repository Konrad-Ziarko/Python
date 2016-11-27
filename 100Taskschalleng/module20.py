class SevenIterator:
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)
    def generate(self, low, up):
        while low <= up:
            if low % 7:
                low = low + 1
            elif not low % 7:
                yield low
                low+=7
obj = SevenIterator()
for i in obj.generate(0, 200):
    print (i)
