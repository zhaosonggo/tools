#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Copyright by zhaosonggo in 2023, All Rights Reserved.


import argparse


def buildPluginParams(argv, config):
    parser = argparse.ArgumentParser(argv, config['name'])
    config_helps = config['helps']
    for key in config_helps.keys():
        params = '-{0}'.format(key)
        shorthand = '-{0}'.format(config_helps[key]['shorthand'])
        help = config_helps[key]['description']
        default = config_helps[key]['values'][config_helps[key]['default']]['value']
        required = config_helps[key]['required']
        parser.add_argument(params, shorthand, help=help, default=default, required=required)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    buildPluginParams(argv="", config="")

