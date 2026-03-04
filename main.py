"""
Name: Temperature converter
Purpose: Converts temperature from celsius to fahrenheit
Date: 3/4/2026
Author: Luke Atkins
Starter Code: No starter code used
"""

def get_celsius() -> float:
    cel = input("Enter temperature in Celsius: ")
    try:
        return float(cel)
    except:
        print("Invalid input")
    return get_celsius()

def output_conversion(celsius: float, fahrenheit: float):
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

def main():
    celsius = get_celsius()
    output_conversion(0, celsius)

if __name__ == "__main__":
    main()