import os
from joblib import Parallel, delayed
import pickle

def print_dir(directory_path, max_items_to_return = 15):
    dir_contents = os.listdir(directory_path)
    str_to_print = '{:>12}  {:>12}'.format('Name', 'Full Path')
    i = 1
    for child in dir_contents:
        if max_items_to_return is not None:
            if i > max_items_to_return:
                break
        full_child_path = os.path.join(directory_path, child)
        str_to_print = str_to_print + '\n' + '{:>12}  {:>12}'.format(child, full_child_path)
        i = i + 1
    number_of_items = len(dir_contents)
    #Only report a max number of items less than or equal to the number of items in the directory
    if max_items_to_return > number_of_items:
        max_items_to_return = len(dir_contents)
    #Convert variables to strings to allow propper concatonation
    max_items_to_return = str(max_items_to_return)
    number_of_items = str(number_of_items)
    str_to_print = str_to_print + '\n' + 'Showing ' + max_items_to_return + ' of ' + number_of_items + ' items'
    print(str_to_print)

def print_file (file_path, line_limit = 30):
    with open(file_path) as file:
        lines_read = 0
        for line in file.readlines():
            if (lines_read < line_limit):
                print(line)
                lines_read = lines_read + 1
            else:
                break

def pickle_as_file (object, file_path):
    binary_data = pickle.dumps(object)
    with open(file_path, 'wb') as file:
        file.write(binary_data)

def unpickle_from_file (file_path):
    binary_data = ''
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    object = pickle.loads(binary_data)