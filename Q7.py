budget = float(input("Enter budget: "))
season = input("Enter season: ")
if budget <= 100:
    place = "Bulgaria"
    if season == "summer":
        money = budget*0.30
    else:
        money = budget*0.70

elif budget <= 1000:
    place = "Balkans"
    if season == "summer":
        money = budget*0.40
    else:
        money = budget*0.80

else:
    place = "Europe"
    money = budget*0.90

print("vacation place",place)
print("money spent:", round(money),"BGN")