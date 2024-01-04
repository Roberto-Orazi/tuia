### Dates ###
from datetime import datetime

now = datetime.now()
print(
    f"Hoy es {now.day} del mes {now.month} del año {now.year} y son las {now.hour}:{now.minute}"
)

timestamp = now.timestamp()
print(timestamp)

year_2023 = datetime(2023, 1, 1)
print(year_2023)


def print_date(date):
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.day)
    print(date.month)
    print(date.year)
    print(date.timestamp())


print_date(now)


from datetime import time

current_time = time(21, 6, 20)


def print_time(time):
    print(time.hour)
    print(time.minute)
    print(time.second)


print_time(current_time)


from datetime import date

current_date = date.today()


def print_curr_date(date):
    print(date.day)
    print(date.month)
    print(date.year)


print_curr_date(current_date)


tomorrow = date(current_date.year, current_date.month, current_date.day + 1)

print(tomorrow.day)


diff = now - year_2023
print(diff)
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
finish_timedelta = timedelta(300, 100, 100, weeks=13)

print(finish_timedelta - start_timedelta)
print(finish_timedelta + start_timedelta)
print(finish_timedelta / start_timedelta)

