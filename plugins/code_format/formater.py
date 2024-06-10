#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright by zhaosonggo in 2024, All Rights Reserved.

import subprocess

class Formater:
    def __init__(self, cmd):
        self.cmd = cmd

    def format(self):
        subprocess.check_call(self.cmd, shell=True)


class CFormater(Formater):
    def __init__(self, file):
        super().__init__(f'clang-format -style=google -i {file}')


class GnFormater(Formater):
    def __init__(self, file):
        super().__init__(f'gn format {file}')


def FormaterFactory(file:str):
    if file.endswith('.c') or file.endswith('.cc') or file.endswith('.cpp') or file.endswith('.h'):
        return CFormater(file)
    elif file.endswith('.gn'):
        return GnFormater(file)
    else:
        return None




