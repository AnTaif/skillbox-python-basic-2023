class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"День: {self.day}    Месяц: {self.month}    Год: {self.year}"

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        if cls.is_date_valid(date_str):
            return cls(day, month, year)
        else:
            raise ValueError("Некорректная дата")

    @staticmethod
    def is_date_valid(date_str):
        day, month, year = map(int, date_str.split('-'))
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
        else:
            return False

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
