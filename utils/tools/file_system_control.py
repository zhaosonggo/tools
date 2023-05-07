#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Copyright by zhaosonggo in 2023, All Rights Reserved.


import os
import sys

def getFileFromPath(path):
    if os.path.isfile(path):
        return [path]
    
    if os.path.isdir(path):
        file_list = []
        file_or_path_list = os.listdir(path)
        for file in file_or_path_list:
            file_or_path_name = os.path.join(path, file)
            file_list += getFileFromPath(file_or_path_name)
        return file_list

def getFileFromPathWithSuffix(path, suffix):
    file_list = getFileFromPath(path)
    return [item for item in file_list if item.endswith(suffix)]