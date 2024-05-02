import datetime
import calendar

def calculate_optimal_days_from_console():
    
    N = int(input())
    year = int(input())
    holidays = []
    for _ in range(N):
        day, month = input().split()
        holidays.append((day, month))
    first_day_of_year = input()

   
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    month_names = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                   "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    
    
    holiday_dates = [datetime.date(year, month_names[month], int(day)) for day, month in holidays]

    
    weekday_counts = {day: 52 for day in weekdays}
    extra_days = (datetime.date(year, 1, 1) + datetime.timedelta(days=365 + calendar.isleap(year) - 1)).weekday() - datetime.date(year, 1, 1).weekday()
    if extra_days < 0:
        extra_days += 7
    for i in range(extra_days + 1):
        weekday_counts[weekdays[(weekdays.index(first_day_of_year) + i) % 7]] += 1

    
    holiday_weekday_counts = {day: 0 for day in weekdays}
    for date in holiday_dates:
        holiday_weekday_counts[weekdays[date.weekday()]] += 1

    
    effective_free_days = {}
    for day in weekdays:
        effective_days_off = weekday_counts[day] + sum(holiday_weekday_counts[d] for d in weekdays if d != day)
        effective_free_days[day] = effective_days_off

    best_day = max(effective_free_days, key=effective_free_days.get)
    worst_day = min(effective_free_days, key=effective_free_days.get)

    return best_day, worst_day


best_day, worst_day = calculate_optimal_days_from_console()
print(best_day, worst_day)
