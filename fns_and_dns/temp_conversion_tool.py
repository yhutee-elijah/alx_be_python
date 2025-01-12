FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = input("Enter the temperature to convert: ")
        if not temperature.replace(".", "").isdigit():
            raise ValueError("Invalid temperature. please enter a number")
        temperature = float(temperature)
        unit = input("Is this temperature in Celsius or Farenheit? (C/F): ").strip().upper()
        if unit == "F":
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}F is {converted_temperature:.2f}C")
        elif unit == "C":
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celcius or 'F'for Fahrenheit")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()