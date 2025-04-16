import keyword
print(keyword.kwlist)

import calendar
print(calendar.month(2019, 3))

import datetime
now =  datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

import tkinter as tk
base = tk.Tk()

h = " Hello world! ";

print(h.rfind("e"))