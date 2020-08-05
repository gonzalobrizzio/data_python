#!/usr/bin/python2.7
import re
from io import open
import csv

def count_separator(line, separator):
    count_total_separator = 0

    for char in line:
        if char == separator:
            count_total_separator += 1

    return count_total_separator

def count_columns(file):
    reader = csv.reader(file, delimiter="\t")
    count_total_columns = len(next(reader)) - 1

    return count_total_columns

def transform_file(file,new_file, separator):
    tsv_utf16 = open(file, 'r', encoding="utf-16-le")
    csv_utf8 = open(new_file, 'w+', encoding="utf-8")

    file_line_aux = ''

    fields = count_columns(tsv_utf16)

    tsv_utf16.seek(0)

    for file_lines in tsv_utf16.readlines():
        file_content = re.sub("\t", separator, file_lines)

        if count_separator(file_content, separator) == fields:
            csv_utf8.write(file_content)
        else:
            file_line_aux += file_content
            file_line_aux = re.sub("\n", "", file_line_aux)

            if count_separator(file_line_aux, separator) == fields:
                file_line_aux += "\n"
                csv_utf8.write(file_line_aux)
                file_line_aux = ''

    csv_utf8.close()
    tsv_utf16.close()

if __name__ == "__main__":
    transform_file(r'C:\Users\gonza\OneDrive\Escritorio\datos_data_engineer.tsv', 'datos_data_engineer.csv', "|")