import csv

def import_csv(file_path):

    with open(file_path, 'r', encoding='utf-8') as f:
        rows = csv.reader(f)
        csv_data = [ i for i in rows ]

    f.close()
    return csv_data
