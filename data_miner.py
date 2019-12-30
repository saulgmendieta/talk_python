import csv
import os
import statistics

from data_types import Purchase


def print_header():
    print('----------------------------------')
    print('   REAL ESTATE DATA MINING APP')
    print('----------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'database_example.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        # for row in reader:
        #     print(row)

        return purchases


# def load_file_basic(dir):
#     with open(dir, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('Found header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             lines.append(line_data)
#
#         print(lines[:5])
#     return []

# def get_flow(p):
#    return p.var2


def query_data(data):

    # data.sort(key=get_flow)
    data.sort(key=lambda p: p.var2)
    high_flow = data[-1]
    print('The highest flow was {:,} at {} for device {}'.format(
        high_flow.var2, high_flow.fecha, high_flow.iddispositivo))

    low_flow = data[0]
    print('The lowest flow was {:,} at {} for device {}'.format(
        low_flow.var2, low_flow.fecha, low_flow.iddispositivo))

    # flows = [
    #     p.var2
    #     for p in data
    # ]

    # ave_flow = statistics.mean(flows)
    ave_flow = statistics.mean(p.var2 for p in data)
    print('The average flow is {:,}'.format(ave_flow))

    # flows = []
    # for pur in data:
    #     flows.append(pur.var2)
    # ave_flow = statistics.mean(flows)
    # print('The average flow is {:,}'.format(ave_flow))


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


if __name__ == "__main__":
    main()
