def main():
    def convert_length(feet, conversion_factor):
        return feet * conversion_factor

    conversions = [
        ("inches", 12),
        ("yards", 1/3),
        ("miles", 1/5280),
        ("millimeters", 304.8),
        ("centimeters", 30.48),
        ("meters", 0.3048),
        ("kilometers", 0.0003048),
    ]

    print("Enter the length in feet:")
    feet = float(input())

    print("Choose the conversion option:")
    for i, (unit, _) in enumerate(conversions, 1):
        print(f"{i}: Convert to {unit}")

    choice = int(input())

    unit, factor = conversions[choice - 1]
    converted_length = convert_length(feet, factor)
    print(f"{feet} feet is {converted_length} {unit}")

main()