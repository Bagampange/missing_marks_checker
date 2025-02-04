import pytest
import csv
import os
import sys
from project import usage_validation, file_validation, check_missing, generate_csv, generate_table

# Test usage_validation function
def test_usage_validation():
    # Test missing CSV file
    sys.argv = ["main.py"]
    with pytest.raises(SystemExit) as e:
        usage_validation()
    assert str(e.value) == "Missing CSV file"

    # Test too many command-line arguments
    sys.argv = ["main.py", "file1.csv", "file2.csv"]
    with pytest.raises(SystemExit) as e:
        usage_validation()
    assert str(e.value) == "Too many command-line arguments"

    # Test invalid file extension
    sys.argv = ["main.py", "file1.txt"]
    with pytest.raises(SystemExit) as e:
        usage_validation()
    assert str(e.value) == "Invalid or Missing CSV file"

    # Test valid CSV file
    sys.argv = ["main.py", "file1.csv"]
    usage_validation()  # Should not raise any exception

# Test file_validation function
def test_file_validation(tmpdir):
    # Create a temporary CSV file
    file_path = tmpdir.join("test.csv")
    file_path.write("name,mark\nRonald,85\nBaga,\nDaphine,90")

    # Test valid CSV file
    fieldnames, students_data = file_validation(file_path)
    assert fieldnames == ["name", "mark"]
    assert students_data == [
        {"name": "Ronald", "mark": "85"},
        {"name": "Baga", "mark": ""},
        {"name": "Daphine", "mark": "90"}
    ]

    # Test non-existent file
    with pytest.raises(SystemExit) as e:
        file_validation("non_existent.csv")
    assert str(e.value) == "CSV file does not exist!"

# Test check_missing function
def test_check_missing():
    students_data = [
        {"name": "Ronald", "mark": "85"},
        {"name": "Baga", "mark": ""},
        {"name": "Daphine", "mark": "90"}
    ]
    students_with_missing_marks = check_missing(students_data)
    assert students_with_missing_marks == [{"name": "Baga", "mark": ""}]

# Test generate_csv function
def test_generate_csv(tmpdir):
    dict_array = [{"name": "Baga", "mark": ""}]
    fieldnames = ["name", "mark"]

    # Test successful CSV generation
    output_csv = generate_csv(dict_array, fieldnames)
    assert output_csv == "missing_marks.csv"

    # Check if the file was created and contains the correct data
    with open("missing_marks.csv", "r") as file:
        reader = csv.DictReader(file)
        assert list(reader) == dict_array

# Test generate_table function
def test_generate_table(capsys, tmpdir):
    # Create a temporary CSV file
    file_path = tmpdir.join("test_table.csv")
    file_path.write("name,mark\nBaga,")

    # Test table generation
    generate_table(file_path)
    captured = capsys.readouterr()
    assert "Baga" in captured.out
    assert "" in captured.out

    # Test non-existent file
    with pytest.raises(SystemExit) as e:
        generate_table("non_existent.csv")
    assert str(e.value) == "CSV file does not exist!"

    # Test empty CSV file
    empty_file_path = tmpdir.join("empty.csv")
    empty_file_path.write("")
    generate_table(empty_file_path)
    captured = capsys.readouterr()
    assert "No students with missing marks!" in captured.out
