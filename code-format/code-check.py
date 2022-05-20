#!/usr/bin/env python
# Copyright by OSCode in 2021, All Rights Reserved.

import os
import sys
import argparse
import config

PATH_HELP = 'The path where the formatted code file is located. \n\t The default path is the current one'
VERBOSE_HELP = 'Whether to visualize the inspection process,on or off[default]'
FILE_TYPE_HELP = "file Type\
            all[default]\
            c[c language and cpp]\
            j[java]\
            o[object c]"


def check_file(file_path, file_type_list, show_process_info):
    files_map = {}
    for root, _, files in os.walk(file_path):
        files_map[root] = files
    for key in files_map.keys():
        files = files_map[key]
        for file in files:
            if file.split('.')[-1] in file_type_list:
                if show_process_info == 'on':
                    print("Formating: [ " + key + "/" + file + " ]")
                os.system("clang-format -style=google -i " + key + "/" + file)


def main(argv):
    parser = argparse.ArgumentParser(argv, "code style check")
    parser.add_argument('-path', '-p', help=PATH_HELP, default='.', required=False)
    parser.add_argument('-verbose', '-v',help=VERBOSE_HELP, default='off', required=False)
    parser.add_argument('-language', '-l', help=FILE_TYPE_HELP, default='all', required=False)   
    args = parser.parse_args()
    file_type_list = config.checkFile(args.language).getFileType()
    file_path = args.path
    show_process_info = args.verbose
    check_file(file_path, file_type_list, show_process_info)


if __name__ == "__main__":
    main(sys.argv)
            
            













