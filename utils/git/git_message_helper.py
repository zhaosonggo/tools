#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Copyright by zhaosonggo in 2023, All Rights Reserved.

import os


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


def getCommitDiffWithSuffix(suffix):
    file_list = getCommitDiffInfo()
    return [item for item in file_list if item.endswith(suffix)]