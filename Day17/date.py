from datetime import date, time, datetime

now = datetime.now()

print(now.strftime('%d/%m/%y %H:%M:%S'))

print(now.strftime('%d/%m/%y %I:%M:%S'))

print(now.strftime('%d %b %y %I:%M:%S'))

print(now.strftime('%d %B %y %I:%M:%S %p'))

print(now.strftime('%A, %d %B %y %I:%M:%S %p'))   