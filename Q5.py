km = float(input("Enter kilometres: "))
period = input("Enter day or night: ")
if period == 'day':
    taxi = 33.58+km*37.89
else:
    taxi = 33.58+km*43.17
if km >= 20:
    bus = km*4.32
else:
    bus = 999999
if km >= 100:
    train = km*2.88
else:
    train = 999999

cheapest = min(taxi,bus,train)
print("cheapest price=",round(cheapest,2))