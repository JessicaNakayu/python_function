# Conversion Calculator development:
#I want to create a conversion calculator that converts at least 3-7 conversions for different values
# Some ideas:
# inches to millimeters and then reverse
# feet to meters and the reverse
# Celsius to Fahrenheit and the reverse
# some format ideas for my conversions are:
# inches to millimeter (this is quite long)
# in to mm (this on it shorter)
# in -> mm (this one has an arrow so it seems a bit more direct in what direction it is going)
#
#I should put them into functions like this:
#  def inches_to_mm(length_in_inches):
 #     length_in_mm = length_in_inches * 25.4
  #    return length_in_mm

# Once I have the functions defined for my above conversions I need something to actually converted the conversion and print it out.
# another function would most likely be a goood idea:
# I could start it like this:
#def perform_conversion(value, conversion_direction):
 #   if conversion_direction == 'in -> mm':
  #      converted_value = inches_to_mm(value)
   #     value_unit = "inches"
    #    converted_value_unit = "mm"

#And my print statemnet should include the the final results
# print(f'{value} {value_unit} = {converted_value:.2f} {converted_value_unit}'))
# I dont want a huge value so I am going to put it at 2 decimal places.

# I also need to know what conversion they want to do and what value they want to convert plus I dont need an endless loop so they should be able to leave the claculator as well
# to exit or quit we could do x or q, lets do q for quit.
# I also want the claculator to know my conversion so I will have them in a listto compare them too
#conversion_list = ['in -> mm', 'mm -> in', 'ft -> m', 'm -> ft', 'C -> F', 'F -> C']
# the list needs to show up formated in the conversion they want to do.
#input('Enter conversion direction ({}), or "q" to quit: '.format(', '.join(conversion_list)))
#and
#float(input("Enter value to be converted: "))
# noticed that if I enter a digit that is not a number I get a value error so I need to add an exception instead of my code breaking.
# it would look like:
#try:
#   value = ..... (what I have written here for input)
#   except ValueError:
#           Print("Invalid input for value")
#           continue
