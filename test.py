import os

def set_path():
    current_folder = os.path.dirname(os.path.realpath(__file__))
    main_folder = 'Reading Material'
    new_folder = 'Week ' + str(1)
    return [current_folder, main_folder, new_folder]


print(os.path.join(*set_path()))