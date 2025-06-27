import argparse

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number.")
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a number.")
    return (fahrenheit - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(description="Convert between Celsius and Fahrenheit.")
    parser.add_argument("temperature", type=float, help="The temperature to convert.")
    parser.add_argument("-u", "--unit", choices=["C", "F"], default="C", help="The input unit (C or F). Defaults to Celsius.")
    args = parser.parse_args()

    if args.unit == "C":
        result = celsius_to_fahrenheit(args.temperature)
        print(f"{args.temperature}°C is equal to {result}°F")
    else:
        result = fahrenheit_to_celsius(args.temperature)
        print(f"{args.temperature}°F is equal to {result}°C")

if __name__ == "__main__":
    main()
