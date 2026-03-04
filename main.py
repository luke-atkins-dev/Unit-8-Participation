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

def main():
    pass

if __name__ == "__main__":
    main()