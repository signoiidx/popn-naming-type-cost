"""Import CSV data from a file."""
import csv


def import_csv(file_path):
    """Read a CSV file and return its rows as a list."""
    with open(file_path, 'r', encoding='utf-8') as f:
        rows = csv.reader(f)
        csv_data = list(rows)

    return csv_data
