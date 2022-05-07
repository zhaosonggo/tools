#!/usr/bin/env python
# Copyright by OSCode in 2021, All Rights Reserved.

import os
import sys

ignored_dir = ["./cmake-build-debug"]

def isTargetFile(file_name, path):
    if path is not None:
        for i_path in ignored_dir:
            if i_path in path:
                return False
    if file_name.endswith(".cc") or file_name.endswith(".h") or file_name.endswith(".cpp") or file_name.endswith(".mm") or file_name.endswith(".m") or file_name.endswith(".java"):
        return True
    return False

def file_name_walk(file_dir):
    files_map = {}
    for root, _, files in os.walk(file_dir):
        files_map[root] = files
    for key in files_map.keys():
        files = files_map[key]
        for file in files:
            if isTargetFile(file, key):
                print("Formating: [ " + key + "/" + file + " ]")
                os.system("clang-format -style=google -i " + key + "/" + file)

def check_new_commit():
    gc_1 = "git log -2 --pretty=oneline"
    gc_2 = "git diff {0} {1} --name-only"
    commits = os.popen(gc_1)
    commit_array = []
    for commit in commits:
        commit_array.append(commit.split(" ")[0])
    if len(commit_array) == 1:
        file_name_walk("./")
    else:
        diff_info = os.popen(gc_2.format(commit_array[0], commit_array[1]))
        for line in diff_info:
            if isTargetFile(line.rstrip()):
                os.system("clang-format -style=google -i " + "./" + line)

def check_all_file():
    file_name_walk("./")



if __name__ == "__main__":
    if len(sys.argv) == 1:
        check_new_commit()
    
    else:
        for param in sys.argv[1:]:
            if param == "all":
                check_all_file()
            
            













