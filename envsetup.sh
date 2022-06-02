# !/bin/sh


# get project root dir
# script relative to execute 
mypath=$(dirname $0)
# execute path
current_path=`pwd`
ROOT_PATH=${current_path}/${mypath}


# path of code-format
TOOL_CODE_FORMAT=${ROOT_PATH}"/code-format"


export PATH=${PATH}:${TOOL_CODE_FORMAT}

alias check-format="code-check.py"
