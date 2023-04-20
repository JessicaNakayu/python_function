#conversion functions for my conversion calculator
#conversion to mm from inches
def inches_to_mm(length_in_inches):
    length_in_mm = length_in_inches * 25.4
    return length_in_mm
#conversion to inches from mm
def mm_to_inches(length_in_mm):
    length_in_inches = length_in_mm / 25.4
    return length_in_inches
#conversion to meters from feet
def feet_to_meters(length_in_feet):
    length_in_meters = length_in_feet * 0.3048
    return length_in_meters
#conversion to feet from meters
def meters_to_feet(length_in_meters):
    length_in_feet = length_in_meters / 0.3048
    return length_in_feet
#conversion to Celsius from Fahrenheit
def F_to_C(temp_in_F):
    temp_in_C = (temp_in_F - 32) * 5/9
    return temp_in_C
#conversion to Fahrenheit to Celsius
def C_to_F(temp_in_C):
    temp_in_F = (temp_in_C * 9/5 +32)
    return temp_in_F
#function for the print results 
def print_results(value, converted_value, value_unit, converted_value_unit):
    print(f'{value} {value_unit} = {converted_value:.2f} {converted_value_unit}')
    value_unit = ""
    converted_value_unit = ""
# if else statments for the conversion direction so we output the right conversion.
def perform_conversion(value, conversion_direction):
   
    if conversion_direction == 'in -> mm':
        converted_value = inches_to_mm(value)
        value_unit = "inches"
        converted_value_unit = "mm"
    elif conversion_direction == 'mm -> in':
        converted_value = mm_to_inches(value)
        value_unit = "mm"
        converted_value_unit = "inches"
    elif conversion_direction == 'ft -> m':
        converted_value = feet_to_meters(value)
        value_unit = "ft"
        converted_value_unit = "m"
    elif conversion_direction == 'm -> ft':
        converted_value = meters_to_feet(value)
        value_unit = "m"
        converted_value_unit = "ft"
    elif conversion_direction == 'C -> F':
        converted_value = C_to_F(value)
        value_unit = "C"
        converted_value_unit = "F"
    elif conversion_direction == 'F -> C':
        converted_value = F_to_C(value)
        value_unit = "F"
        converted_value_unit = "C"
    else:
        print("Invalid conversion direction")
    
    

    
    return (value, converted_value, value_unit, converted_value_unit)
# list of my conversions
conversion_list = ['in -> mm', 'mm -> in', 'ft -> m', 'm -> ft', 'C -> F', 'F -> C']

while True:
    # get the conversion direction from the user
    conversion_direction = input('Enter conversion direction ({}), or "q" to quit: '.format(', '.join(conversion_list)))
    if conversion_direction == "q":
        break

    # check if the conversion direction is valid
    if conversion_direction not in conversion_list:
        print("Invalid conversion direction, please enter valid conversion direction.")
        continue

    # get the value to be converted from the user
    try:
        value = float(input("Enter value to be converted: "))
    except ValueError:
        print("Invalid input for value")
        continue

    # perform the conversion and print the results
    conversion_result = perform_conversion(value, conversion_direction)
    if conversion_result is not None:
        print_results(*conversion_result)

#After exiting the calculator have an exiting statement.
print('Thanks for using The Cool Conversion Calculator!')
