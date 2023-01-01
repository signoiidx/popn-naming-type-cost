import sys

from import_csv import import_csv
from parse_name import parse_name
# from export_result import export_result


def main(argv):
    csv_data = import_csv('data/popn_name_arcade.csv')
    result_data = parse_name(csv_data)
#     export_result(result_data)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
