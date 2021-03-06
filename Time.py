import pytz
from datetime import datetime


def day_of_week(today=True, custom_day=None, flag=True):
    current = datetime.now(pytz.timezone('Asia/Kolkata'))
    day = current.weekday()
    if today is True:
        if day == 6:
            day = 0
        else:
            day += 1
    else:
        if day == 5:
            day = 0
        elif day == 6:
            day = 1
        else:
            day += 2
    if flag is True:
        if custom_day is None:
            if 1 <= day <= 3:
                noc = 5
            else:
                noc = 4
            return day, noc
        else:
            if 1 <= custom_day <= 3:
                noc = 5
            else:
                noc = 4
            return custom_day, noc
    else:
        return day


def curr_time():
    current = datetime.now(pytz.timezone('Asia/Kolkata'))
    hour = int(current.time().strftime('%H'))
    minutes = int(current.time().strftime('%M'))
    if 0 <= hour <= 15:
        time = hour
    elif hour == 16:
        if 0 <= minutes <= 29:
            time = hour
        else:
            time = hour + 1
    else:
        time = hour + 1
    return time


def date():
    current = datetime.now(pytz.timezone('Asia/Kolkata'))
    d = current.date().strftime('%d')
    m = current.date().strftime('%m')
    y = current.date().strftime('%Y')
    a = ['AM', 'PM']
    H = int(current.time().strftime('%H')) % 12
    if H == '0':
        H = '12'
    M = int(current.time().strftime('%M'))
    ampm = a[int(current.time().strftime('%H')) // 12]
    return f"{d}.{m}.{y} - {H}:{M} {ampm}"