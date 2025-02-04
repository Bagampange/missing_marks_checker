import csv
import os
import sys
from tabulate import tabulate


def main():
    # Validate usage
    usage_validation()

    # Store input CSV if usage validation is successful
    input_csv = sys.argv[1]

    # Validate input CSV file
    fieldnames, students_data = file_validation(input_csv)

    # Check for students with missing marks
    students_with_missing_marks = check_missing(students_data)

    # Store students with missing marks in CSV
    output_csv = generate_csv(students_with_missing_marks, fieldnames)

    # Generate display table in the terminal
    generate_table(output_csv)


def usage_validation():
    # Exit if few command-line arguments: Missing CSV file source
    if len(sys.argv) < 2:
        sys.exit("Missing CSV file")

    # Exit if too many command-line arguments
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Else validate the CSV file
    else:
        input_ext = os.path.splitext(sys.argv[1])[1].lower()
        if input_ext != ".csv":
            sys.exit("Invalid or Missing CSV file")


def file_validation(file_path):
    # Return valid dict for valid CSV file
    try:
        with open(file_path) as file:
            reader = csv.DictReader(file)
            fieldnames = list(reader.fieldnames) if reader.fieldnames else []
            students_data = list(reader)
            return fieldnames, students_data
    except FileNotFoundError:
        sys.exit("CSV file does not exist!")


def check_missing(students_data):
    # Use filter() with a lambda function to select students with missing marks
    students_with_missing_marks = list(
        filter(lambda student: "" in student.values(), students_data)
    )
    return students_with_missing_marks


def generate_csv(dict_array, fieldnames):
    try:
        # Check if file exists and try to remove it before writing
        if os.path.exists("missing_marks.csv"):
            os.remove("missing_marks.csv")

        with open("missing_marks.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dict_array)
            return "missing_marks.csv"

    except PermissionError:
        sys.exit("Permission denied! Close the file and try again.")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")


def generate_table(file_path):
    try:
        with open(file_path, "r", newline="") as file:
            reader = list(csv.reader(file))

            if not reader:
                print("No students with missing marks!")
                return

            print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("CSV file does not exist!")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
