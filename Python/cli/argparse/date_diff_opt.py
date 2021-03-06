from datetime import datetime
from argparse import ArgumentParser


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
    parser = ArgumentParser()
    parser.add_argument(
        '-s', '--start_date', type=str,
        dest='start', required=True,
        help='The start date'
    )
    parser.add_argument(
        '-e', '--end_date', type=str,
        dest='end', required=True,
        help='The end date'
    )
    parser.add_argument(
        '-i', '--include', action='store_true',
        dest='include',
        help='Include end date in calculation (1 day is added)'
    )
    args = parser.parse_args()
    res = calc(args.start, args.end, args.include)
    print(f'The duration between {args.start} and {args.end} is {res} days.')
