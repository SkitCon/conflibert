'''
File: split_json_label_studio.py
Author: Amber Converse
Purpose: Takes a CSV task file formatted for use on Label Studio
    containing sentences in English, Spanish, and Arabic and splits
    it into two files, one containing sentences in English and Spanish,
    one containing English and Arabic. Takes the name of JSON task file
    as an argument.
'''

import sys
import csv

def main():
    if len(sys.argv) < 2:
        print("Error in argument format. Please use the name of the input file as the first argument.")
        exit(0)
    
    with open(sys.argv[1], 'r', newline='') as input_f:
        input_reader = csv.reader(input_f)
        with open(f"en_ar_{sys.argv[1]}", 'w', newline='') as output_ar:
            with open(f"en_es_{sys.argv[1]}", 'w', newline='') as output_es:
                ar_writer = csv.writer(output_ar)
                es_writer = csv.writer(output_es)
                for line in input_reader:
                    ar_line = line[:3] + line[4:]
                    es_line = line[:1] + line[2:]
                    ar_writer.writerow(ar_line)
                    es_writer.writerow(es_line)
        
if __name__ == "__main__":
    main()
