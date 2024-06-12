"""
File: compute_average.py
------------------------
A simple list practice: Load a list of nubmer from a file and return the average
"""

def main():
    number_list = load_numbers_from_file("numbers.txt")
    sum_of_list = sum(number_list)
    len_of_list = len(number_list)
    avg_of_list = sum_of_list / len_of_list
    print(avg_of_list)

def load_numbers_from_file(filepath):
    # Loads numbers from a file into a list and returns as a list
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    return numbers

if __name__ == '__main__':
    main()
