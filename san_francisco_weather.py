import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/san_francisco_weather_comparison.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#second_filename = 'data/death_valley_2018_simple.csv'
#with open(second_filename) as f_obj:
#    reads = csv.reader(f_obj)
#    head_row = next(reads)
#    highs_t, lows_t, dates_d = [], [], []
#    for i in reads:
#        current_date_d = datetime.strptime(i[2], '%Y-%m-%d')
#        high_t = int(i[6])
#        low_t = int(i[5])
#        dates_d.append(current_date_d)
#        highs_t.append(high_t)
#        lows_t.append(low_t)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='cyan', alpha=0.2)

title = "Daily high and low temperatures - 2022-2023\nSan Francisco, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
