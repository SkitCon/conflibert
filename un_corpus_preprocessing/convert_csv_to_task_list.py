'''
File: convert_csv_to_task_list.py
Author: Amber Converse
Purpose: This scripts converts a parallel corpus CSV file
    with the schema id,ar,en,es to a JSON task list fit to
    be imported into Label Studio. Argument is a file path.
'''

import sys
import csv
import json
from pathlib import Path

def main():
    if len(sys.argv) == 1:
        print("Please include file path as an argument.")
        exit(0)
    
    json_list = []
    with open(sys.argv[1],'r',newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if i > 0:
                json_list.append({"id":row[0],
                                  "data":
                                    {"text_ar":row[1],
                                     "text_en":row[2],
                                     "text_es":row[3]}})
    with open(Path(sys.argv[1]).with_suffix(".json"),'w') as json_file:
        json.dump(json_list, json_file)   

if __name__ == "__main__":
    main()
