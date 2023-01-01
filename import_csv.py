import csv

def import_csv(file):

    with open(file, encoding='utf-8') as f:
        rows = csv.reader(f)
        csv_data = [ i for i in rows ]

    f.close()
    return csv_data
