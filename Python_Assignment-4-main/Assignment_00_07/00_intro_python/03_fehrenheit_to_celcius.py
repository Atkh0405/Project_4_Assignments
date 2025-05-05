def main():
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    result = (Fahrenheit - 32) * 5 / 9
    print(f"Temperature {Fahrenheit}°F = {result:.2f}°C")

main()
