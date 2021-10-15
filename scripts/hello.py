#!/usr/bin/env python3
from dev_aberto import hello
import babel.dates
import gettext
import datetime

gettext.install('cli',localedir='locale')

if __name__ == '__main__':
    date, name = hello()
    date_translate = babel.dates.format_datetime(datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z'))

    print(_('Último commit feito em:'), date_translate, _(' por'), name)
