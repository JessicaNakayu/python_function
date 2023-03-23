#conversion functions
def inches_to_mm(length_in_inches):
    length_in_mm = length_in_inches * 25.4
    return length_in_mm

def mm_to_inches(length_in_mm):
    length_in_inches = length_in_mm / 25.4
    return length_in_inches

# get the length from the user
conversion_direction = input('Enter conversion direction (in -> mm or mm -> in): ')

length = float(input("Enter length: "))

#convert the length to the correct function
#in to mm
if conversion_direction == 'in -> mm':
    converted_len = inches_to_mm(length)
    print(f'{length} inches = {converted_len} mm')
    #do in to mm
elif conversion_direction == 'mm -> in':
    converted_len = mm_to_inches(length)
    print(f'{length} mm = {converted_len} inches')
    #do mm to in
else:
    print("Invalid conversion direction")

