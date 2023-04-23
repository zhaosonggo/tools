#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright by OSCode in 2021, All Rights Reserved.

import os
import sys
import argparse
import config


CHECK_MODE = '0 [default]: Check all files \
              1 :Check new commit change files'
PATH_HELP = 'The path where the formatted code file is located. \n\t The default path is the current one'
VERBOSE_HELP = 'Whether to visualize the inspection process,on or off[default]'
FILE_TYPE_HELP = "file Type\
            all[default]\
            c[c language and cpp]\
            j[java]\
            o[object c]"


def isIgnored(item, ignored_list):
    for i in ignored_list:
        try:
            if os.path.samefile(item, i):
                return True
        except:
            # if i is not exist, continue
            continue
    return False


def getCommitDiffInfo():
    commit_change_info = os.popen("git diff HEAD^ --name-only").readlines()
    change_file_list = []
    index = len(commit_change_info) - 1
    while index >= 0:
        if commit_change_info[index] == "\n":
            break
        else:
            item = commit_change_info[index].split()[-1]
            change_file_list.append(item)
        index -= 1
    return change_file_list


def runCheck(path, process):
    # 如果路径指向一个文件，直接进行操作
    if os.path.isfile(path):
        process(path)
    # 如果指向一个路径
    if os.path.isdir(path):
        # 获取路径下所有的子节点名称
        file_list = os.listdir(path)
        # 需要检查的文件列表，默认为所有都需要检查
        check_file_list = file_list[:]
        # 如果当前目录下具有文件.checkignore
        # 就需要进行check_file_list的文件筛选
        if ".checkignore" in file_list:
            ignored_file = []
            ignore_file_path = os.path.join(path, ".checkignore")
            fd = open(ignore_file_path)
            # 生成被忽略的文件列表
            for ignore_item in fd.readlines():
                ignored_file.append(os.path.join(path, ignore_item).rstrip())
            # .checkignore 本身应该被忽略
            ignored_file.append(ignore_file_path)
            # 过滤check_file
            check_file_list = [item for item in file_list if not isIgnored(os.path.join(path, item), ignored_file)]
        for file in check_file_list:
            file_name = os.path.join(path, file)
            # 递归
            runCheck(file_name, process)


def check_file(file, file_type_list, show_process_info, mode):
    def format_check(file_):
        if file_.split('.')[-1] in file_type_list:
            if show_process_info == 'on':
                print("\033[32mFormating:[\033[0m " + file_ + " \033[32m]\033[0m")
            os.system("clang-format -style=google -i " + file_)
    if mode == "0":
        runCheck(file, format_check)
        return
    if mode == "1":
        file_list = getCommitDiffInfo()
        for item in file_list:
            runCheck(item, format_check)
        return


def main(argv):
    parser = argparse.ArgumentParser(argv, "code style check")
    parser.add_argument('-mode', '-m', help=CHECK_MODE, default='0', required=False)
    parser.add_argument('-path', '-p', help=PATH_HELP, default='.', required=False)
    parser.add_argument('-verbose', '-v',help=VERBOSE_HELP, default='off', required=False)
    parser.add_argument('-language', '-l', help=FILE_TYPE_HELP, default='all', required=False)   
    args = parser.parse_args()
    file_type_list = config.checkFile(args.language).getFileType()
    file_path = args.path
    show_process_info = args.verbose
    mode = args.mode
    check_file(file_path, file_type_list, show_process_info, mode)


if __name__ == "__main__":
    main(sys.argv)














