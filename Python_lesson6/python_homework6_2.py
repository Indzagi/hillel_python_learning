my_time = int(input("Enter the number of seconds from 0 to 8639999 to convert to time format: "))

if 0 <= my_time < 8640000:
    days = divmod(my_time, 86400)
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    seconds = minutes[1]
    my_null_h = "0" if hours[0] < 10 else ""
    my_null_min = "0" if minutes[0] < 10 else ""
    my_null_sec = "0" if seconds < 10 else ""
    day_end = (0, 5, 6, 7, 8, 9)
    if days[0] % 10 == 1 and days[0] != 11:
        text_days = "день"
    elif days[0] % 10 in day_end or 5 <= days[0] <= 19:
        text_days = "днів"
    else:
        text_days = "дні"
    print(f"{days[0]} {text_days}, {my_null_h}{hours[0]}:{my_null_min}{minutes[0]}:{my_null_sec}{seconds}")
else:
    print("The value is outside the available range")
