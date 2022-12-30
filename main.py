import sys

from import_csv import import_csv
from parse_name import parse_name
# import export_result


def main(argv):
    csv_data = import_csv('data/popn_name_arcade.csv')
    
    parse_name(csv_data)
        
#    export_result()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
