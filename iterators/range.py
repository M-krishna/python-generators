class Range:
    def __init__(self, start, end):
        self.end = end
        self.current = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        while self.current < self.end:
            return self.current
        raise StopIteration
