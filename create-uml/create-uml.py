#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright by zhaosonggo in 2023, All Rights Reserved.


import os
import sys
import json
from utils.config.build_plugin_params import buildPluginParams
from utils.git.git_message_helper import getCommitDiffWithSuffix
from utils.tools.build_deps import depsBuild
from utils.tools.file_system_control import getFileFromPathWithSuffix

UML_FILE_SUFFIX = ".uml"
JAR_NAME = "plantuml-1.2023.6.jar"
JAR_PATH = os.path.join(sys.path[0], JAR_NAME)


def createUML(files, verbose, out):
    if os.path.isfile(out):
        print("输出目录与现有文件重名")
        return
    
    if not os.path.exists(out):
        os.makedirs(out)
    for file in files:
        if verbose == "on":
            print("正在生成[{0}]".format(file))
        os.system("java -jar {0} {1} -o {2}".format(JAR_PATH, file, out))


def getFiles(path, mode):
    if mode == "1":
        return getCommitDiffWithSuffix(UML_FILE_SUFFIX)
    elif mode == "0":
        return getFileFromPathWithSuffix(path, UML_FILE_SUFFIX)    


def main(argv):
    config_path = os.path.join(sys.path[0], "config.json")
    params_config = json.load(open(config_path, "r+"))
    if len(params_config['deps']) != 0:
        depsBuild(params_config['deps'])
    args = buildPluginParams(argv, params_config)
    file_list = getFiles(args.path, args.mode)
    createUML(file_list, args.verbose, args.out)

if __name__ == "__main__":
    main(sys.argv)

