import re


def coefficient_list(s):
    s = s.replace('-', '+-').replace('$', '')
    extra_spaces = re.compile(' *[+] *')
    l = extra_spaces.sub('+', s).split('+')
    return l if l[0] != '' else l[1:]


def mathematician_form(s):
    A = coefficient_list(s)
    return ' + '.join(reversed(A))


def remove_extra_plus(s):
    return s.replace('+ -', '-')


def latex(s):
    return '$' + remove_extra_plus(mathematician_form(s)) + '$'


print(latex('$-3x^4-7x^3+21x-17$'))
print(latex('$+3x^4 -7x^3 + 21x + 17$'))
