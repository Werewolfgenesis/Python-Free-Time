import calendar

year = input("Input year: ")
for value in range(1,13):
    print(calendar.month(int(year), value))
