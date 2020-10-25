d = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30, 'oct': 31,
     'nov': 30, 'dec': 31}
months = list(d.keys())


def date(s):
    date = ''
    for i in s[:2]:
        if i.isdigit():
            date += i
    return int(date)


def year(s):
    year = s[-1:-5:-1]
    return int(year[::-1])


def leap(s):
    year1 = year(s)
    if year1 % 100 == 0:
        if year1 % 400 == 0:
            return True
    elif year1 % 4 == 0:
        return True


def month(s):
    month = ''
    for i in s:
        if i.isalpha():
            i = i.lower()
            month += i
    return month[:3]


def days_prev_months(s):
    days = 0
    r = months.index(months(s))
    if leap(s) and r > 1:
        days += 1
    for i in range(r):
        days += d[months[i]]
    return days


def days_total(s):
    return days_prev_months(s) + date(s)


def days_string(s):
    return '0' * (3 - len(str(days_total(s)))) + str(days_total(s))


def final(s):
    return str(year) + days_string(s)
