"""
Name: Temperature converter
Purpose: Converts temperature from celsius to fahrenheit
Date: 3/4/2026
Author: Luke Atkins
Starter Code: No starter code used
"""

# Task function (converts and returns)
def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts celsius to fahrenheit

    Args:
        celsius: celsius to convert to fahrenheit
    Returns:
        float: (conversion)
    """
    return (celsius * (9/5)) + 32

# Side-effect (Receives input and prints)
def get_celsius() -> float:
    """
    Forces user to enter valid float (negative supported, no range limit)

    Args:
        None
    Returns:
        float: (The float representation of the celsius to be converted)
    """
    cel = input("Enter temperature in Celsius: ")
    try:
        return float(cel)
    except:
        print("Invalid input")
    return get_celsius()

# Side-effect (Prints to the console)
def output_conversion(celsius: float, fahrenheit: float) -> None:
    """
    Outputs original input and conversion to output stream

    Args:
        celsius: (float) The celsius originally provided
        fahrenheit: (float) the conversion
    Returns:
        None
    """
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Orchestrator (Main is always orchestrator
def main() -> None:
    """
    Main entry for the program

    Args:
        None
    Returns:
        None
    """
    celsius = get_celsius()
    convert = celsius_to_fahrenheit(celsius)
    output_conversion(celsius, convert)

if __name__ == "__main__":
    main()