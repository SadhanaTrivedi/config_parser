import pytest

from config_parser_package.write_config import Writer, ConfigFileWriter
from config_parser_package.read_config import ConfParser


@pytest.fixture
def write_config(request):
    conf = Writer(request.param)
    return conf

@pytest.fixture
def conf_parser(request):
    conf = ConfParser(request.param)
    return conf
