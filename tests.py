# class Animal:
#     def __init__(self, voice):
#         self.voice = voice
#
#
# cat = Animal('Meow')
# print(cat.voice)  # => Meow
#
# dog = Animal('Woof')
# print(dog.voice)  # => Woof


def get_input():
    """This function prompts the user for input and returns it"""
    user_input = input("Enter a value: ")
    return user_input


def convert_to_int(user_input):
    """This function takes a string as input and converts it to an integer"""
    num = int(user_input)
    return num


def apply_operation(num):
    """This function takes an integer as input and applies an operation (e.g. multiplying by 2)"""
    result = num * 2
    return result


def convert_to_str(result):
    """This function takes an integer as input and converts it to a string"""
    string = str(result)
    return string


def print_output(string):
    """This function takes a string as input and prints it to the console"""
    print("The result is:", string)


def main():
    """This function is the main function that calls other functions"""
    user_input = get_input()
    num = convert_to_int(user_input)
    result = apply_operation(num)
    string = convert_to_str(result)
    print_output(string)


# Call the main function to run the program
main()
