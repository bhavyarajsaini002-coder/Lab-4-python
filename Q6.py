holidays = int(input("Enter holidays: "))
working_days = 365-holidays
play_time = working_days*63+holidays*127
difference = abs(30000-play_time)
if play_time > 30000:
    print("Tom will run away")
    print("Difference=",difference,"minutes")
else:
    print("Tom sleep well")
    print("Difference=",difference,"minutes")