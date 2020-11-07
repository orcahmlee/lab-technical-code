import sys
from datetime import datetime


def calc(start_date: str, end_date: str, include: bool = False) -> int:
    date_format = '%Y-%m-%d'
    start_d = datetime.strptime(start_date, date_format)
    end_d = datetime.strptime(end_date, date_format)
    diff = end_d - start_d

    if include:
        return diff.days + 1
    else:
        return diff.days


if __name__ == "__main__":
    res = calc(sys.argv[1], sys.argv[2])
    print(f'{res} days.')
