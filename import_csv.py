import csv

def import_csv(file):

    f = open(file, 'r')
    rows = csv.reader(f)
    csv_data = [ i for i in rows ]

    f.close()
    return csv_data
