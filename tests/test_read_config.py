import json
import os

import pytest
from config_parser_package.read_config import YamlFile, ConfFile


@pytest.mark.parametrize("conf_parser", [ConfFile()], indirect=True)
def test_success_conf_file_reader(conf_parser):
    """
    success test case for cfg file
    """
    with open('example.cfg', 'w') as file:
        result = conf_parser.get_config('example.cfg')
        assert result == {}
        file.write("[section]\ntest=123")
    result = conf_parser.get_config('example.cfg')
    assert type(result) == dict
    os.remove('example.cfg')

@pytest.mark.parametrize("conf_parser", [ConfFile()], indirect=True)
def _exception_conf_file_reader(conf_parser):
    """
    exception test case for cfg file (data in file is not as per expected format)
    """
    with open('example.cfg', 'w') as file:
        file.write("test=123")
    with pytest.raises(RuntimeError):
        conf_parser.get_config('example.cfg')
    os.remove('example.cfg')


@pytest.mark.parametrize("conf_parser", [YamlFile()], indirect=True)
def test_success_yaml_file_reader(conf_parser):
    """
    success test case for yaml file
    """
    with open('example.yaml', 'w') as file:
        file.write(json.dumps({'test_write_key': {'key': 'value'}}))

    result = conf_parser.get_config('example.yaml')
    os.remove('example.yaml')
    assert type(result) == dict


@pytest.mark.parametrize("conf_parser", [YamlFile()], indirect=True)
def test_exception_yaml_file_not_found(conf_parser):
    """
    exception test case for yaml file
    """
    with pytest.raises(RuntimeError):
        conf_parser.get_config('xyz.yaml')


@pytest.mark.parametrize("conf_parser", [ConfFile()], indirect=True)
def test_conf_file_not_found(conf_parser):
    """
    file is not available case in configparser
    """
    with pytest.raises(RuntimeError):
        conf_parser.get_config('xyz.cfg')









