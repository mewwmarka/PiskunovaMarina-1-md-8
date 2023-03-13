
from datetime import datetime


def is_date_magic(string_date: str) -> bool:
    result_date = datetime.strptime(string_date, '%d.%m.%Y')
    return result_date.day * result_date.month == int(result_date.strftime('%y'))


print(is_date_magic('04.11.2044'))
