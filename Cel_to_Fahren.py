print("1. Celcius to Fahrenheit")
print("2. Fahrenheit to Celcius")
op = input("Enter the operation number: ")

match op:
    case '1':
        cel = float(input("Enter the Celcius: "))
        form = (cel*(9/5)+32)
        print(f"In Celcius, the temperature is: {form:.2f}")
    case '2':
        fah = float(input("Enter the Fahrenheit: "))
        form = ((fah-32)*5/9)
        print(f"In Fahrenheit, the temperature is: {form:.2f}")