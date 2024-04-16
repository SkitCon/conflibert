'''
File: step1_to_step2.py
Author: Amber Converse
Purpose: This script takes the exported anotations from
    step 1 of the annotation process on Label Studio.
    These annotations should only be for broad PLOVER
    categories (VerCoop, MatCoop, VerConf, MatConf).
    These annotations will be filtered and adjusted for
    input into step 2. Annotations where agreement was
    not 100% are excluded. Annotations that were
    skipped with 100% agreement (i.e. irrelevant) are
    also excluded. Annotations that make it past these
    filters are converted into predictions. Exported file
    will be in the same directory with the same name as
    the input file with the prefix "step2_". One argument
    is required: the name of the input file.
'''

import sys
import json
from pathlib import Path

def convert_annotation(annotation):
    '''
    This function takes in an annotation and ensures it
    meets the criteria for step 2, then converts it to
    a prediction.

    :param:annotation(dict): A json-style dictionary
        defining an annotation
    :return: The converted annotation object or None if
        the annotation does not meet the criteria for
        step 2
    '''
    if len(annotation["annotations"]) == 0:
        return None
    gold_label = None
    for result in annotation["annotations"]:
        if not result["result"]:
            return None
        if not gold_label:
            gold_label = result["result"]
        else:
            if gold_label[0]["value"] != result["result"][0]["value"]:
                return None
    assert annotation["agreement"] == 100
    annotation["annotations"] = []
    annotation["total_annotations"] = 0
    annotation["total_predictions"] = 1
    annotation["predictions"] = [{"result":gold_label}]
    return annotation

def main():
    annotations = json.load(open(sys.argv[1],'r'))
    converted_annotations = []
    for annotation in annotations:
        converted_annotation = convert_annotation(annotation)
        if converted_annotation:
            converted_annotations.append(converted_annotation)
    print(f"Outputting {len(converted_annotations)} annotations...")
    output_file = Path(sys.argv[1])
    output_file = Path(f"{output_file.parent}/step2_{output_file.name}")
    json.dump(converted_annotations, open(output_file,'w'))
    
if __name__ == "__main__":
    main()
