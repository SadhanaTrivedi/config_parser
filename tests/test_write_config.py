import os

import pytest
from config_parser_package.write_config import WriteJsonFile, WriteEnvFile,\
    WriteOsVariables


@pytest.mark.parametrize("write_config", [WriteOsVariables()], indirect=True)
def test_success_os_variable_set(write_config):
    """
    success test case for writing os variable
    """
    result = write_config.set_config({"test_env": "test_value"})
    assert result == True


@pytest.mark.parametrize("write_config", [WriteOsVariables()], indirect=True)
def test_wrong_config_os_variable(write_config):
    """
    error test case for setting os variable
    """
    result = write_config.set_config("wrong conf")
    assert result == False


@pytest.mark.parametrize("write_config", [WriteJsonFile()], indirect=True)
def test_success_write_json_file(write_config):
    """
    success test case for writing json file
    """
    result = write_config.set_json_config("test.json", {"t": {"test": 1}})
    assert result == True


@pytest.mark.parametrize("write_config", [WriteJsonFile()], indirect=True)
def test_error_write_json_file(write_config):
    """
    error case for writing json file
    """
    result = write_config.set_json_config("test.json", "test")
    assert result == False


@pytest.mark.parametrize("write_config", [WriteEnvFile()], indirect=True)
def test_error_env_file_not_found(write_config):
    """
    error case in case env file not found
    """
    result = write_config.set_config({"test_env": 1})
    assert result == True



@pytest.mark.parametrize("write_config", [WriteEnvFile()], indirect=True)
def test_success_env_file_not_found(write_config):
    """
    env file not found test case by creating the file
    """
    with open('.env', 'w') as file:
        pass
    result = write_config.set_config({"test_env": 1})
    assert result == True
    os.remove('.env')



@pytest.mark.parametrize("write_config", [WriteEnvFile()], indirect=True)
def test_wrong_config_found(write_config):
    """
    incorrect data while saving the config
    """
    with open('.env', 'w') as file:
        pass
    result = write_config.set_config("test wrong data")
    assert result == False
    os.remove('.env')





