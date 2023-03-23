#functions -- Block of code that is designed 
#             to preform a specific task
#          - built in functions
#          - create custom functions
#          - break up our code into smaller -- reusable parts
#def say_hello(name):
#    print('Hello, ' + name + '!!')
#
#calling the function
#say_hello('Jessica')

def add_numbers(x, y):
    return x + y
def calculate_total(x, y, z):
    total = add_numbers(x, y)
    sum = add_numbers(total, z)
    return sum

results = calculate_total(3, 4, 5)
print(results)

def say_hello(name = 'World!'):
    print('Hello ' + name)
say_hello()
say_hello('Jessica')
