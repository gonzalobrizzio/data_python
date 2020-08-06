#!/usr/bin/python2.7
from io import open
import csv


def count_columns(file):
    reader = csv.reader(file, delimiter="\t")
    count_total_columns = len(next(reader)) - 1

    return count_total_columns


def transform_file(old_file, new_file, separator, old_enconding, new_enconding):
    tsv_utf16 = open(old_file, 'r', encoding=old_enconding)
    csv_utf8 = open(new_file, 'w+', encoding=new_enconding)

    file_line_aux = ''

    fields = count_columns(tsv_utf16)

    tsv_utf16.seek(0)

    for file_lines in tsv_utf16.readlines():
        file_content = file_lines.replace("\t", separator)

        if file_content.count(separator) == fields:
            csv_utf8.write(file_content)
        else:
            file_line_aux += file_content
            file_line_aux = file_line_aux.replace("\n", " ")

            if file_line_aux.count(separator) == fields:
                file_line_aux += "\n"
                csv_utf8.write(file_line_aux)
                file_line_aux = ''

    csv_utf8.close()
    tsv_utf16.close()


if __name__ == "__main__":
    transform_file("C:\Users\gonza\OneDrive\Escritorio\datos_data_engineer.tsv", "datos_data_engineer.csv", "|", "utf-16-le", "utf-8")