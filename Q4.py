hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
if 0 <= hours < 24 and 0 <= minutes < 60:
    minutes += 15

    if minutes >= 60:
        minutes -= 60
        hours += 1

        if hours == 24:
            hous = 0
    print(f"Time after 15 minutes will be {hours:02d}:{minutes:02d}")
else:
    print("Invalid input")