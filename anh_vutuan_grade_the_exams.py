import pandas as pd
import numpy as np
filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")

# Attempt to open the specified file. If the file is not found, print an error message and exit the program.
try:
    file = open(filename, "r")
    print(f"Successfully opened {filename}")
    lines = file.readlines()

except:
    print("File not found.")
    exit()

def check_valid(line):
    """
    Checks if a given line from the class file is valid based on specific criteria.

    Parameters:
    line (str): A single line from the class file.

    Returns:
    str: 'invalid values' if the line does not contain exactly 26 values,
         'invalid N#' if the first value does not start with 'N' followed by 8 digits,
         True if the line is valid.
    """
    line = line.split(',')
    if len(line) != 26:
        return 'invalid values'
    elif line[0][0] != "N" or len(line[0]) != 9 or not line[0][1:].isdigit():
        return 'invalid N#'
    else:
        return True

def check_answer(lines):
    """
    Grades each valid line from the class file against an answer key and calculates the score.

    Parameters:
    lines (list): A list of lines from the class file.

    Returns:
    list: A list of lists, where each inner list contains a student's ID and their grade.
    """
    grades = []
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key = answer_key.split(',')
    for line in lines:
        if check_valid(line) == True:
            line = line.split(',')

            score = 0
            for i in range(1, len(line)):
                if line[i].rstrip('\n') == answer_key[i - 1]:
                    score += 4
                elif line[i].rstrip('\n') == "":
                    score += 0
                else:
                    score -= 1
            grades.append([line[0], score])
    return grades

grades = check_answer(lines)
df = pd.DataFrame(grades, columns = ['N#', 'Grade'])

# Calculate and print statistical information about the grades.
mean = df['Grade'].mean()
max = df['Grade'].max()
min = df['Grade'].min()
range = max - min
median = df['Grade'].median()
print(f"Mean score: {mean}")
print(f"Highest score: {max}")
print(f"Lowest score: {min}")
print(f"Range of scores: {range}")
print(f"Median score: {int(median)}")

# Split the filename to remove the file extension and use the base name for the output file.
file_name = filename.split('.')[0]
# Save the DataFrame `df` containing grades to a CSV file without the index and header.
# The output file is named after the original file with '_grades.txt' appended.
df.to_csv(f'{file_name}_grades.txt', index=False, header=False)

print('***ANALYZING***')
valid = 0
for line in lines:
    if check_valid(line) == True:
        valid += 1
    elif check_valid(line) == 'invalid values':
        print(f"Invalid line of data: does not contain exactly 26 values: \n{line}")
    elif check_valid(line) == 'invalid N#':
        print(f"Invalid line of data: N# is invalid \n{line}")
if valid == len(lines):
    print("No errors found!")
print('***REPORT***')
print(f"Total valid lines of data: {valid}")
print(f"Total invalid lines of data: {len(lines) - valid}")
print('***REPORT***')
print(f"Total valid lines of data: {valid}")
print(f"Total invalid lines of data: {len(lines) - valid}")