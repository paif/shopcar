import datetime

def parse_date(date_string):
    year, month, day = date_string.split(".")
    return datetime.date(int(year), int(month), int(day))


if __name__ == '__main__':
    print(parse_date("2013.11.12"))