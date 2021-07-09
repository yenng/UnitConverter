"""
    0. Number system
    1. Temperature
    2. Weight
    3. Length
    4. Area
    5. Angle
"""

def get_type(unit_type):
    """Return the unit types with user's choice"""
    
    # Create a dictionary with unit types.
    type_dir = {
        0: ["Dec", "Bin", "Hex", "Oct"],
        1: ["Celsius(°C)", "Fahrenheit(°F)", "Kelvin(K)"],
        2: ["Kilogram(kg)", "Gram(g)", "Pound(lbs)", "Ounce(oz)"],
        3: ["Meter(m)", "Foot(ft)", "Inch(in)", "Mile(mi)"],
        4: ["Square meter(m^2)", "Square foot(ft^2)"],
        5: ["Degree(°)", "Radian(rad)", "Pi Radian(π rad)"],
    }
    units = type_dir.get(unit_type, None)

    # Raise an error if user input an invalid value.
    if units == None:
        raise ValueError("Choice not available in list. Restart the program and choose from the list.")
    return units        

def print_unit_choice(units):
    """Print the choice for user to choose."""

    print("Unit list:")
    # Loop through the unit types that get previously.
    for i, unit in enumerate(units):
        print("{0} -> {1}".format(i, unit))
        # Add value to unit dictionary.
        
    # Get user's input for source unit and target unit.
    try:
        source_unit = int(input("From: \t"))
        target_unit = int(input("To: \t"))
    except ValueError:
        raise ValueError("Choice not available in list. Restart the program and choose from the list.")
    if source_unit not in range(len(units)) or target_unit not in range(len(units)):
        raise ValueError("Choice not available in list. Restart the program and choose from the list.")

    return source_unit, target_unit

def number_system_converter(source_unit, target_unit, value):
    """Converter for number system."""
    
    dic = {0: [10,'d'], #For Decimal
           1: [2, 'b'], #For Binary
           2: [16,'x'], #For Hexadecimal
           3: [8, 'o']} #For Octal
    
    # Cast the input value to decimal.
    value_int = int(value,dic.get(source_unit)[0])
    
    result = format(value_int, dic.get(target_unit)[1])
    return result

def temp_converter(source_unit, target_unit, value):
    """Converter for temperature."""
    
    value = float(value)
    dic_to_celcius = {0: lambda x: round(x,2),              # Celsius to Celsius
                      1: lambda x: round((x-32)*5.0/9.0,2), # Fahrenheit to Celsius
                      2: lambda x: round(x-273.15,2)}       # Kelvin to Celsius

    value_celsius = dic_to_celcius.get(source_unit)(value)

    dic_to_target = {0: lambda x: round(x,2),               # Celsius to Celsius
                     1: lambda x: round(x*9.0/5.0+32,2),    # Celsius to Fahrenheit
                     2: lambda x: round(x+273.15,2)}        # Celsius to Kelvin

    result = dic_to_target.get(target_unit)(value_celsius)
    return result

def converter(unit_type, source_unit, target_unit, value):
    """Main converter for all types."""

    # Create the ratio 
    dic_weight = {0: 1000.0,    # For kg to g
                  1: 1.0,       # For g to g
                  2: 453.59,    # For lbs to g
                  3: 28.35}     # For oz to g
    
    dic_length = {0: 1.0,       # For m to m
                  1: 0.3048,    # For ft to m
                  2: 0.0254,    # For in to m
                  3: 1609.34}   # For mile to m
    
    dic_area = {0: 1.0,     # For m^2 to m^2
                1: 0.0929}  # For ft^2 to m^2
    
    dic_angle = {0: 1.0,        # For ° to °
                 1: 57.2958,    # For rad to °
                 2: 180}        # For pi rad to °
    
    converter_list = [number_system_converter,
                      temp_converter,
                      dic_weight,
                      dic_length,
                      dic_area,
                      dic_angle]
    
    if unit_type < 2:
        result = converter_list[unit_type](source_unit, target_unit, value)
    else:
        value = float(value)
        result = round(value*converter_list[unit_type].get(source_unit)/converter_list[unit_type].get(target_unit), 2)
    return result
                      
def main():

    print("UNIT CONVERTER.\n")
    print("What type of conversion?")
    print("0 -> Number system")
    print("1 -> Temperature")
    print("2 -> Weight")
    print("3 -> Length")
    print("4 -> Area")
    print("5 -> Angle")
    unit_type = input("Please choose a unit type from list above:")

    try:
        unit_type = int(unit_type)
    except ValueError:
        raise ValueError("Please enter the number from the list given.")
    units = get_type(unit_type)
    source_unit, target_unit = print_unit_choice(units)

    value = input("Value: ")
    result = converter(unit_type, source_unit, target_unit, value)

    print("Result: {0} {1} equals to {2} {3}".format(value, units[source_unit],result, units[target_unit]))
    


if __name__ == "__main__":
    main()
