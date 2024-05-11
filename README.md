# Grade The Exams

## Description
This project automates the grading process for multiple-choice exams. It reads exam answer sheets provided in text files, compares the answers to an answer key, calculates grades, and generates a report for each class. The project supports multiple classes, identifying valid and invalid submissions based on specific criteria.

## Installation
No installation is required beyond having Python and Pandas library installed on your system. Ensure you have Python 3.x installed along with Pandas, which can be installed using pip if not already available:

```bash
pip install pandas
```

## Usage
To use this script, run `anh_vutuan_grade_the_exams.py` from your terminal or command prompt. When prompted, enter the name of the class file you wish to grade (e.g., `class1` for `class1.txt`). The script will process the file, grade each valid submission, and output the results to a new file named `<class_name>_grades.txt` (e.g., `class1_grades.txt`).

Example command:
```bash
python anh_vutuan_grade_the_exams.py
```

## Features
- Validates each line of the input file to ensure it meets the expected format.
- Grades each valid submission based on the provided answer key.
- Calculates statistical information such as mean, median, highest score, lowest score, and range of scores.
- Generates a report file for each class with the grades of all students.
- Identifies and reports any invalid submissions.

## Contributing
Contributions to this project are welcome. Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push your branch and submit a pull request.

## Credits
This project was developed by Anh Vu Tuan. Special thanks to everyone who has contributed to improving this grading system.

## License
This project is released under the MIT License. See the LICENSE file for more details.
