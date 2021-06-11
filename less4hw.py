class Factorial:

    def __init__(self, num):
        self._num = num
        self.factorial = self._factorial()

    def _factorial(self, f_sum=1):
        if self._num == 0:
            return f_sum
        f_sum = f_sum * self._num
        self._num -= 1
        return self._factorial(f_sum)


f = Factorial(4)
print(f.factorial)
f.factorial = 20
print(f.factorial)


f2 = Factorial(30)