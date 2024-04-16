'''
File: compile_es_un_corpus.py
Author: Amber Converse
Purpose: This script reads all of the files in UN TEI corpus
    in Spanish and compiles them into csv files for each year
    including the columns: id, news_outlet, title, date, and
    text.

    Spanish corpus must be in the directory:
    UNv1.0-TEI/es
'''

import os
from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd

def main(): 
    path = Path("UNv1.0-TEI/es")
    years = [item for item in path.iterdir() if item.is_dir()]
    for year in years:
        df_inst = False
        for file in year.rglob("*.xml"):
            try:
                doc_tree = ET.parse(file).getroot()
            except Exception as e:
                print(f"Could not parse {file}: {e}")
                continue
            df_dict = dict()
            id = doc_tree.find(".//idno[@type='symbol']").text.strip()
            df_dict["id"] = f"{year.stem}/{id}"
            df_dict["news_outlet"] = "United Nations"
            df_dict["title"] = doc_tree.find(".//title").text.strip()
            date = doc_tree.find(".//date").text.strip()
            df_dict["date"] = f"{date[:4]}/{date[4:6]}/{date[6:]}"
            ps = []
            for p in doc_tree.find(".//text").findall(".//p"):
                ps.append(" ".join([s.text.strip() for s in p.findall(".//s") if s.text]))
            df_dict["text"] = "\n".join(ps)
            
            sub_df = pd.DataFrame(df_dict,index=[0])
            if df_inst:
                df = pd.concat([df,sub_df], ignore_index=True)
            else:
                df = sub_df
                df_inst = True
        if not os.path.exists("compiled_es_un_corpus"):
            os.mkdir("compiled_es_un_corpus") 
        df.to_csv(f"compiled_es_un_corpus/International_UN_{year.stem}.csv",encoding="utf-8-sig")

if __name__ == "__main__":
    main()
