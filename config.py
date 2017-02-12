import csv
import os

current_directory_path = os.path.dirname(__file__)
default_items_to_scrape = 240


def write_to_excel(output, fieldnames):
    with open(current_directory_path + '/output/output.csv', "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, restval="", dialect='excel')
        writer.writeheader()
        for result in output:
            writer.writerow(result)


