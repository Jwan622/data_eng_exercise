import glob
import os
import csv

from app.constants import MARKETING_FILE_PREFIX, USER_RECORDS_KEY, AD_RECORDS_KEY


def import_records(path = "dataset/*.csv"):
    final_records = {
        USER_RECORDS_KEY: [],
        AD_RECORDS_KEY: []
    }
    for file_path in glob.glob(path):
        with open(file_path, 'r') as file:
            print(f"Processing {file_path}")
            csv_reader = clean_records(file)
            key = AD_RECORDS_KEY if os.path.basename(file_path).startswith(MARKETING_FILE_PREFIX) else USER_RECORDS_KEY
            next(csv_reader)
            for row in csv_reader:
                final_records[key].append(tuple(row))

    print(f"User records processed: {len(final_records[USER_RECORDS_KEY])}")
    print(f"Ad records processed: {len(final_records[AD_RECORDS_KEY])}")
    return final_records


def clean_records(file):
    return csv.reader((line.replace('\0', '') for line in file))
