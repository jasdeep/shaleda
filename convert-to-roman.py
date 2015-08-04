# -*- coding: utf-8 -*-
import codecs
from unidecode import unidecode
from sys import argv
import os


def read_and_convert(filename):
    file_stream = read_file(filename)
    converted_text = ''
    for line in file_stream:
        converted_text = converted_text + convert_to_roman(line)
    return converted_text


def read_file(filename):
    return codecs.open(filename, "r", "utf-8")


def convert_to_roman(text):
    return unidecode(text)


def write_file(filename, text):
    only_filename, file_extension = os.path.splitext(filename)
    file_output = codecs.open(only_filename + "_roman" + file_extension, 'w', 'utf-8')
    file_output.write(text)
    file_output.close()


if __name__ == '__main__':
    script, filename = argv
    text = read_and_convert(filename)
    write_file(filename, text)
