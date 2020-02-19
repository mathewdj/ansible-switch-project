import os
import random
import string
from os.path import join
from typing import List

from files.switch_project import find_project, identify_project, ProjectMatch


class TestSwitchProject:
    def test_find_a_project_by_name(self):
        working_dir = join(f"/tmp/project{random_string()}")

        project = 'red-amber'
        create_temp_projects(working_dir, [project])

        assert find_project([working_dir], "red-amber") == [join(working_dir, project)]

    def test_find_a_project_by_name_with_numbers(self):
        working_dir = join(f"/tmp/project{random_string()}")

        project = 'red-amber9'
        create_temp_projects(working_dir, [project])

        assert find_project([working_dir], "red-amber9") == [join(working_dir, project)]

    def test_find_a_project_via_acronym_for_projects_with_dashes(self):
        working_dir = join(f"/tmp/project{random_string()}")

        project = 'green-web'
        create_temp_projects(working_dir, [project])

        assert find_project([working_dir], "gw") == [join(working_dir, project)]

    def test_find_a_project_via_acronym_for_projects_with_dashes_and_numbers(self):
        working_dir = join(f"/tmp/project{random_string()}")

        project = 'green2-web3'
        create_temp_projects(working_dir, [project])

        assert find_project([working_dir], "gw") == [join(working_dir, project)]

    def test_find_a_project_via_acronym_for_projects_without_dashes(self):
        working_dir = join(f"/tmp/project{random_string()}")

        project = 'toolbelt'
        create_temp_projects(working_dir, [project])

        assert find_project([working_dir], "tb") == [join(working_dir, project)]

    def test_find_many_projects_matching_acronym_sorting_alphabetically(self):
        working_dir = join(f"/tmp/project{random_string()}")

        project1 = 'exciting-ramanujan'
        project2 = 'epic-ramanujan'
        project3 = 'epic-raman'
        create_temp_projects(working_dir, [project1, project2, project3])

        assert find_project([working_dir], "er") == [join(working_dir, project) for project in
                                                     sorted([project3, project2, project1])]


class TestIdentifyProjects:
    def test_select_single_project_match(self):
        working_dir = join(f"/tmp/project{random_string()}")

        project1 = 'exciting-ramanujan'
        create_temp_projects(working_dir, [project1])

        assert identify_project([working_dir], project1) == (
            ProjectMatch.SINGLE_MATCHING_PROJECT, [join(working_dir, project1)])

    def test_select_no_matching_projects(self):
        working_dir = join(f"/tmp/project{random_string()}")

        project1 = 'eager-benz'
        create_temp_projects(working_dir, [project1])

        assert identify_project([working_dir], "zz") == (ProjectMatch.NO_MATCHING_PROJECTS, [])

    def test_select_multiple_project_match(self):
        working_dir = join(f"/tmp/project{random_string()}")

        project1 = 'eager-benz'
        project2 = 'elastic-bohr'
        create_temp_projects(working_dir, [project1, project2])

        assert identify_project([working_dir], "eb") == (
            ProjectMatch.MULTIPLE_MATCHING_PROJECTS, [join(working_dir, project1), join(working_dir, project2)])


def create_temp_projects(working_dir: str, projects: List[str]):
    if not os.path.exists(working_dir):
        os.mkdir(working_dir)

    for p in projects:
        os.mkdir(join(working_dir, p))
        with open(join(working_dir, p, "README.md"), "w") as f:
            f.write("Status: 2019 keep")


def random_string(string_length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))
