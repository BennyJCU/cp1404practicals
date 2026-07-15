import csv
from guitar import Guitar


def main():
    guitars = []

    get_csv(guitars)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_csv(guitars):
    """guitar file reader version using the csv module."""
    # First, open the file for reading - note: specify newline
    # to avoid quoted \n in strings being considered a new record
    in_file = open('guitars.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)  # use default dialect, Excel
    for row in reader:
        guitar = Guitar(row[0],row[1],row[2])
        guitars.append(guitar)

    in_file.close()


main()

