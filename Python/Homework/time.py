from datetime import datetime, timedelta

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
d = {'Los Angeles': '-08:00', 'New York': '-05:00', 'London': '+00:00', 'Rome': '+01:00', 'Beijing': '+08:00',
     'Canberra': '+10:00'}


def julian(city1, s, city2):
    s = s.replace(",", "").replace(":", " ")
    l = list(s.split())
    month = months.index(l[0]) + 1
    date = int(l[1])
    year = int(l[2])
    hours = int(l[3])
    mins = int(l[4])
    curr_time = datetime(year, month, date, hours, mins)
    if d[city1][0] == '+':
        if d[city2][0] == '+':
            p2 = int(d[city2][-2:]) - int(d[city1][-2:])
            p1 = int(d[city2][1:3]) - int(d[city1][1:3])
        else:
            p2 = - int(d[city2][-2:]) - int(d[city1][-2:])
            p1 = - int(d[city2][1:3]) - int(d[city1][1:3])
    else:
        if d[city2][0] == '+':
            p2 = int(d[city2][-2:]) + int(d[city1][-2:])
            p1 = int(d[city2][1:3]) + int(d[city1][1:3])
        else:
            p2 = - int(d[city2][-2:]) + int(d[city1][-2:])
            p1 = - int(d[city2][1:3]) + int(d[city1][1:3])
    new_time = str(curr_time + timedelta(hours=p1, minutes=p2))
    return new_time[:-3]


print(julian('Los Angeles', 'April 1, 2011 23:23', 'Canberra'))
