import datetime
year = 1901
month = 1
day = 1

dates =[]
date_days = []

for i in range(100):
    for i in range (1,13):
        month = i
        x = datetime.datetime(year,month,day)
        dates.append(x)
    year += 1
    
for i in range(len(dates)):
    x = dates[i].strftime("%A")
    date_days.append(x)

sundays = [x for x in date_days if x == 'Sunday']
print(dates[1])
print(len(sundays))