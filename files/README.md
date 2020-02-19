Switch Project
===
Bash or zsh function that finds a single code project in ~/code and ~/go/src directories. It will then change directory to that directory.

Use cases
---
Find project in ```$HOME/code``` and ```$HOME/go/src```:
 1. Find project by name ```field-guide-git```.
 1. Find project by acronym with dashes ```fgg```.
 1. Find project by acronym without dashes ```tb``` for ```toolbelt```.
 1. If multiple projects match, prompt for selection. Sorts project names alphabetically.
 
Once the project is found ```cd``` into that project in the current terminal.

Quickstart
---
```$bash
source switch_project_function.sh
switch_project_function <project>
```
OR
```
sp <project>
```

Testing
---
1. Install pipenv
1. Run pytest
    ```
    pipenv shell
    pytest
    ```

Where did test project names come from?
---
By using the docker name generator: https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go

