Role Name
=========
Puts ``switch_project.py`` and ``switch_project_function.sh`` in the bash functions directory. So that it can be automatically 
found by bash or zsh.

Requirements
------------
1. python 3.7
1. git
1. For bash only (~/.zshrc is part of playbook):
    1. bash profile sourcing bash_functions directory. For example 
        1. ```~/.bash_profile```: 
            ```
            for bash_function in ~/bash_functions/*.sh; do source $bash_function; echo $bash_function; done
            ```
       1. Add ``` ~/bash_functions/``` to PATH environment variable, so that python script can be executed.
          ```
          export PATH=PATH:${HOME}/bash_functions/
          ```

Example Playbook
----------------
Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      connection: local
      roles:
         - ansible-switch-role
         
Running locally
---
To test playbook locally:
```
ansible-playbook test-role.yml
```

License
-------
[GPLv3](LICENSE)
