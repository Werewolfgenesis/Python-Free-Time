import random
import string

letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

def get_pass_lenght():
    length = input("Choose pass length: ")
    return int(length)

def generate_pass(length = 6):
    to_print = f'{letters}{numbers}{punctuation}'
    to_print = list(to_print)
    random.shuffle(to_print)
    password = random.choices(to_print, k=length)
    password = ''.join(password)
    return password

def start_program():
    pass_length = get_pass_lenght()
    print_it = generate_pass(pass_length)
    print("Your randomly generated password is ", print_it)

start_program()
