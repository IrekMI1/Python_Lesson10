class MinStat:
    def __init__(self):
        self.numbers = []
        self.answer = None

    def operation(self):
        self.answer = min(self.numbers)

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        if self.numbers:
            self.operation()
        return self.answer


class MaxStat(MinStat):
    def operation(self):
        self.answer = max(self.numbers)


class AverageStat(MinStat):
    def operation(self):
        self.answer = sum(self.numbers) / len(self.numbers)


values = [1, 2, 4, 5]
mins = MinStat()
maxs = MaxStat()
average = AverageStat()

for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), '{:05.3f}'.format(average.result()))
