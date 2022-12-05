import logging
from abc import ABC, abstractmethod
import json
import dotenv
import os


class ConfigWriter(ABC):
    """
    An abstract class to represent config writer

    Method:
    store_config : it is an abstract method, method should implement by all its concrete classes
    """
    @abstractmethod
    def store_config(self, configuration):
        """
        Abstract method: All concrete class should implement this method
        :param configuration:
        :return: NotImplementedError
        """
        raise NotImplementedError

class ConfigFileWriter(ABC):
    """
    An abstract class to represent config writer

    Method:
    store_config : it is an abstract method, method should implement by all its concrete classes
    """
    @abstractmethod
    def store_config(self, file_name, configuration):
        """
        Abstract method: All concrete class should implement this method
        :param file_name:
        :param configuration:
        :return: NotImplementedError
        """
        raise NotImplementedError

class Writer:
    """
    A factory class which implements a method set_config, by passing the object of particular ConfigWriter
    (WriteJsonFile, WriteEnvFile, WriteOsVariables) functionality provided by corresponding object will be served
    attributes: config_writer
    method : set_config
    """
    def __init__(self, config_writer):
        """
        :param config_writer:
        """
        self.config_writer = config_writer

    def set_config(self, configuration):
        """
        :param configuration:
        :return: boolean
        """
        return self.config_writer.store_config(configuration)

    def set_json_config(self, file_name, configuration):
        """
        :param file_name:
        :param configuration:
        :return: boolean
        """
        return self.config_writer.store_config(file_name, configuration)



class WriteJsonFile(ConfigFileWriter):
    """
    This class will store the given json config in json file
    method: store_config
    """

    def store_config(self, file_name, configuration):
        """
        :param file_name:
        :param configuration:
        :return: boolean
        """
        try:
            if not isinstance(configuration, dict):
                raise TypeError
            json_object = json.dumps(configuration, indent=4)
            with open(file_name, "w") as outfile:
                outfile.write(json_object)
            return True
        except Exception:
            logging.error("There is error in storing config")
            return False


class WriteEnvFile(ConfigWriter):
    """
    This class will store the config in env file
    method: store_config
    """
    def store_config(self, configuration):
        """
        :param configuration:
        :return: boolean
        """
        dotenv_file = dotenv.find_dotenv()
        try:
            if not dotenv_file:
                dotenv_file = os.path.join(os.getcwd(), '.env')
                with open(dotenv_file, 'w'):
                    pass
            dotenv.load_dotenv(dotenv_file)
            if not isinstance(configuration, dict):
                raise TypeError
            for key, value in configuration.items():
                dotenv.set_key(dotenv_file, key, str(value))
            return True
        except Exception:
            logging.error("Error in storing config")
            return False


class WriteOsVariables(ConfigWriter):
    """
    This class will store the given config in os variable
    method: store_config
    """
    def store_config(self, configuration):
        """
        :param configuration:
        :return: boolean
        """
        try:
            if not isinstance(configuration, dict):
                raise TypeError
            for key, value in configuration.items():
                os.environ[key] = str(value)
            return True
        except Exception:
            logging.error("Error in storing config")
            return False
