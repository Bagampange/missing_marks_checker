# MISSING MARKS CHECKER

#### Video Demo: [https://youtu.be/eC2s8JfAtHM](https://youtu.be/eC2s8JfAtHM)

#### Description:

This Python script is designed to process a CSV file containing student data and identify students with missing marks. It generates a new CSV file (`missing_marks.csv`) containing only the students with missing marks and displays the results in a formatted table in the terminal. The script is a simple yet effective tool for educators or administrators to quickly identify incomplete student records.

## **Introduction**

The **Missing Marks Checker** is a command-line tool that automates the process of identifying students with missing marks in a CSV file. It is particularly useful for educators who need to quickly identify incomplete records and take appropriate action. The script is written in Python and leverages the `csv` module for file handling and the `tabulate` library for displaying the results in a readable table format.

## **Features**

- **CSV File Validation**: Ensures the input file is a valid CSV file.
- **Missing Marks Detection**: Identifies students with missing marks (empty fields) in the CSV file.
- **Output CSV Generation**: Creates a new CSV file (`missing_marks.csv`) containing only the students with missing marks.
- **Terminal Display**: Displays the results in a formatted table using the `tabulate` library.

## **Installation Instructions**

To use the Missing Marks Checker, follow these steps:

1. **Install Python**: Ensure Python 3.x is installed on your system.
2. **Clone the Repository**: Use `git clone https://github.com/Bagampange/missing_marks_checker.git` to clone the project.
3. **Install Dependencies**: Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should contain:

   ```plaintext
   tabulate==0.9.0
   ```

## **Usage Instructions**

1. **Prepare Your CSV File**: Ensure your CSV file has a header row and contains student data. For example:

   ```csv
   name,mark
   Ronald,85
   Baga,
   Daphine,90
   ```

2. **Run the Script**: Execute the script from the command line, passing the CSV file as an argument:

   ```bash
   python main.py input.csv
   ```

3. **View Results**:
   - The script will generate a `missing_marks.csv` file containing students with missing marks.
   - The results will also be displayed in a formatted table in the terminal.

## **Example**

Given the following CSV file (`input.csv`):

```csv
name,mark
Ronald,85
Baga,
Daphine,90
```

Running the script:

```bash
python main.py input.csv
```

Output in the terminal:

```
+--------+-------+
| name   | mark  |
+--------+-------+
| Baga   |       |
+--------+-------+
```

A `missing_marks.csv` file will also be created with the following content:

```csv
name,mark
Baga,
```

## **Future Improvements**

- **Support for Multiple Missing Fields**: Extend the script to handle multiple missing fields and provide more detailed output.
- **Interactive Mode**: Add an interactive mode for users to specify which fields to check for missing values.
- **Integration with APIs**: Allow the script to fetch CSV files from cloud storage or APIs.
- **Error Handling**: Improve error handling for edge cases, such as malformed CSV files or unsupported formats.

## **Contributing**

Contributions to the Missing Marks Checker are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## **Contact Information**

For support or inquiries, please reach out to:

- **Author**: Ronald Bagampange
- **Email**: bagampangeronald@gmail.com

## **Dependencies**

- **Python Standard Libraries**:
  - `csv`
  - `os`
  - `sys`
- **External Libraries**:
  - `tabulate` (for table formatting)

## **Files**

- **main.py**: The main script that processes the CSV file and identifies missing marks.
- **requirements.txt**: Lists the external dependencies required to run the script.

## **Acknowledgements**

- **CS50**: For inspiring the problem-solving approach used in this project.
- **Python Community**: For providing excellent documentation and resources.
