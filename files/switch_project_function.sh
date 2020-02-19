function switch_project_function {
    switch_project.py "$@"

    PROJECT=$(cat "${HOME}/.switch-project")

    if [[ "No project match" == "${PROJECT}" ]]; then
      echo "Error: cannot change directory '${PROJECT}'"
      echo -1
    else
      cd "${PROJECT}" || exit
    fi
}

alias sp='switch_project_function'
alias p='switch_project_function'