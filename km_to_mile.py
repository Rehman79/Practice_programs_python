print("1. Kilometer to miles")
print("2. Miles to kilometers")
op = input("Enter the operation number: ")

match op:
    case '1':
        km = float(input("Enter the kilometres: "))
        form = 0.62137119 * km
        print(f"In miles, the distance is: {form:.2f}")
    case '2':
        miles = float(input("Enter the miles: "))
        form = 1.60934 * miles
        print(f"In kilometers, the distance is: {form:.2f}")
