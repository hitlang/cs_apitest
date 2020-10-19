import json
import os
from typing import Dict, Text, List
import yaml
from apitest.common.exceptions import *
from apitest.common.log import MyLog
from models import TestCase

try:
    # PyYAML version >= 5.1
    yaml.warnings({"YAMLLoadWarning": False})
except AttributeError:
    pass


def _load_yaml_file(yaml_file: Text) -> Dict:
    """ load yaml file and check file content format
    """
    with open(yaml_file, mode="rb") as stream:
        try:
            yaml_content = yaml.load(stream)
        except yaml.YAMLError as ex:
            err_msg = f"YAMLError:\nfile: {yaml_file}\nerror: {ex}"
            # logger.error(err_msg)
            MyLog.get_log().error(err_msg)
            raise FileFormatError

        return yaml_content

#
def _load_json_file(json_file: Text) -> Dict:
    """ load json file and check file content format
    """
    with open(json_file, mode="rb") as data_file:
        try:
            json_content = json.load(data_file)
        except json.JSONDecodeError as ex:
            err_msg = f"JSONDecodeError:\nfile: {json_file}\nerror: {ex}"
            raise FileFormatError(err_msg)

        return json_content
#
#
def load_test_file(test_file: Text) -> Dict:
    """load testcase/testsuite file content"""
    if not os.path.isfile(test_file):
        raise FileNotFound(f"test file not exists: {test_file}")

    file_suffix = os.path.splitext(test_file)[1].lower()
    if file_suffix == ".json":
        test_file_content = _load_json_file(test_file)
    elif file_suffix in [".yaml", ".yml"]:
        test_file_content = _load_yaml_file(test_file)
    else:
        # '' or other suffix
        raise FileFormatError(
            f"testcase/testsuite file should be YAML/JSON format, invalid format file: {test_file}"
        )

    return test_file_content
#
#
def load_testcase(testcase: Dict) -> TestCase:
    try:
        # validate with pydantic TestCase model
        testcase_obj = TestCase.parse_obj(testcase)
    except ValidationFailure as ex:
        err_msg = f"TestCase ValidationError:\nerror: {ex}\ncontent: {testcase}"
        raise TestCaseFormatError(err_msg)

    return testcase_obj
#
#
def load_testcase_file(testcase_file: Text) -> TestCase:
    """load testcase file and validate with pydantic model"""
    testcase_content = load_test_file(testcase_file)
    testcase_obj = load_testcase(testcase_content)
    testcase_obj.config.path = testcase_file
    return testcase_obj


def load_folder_files(folder_path: Text, recursive: bool = True) -> List:
    """ load folder path, return all files endswith .yml/.yaml/.json/_test.py in list.

    Args:
        folder_path (str): specified folder path to load
        recursive (bool): load files recursively if True

    Returns:
        list: files endswith yml/yaml/json
    """
    if isinstance(folder_path, (list, set)):
        files = []
        for path in set(folder_path):
            files.extend(load_folder_files(path, recursive))

        return files

    if not os.path.exists(folder_path):
        return []

    file_list = []

    for dirpath, dirnames, filenames in os.walk(folder_path):
        filenames_list = []

        for filename in filenames:
            if not filename.lower().endswith((".yml", ".yaml", ".json", "_test.py")):
                continue

            filenames_list.append(filename)

        for filename in filenames_list:
            file_path = os.path.join(dirpath, filename)
            file_list.append(file_path)

        if not recursive:
            break

    return file_list


#
def locate_file(start_path: Text, file_name: Text) -> Text:
    """ locate filename and return absolute file path.
        searching will be recursive upward until system root dir.

    Args:
        file_name (str): target locate file name
        start_path (str): start locating path, maybe file path or directory path

    Returns:
        str: located file path. None if file not found.

    Raises:
        exceptions.FileNotFound: If failed to locate file.

    """
    if os.path.isfile(start_path):
        start_dir_path = os.path.dirname(start_path)
    elif os.path.isdir(start_path):
        start_dir_path = start_path
    else:
        raise FileNotFound(f"invalid path: {start_path}")

    file_path = os.path.join(start_dir_path, file_name)
    if os.path.isfile(file_path):
        # ensure absolute
        return os.path.abspath(file_path)

    # system root dir
    # Windows, e.g. 'E:\\'
    # Linux/Darwin, '/'
    parent_dir = os.path.dirname(start_dir_path)
    if parent_dir == start_dir_path:
        raise FileNotFound(f"{file_name} not found in {start_path}")

    # locate recursive upward
    return locate_file(parent_dir, file_name)



if __name__ == '__main__':
    r = load_test_file("payment.json")
    # r = load_test_file("template.yml")
    #

    # r = load_testcase_file("payment.json")
    import pprint
    pprint.pprint(r)
    pass


