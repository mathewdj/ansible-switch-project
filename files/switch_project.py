#!/usr/bin/env python3
import re
import sys
from enum import Enum
from os import listdir, environ
from os.path import join
from typing import List, NamedTuple


class ProjectMatch(Enum):
    NO_MATCHING_PROJECTS = 0
    SINGLE_MATCHING_PROJECT = 1
    MULTIPLE_MATCHING_PROJECTS = 2


def find_project(working_dirs: List[str], search_term: str) -> List[str]:
    possible_projects = []
    for working_dir in working_dirs:
        acronym_list = list(search_term)
        projects = [join(working_dir, d) for d in listdir(working_dir)
                    if d == search_term
                    or matches_acronym_with_dashes(d, acronym_list)
                    or matches_acronym_without_dashes(d, acronym_list)]

        for project in projects:
            possible_projects.append(project)

    return sorted(possible_projects)


def matches_acronym_with_dashes(directory_name: str, acronym: List[str]) -> bool:
    acronym_patterns = [f"{letter}[a-z0-9]+" for letter in acronym]

    # eg acronym 'gw' would produce 'g[a-z]+-w[a-z]+'
    pattern = re.compile("-".join(acronym_patterns))

    match = pattern.match(directory_name)
    if match:
        return True
    return False


def matches_acronym_without_dashes(directory_name: str, acronym: List[str]) -> bool:
    acronym_patterns = [f"{letter}[a-z]+" for letter in acronym]
    pattern = re.compile("".join(acronym_patterns))
    match = pattern.match(directory_name)

    if match:
        return True
    return False


def identify_project(working_dirs: List[str], search_term: str) -> (ProjectMatch, List[str]):
    projects = find_project(working_dirs, search_term)

    if len(projects) == 1:
        return ProjectMatch.SINGLE_MATCHING_PROJECT, projects
    elif len(projects) > 0:
        return ProjectMatch.MULTIPLE_MATCHING_PROJECTS, projects

    return ProjectMatch.NO_MATCHING_PROJECTS, list()


class Cli(NamedTuple):
    state_dir: str
    working_dirs: List[str]
    search_term: str

    def select_a_project(self):
        project_match, projects = identify_project(self.working_dirs, self.search_term)

        project = None
        if project_match == ProjectMatch.SINGLE_MATCHING_PROJECT:
            project = projects[0]
        elif project_match == ProjectMatch.MULTIPLE_MATCHING_PROJECTS:
            project = self.multi_project_selection(projects)

        with open(join(f"{self.state_dir}/.switch-project"), "w") as f:
            if project is not None:
                f.write(project)
            else:
                f.write("No project match")

    @staticmethod
    def multi_project_selection(multi_projects: List[str]) -> str:
        indexed_project = [f"{i + 1}) {prj}" for i, prj in enumerate(multi_projects)]
        print("\n".join(indexed_project))
        # Index starts at 1 not 0
        selection = int(input("\n Selection: ")) - 1

        return multi_projects[selection]


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} <search term>")
        sys.exit(0)

    search_terms = sys.argv[1]
    working_directories = [join(environ['HOME'], 'code'),
                           join(environ['HOME'], 'go', 'src'),
                           join(environ['HOME'], 'code', 'ansible-toolbelt')]
    state_dir = environ['HOME']

    Cli(state_dir, working_directories, search_terms).select_a_project()
