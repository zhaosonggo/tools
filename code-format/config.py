#!/usr/bin/env python
# Copyright by OSCode in 2021, All Rights Reserved.

import re


support_file_type = {
    'c':['cc', 'c', 'cpp', 'h'],
    'j':['java'],
    'o':['mm', 'm'],
    # 'p':['py']
}


class checkFile:
    key = None
    def __init__(self, key):
        self.key = key

    def getFileType(self):
        if self.key == 'all':
            result = []
            for key in support_file_type.keys():
                result += support_file_type[key]
            return result
        else:
            type_list = list(self.key)
            result = []
            for key in support_file_type.keys():
                if key in type_list:
                    result += support_file_type[key]
            return result
    