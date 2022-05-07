# !/bin/sh


# get project root dir
# script relative to root
relative_for_root=".."
# script relative to execute
mypath=$(dirname $0)
# executr path
current_path=`pwd`
ROOT_PATH=${current_path}/${mypath}/${relative_for_root}


# path of code-format
TOOL_CODE_FORMAT=${ROOT_PATH}"/tools/code-format"


export PATH=${PATH}:${TOOL_CODE_FORMAT}

alias check-format="code-check.py all"
