class FourDigitYearConverter21Century:
    regex = '2{1}0{1}[0, 1, 2]{1}[0-9]{1}'

    def __str__(self):
        return self.regex

    def to_python(self, value) -> int:
        return int(value)

    def to_url(self, value) -> str:
        return '%04d' % value

class FourDigitYearConverter20Century:
    regex = '1{1}9{1}[0-9]{1}[0-9]{1}'

    def __str__(self):
        return self.regex

    def to_python(self, value) -> int:
        return int(value)

    def to_url(self, value) -> str:
        return '%04d' % value
