from abc import ABC, abstractmethod
from config_parser_package.utils import flatten_dict, get_file_name
import configparser
import logging
import yaml
import os


class FileConfParser(ABC):
    """
    An abstract class to represent config parser

    Method:
    parse_config : it is an abstract method and should implement by all its concrete classes
    """
    @abstractmethod
    def parse_config(self, file_name):
        """
        Abstract method: All concrete class should implement this method
        :param file_name:
        :return: NotImplementedError
        """
        raise NotImplementedError


class ConfParser:
    """
    A factory class which implements a method get config, pass the object of desired FileConfParser
    (ConfFile, YamlFile) to get the response as flat dict
    attributes: file_conf
    method : get_config
    """
    def __init__(self, file_conf):
        """
        :param file_conf:
        """
        self.file_conf = file_conf

    def get_config(self, file_name):
        """
        :param file_name:
        :return: dict
        """
        config = self.file_conf.parse_config(file_name)
        return flatten_dict(config)


class ConfFile(FileConfParser):
    """
    Class will parse configuration file contains the structure
    [Simple Values]
    key=value
    [Simple Values1]
    key:value
    method: parse_config
    """
    def parse_config(self, file_name):
        """
        :param file_name:
        :return: dict
        """
        try:
            file_name = get_file_name(file_name)
            if not file_name:
                raise FileNotFoundError
            parser_obj = configparser.ConfigParser()
            parser_obj.read(file_name)
            config_obj = {section_name: dict(parser_obj[section_name])
                          for section_name in parser_obj.sections()}
            return config_obj
        except Exception as ex:
            logging.error("There is some error in reading file %s", ex)
            raise RuntimeError

class YamlFile(FileConfParser):
    """
    This class will parse the config from yaml file
    method: parse_config
    """
    def parse_config(self, file_name):
        """
        :param file_name:
        :return: dict
        """
        try:
            file_name = get_file_name(file_name)
            if not file_name:
                raise FileNotFoundError
            
            with open(file_name, 'r') as file:
                config_obj = yaml.safe_load(file)
            return config_obj
        except Exception:
            logging.error("There is some error in reading file")
            raise RuntimeError
