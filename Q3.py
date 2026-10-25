shape = input("Enter shape: ").lower()
if shape == "square":
    side = float(input("Enter side: "))
    area = side*side

elif shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length*width

elif shape == "circle":
    radius = float(input("Enter radius: "))
    area = 3.14*radius**2

elif shape == 'triangle':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = base*height/2

else:
    print("Invalid shape")
    area = 0

print("area =",round(area,3))