# !/bin/sh


# get project root dir
# script relative to execute 
mypath=$(dirname $0)
# execute path
current_path=`pwd`
ROOT_PATH=${current_path}/${mypath}

export PYTHONPATH=${ROOT_PATH}:$PYTHONPATH

# path of code-format
PATH_CODE_CHECK=${ROOT_PATH}"/code-format"
export PATH=${PATH}:${PATH_CODE_CHECK}
# path of create-uml
PATH_CREATE_UML=${ROOT_PATH}"/create-uml"
export PATH=${PATH}:${PATH_CREATE_UML}


alias code-check="code-check.py"
alias create-uml="create-uml.py"
