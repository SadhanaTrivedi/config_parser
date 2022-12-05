
# Project Title

Config Parser Package reads configuration from file and return flat dictionary.
It can write config in .env, .json file and os variables.

#### Read Configuration:
Run the code from the location where config files are available it reads from the current working dir

#### Write Configuration:
if .env file is not available it will create in current working directory and then write.
json file will get created in current working directory

## Getting Started

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd config_parser
```

Install dependencies

```bash
  pip install -r requirements.txt
```


## Installation

Clone the project 

### Generate whl file

```bash
Go to the root of the project and run below command

py -m build

.whl file will be available inside dist folder
```

### To install whl file

```bash
py -m pip install config_parser-0.1-py3-none-any.whl
```
## Usage/Examples

### Read the configuration:

```python
import config_parser_package
from config_parser_package.read_config import YamlFile, ConfParser, ConfFile

yaml_file = ConfParser(YamlFile()) # yaml file reader
print(yaml_file.get_config("test.yml")) # pass the name of your file
```

#### ConfFile will parse the content of file if it would look like
```file
[section1]

key=value
 ```

 or 
```file 
[section1]

key:value
``` 

```python
conf_file = ConfParser(ConfFile()) # Any file having structure [section] key=value
print(conf_file.get_config("test.cfg")) # pass the name of your file

conf_file = ConfParser(ConfFile()) # Any file having structure [section] key=value
print(conf_file.get_config("test.conf")) # pass the name of your file
```

### Write the configuration

```python
from config_parser_package.write_config import Writer, WriteJsonFile,\
    WriteEnvFile, WriteOsVariables
    

#Note: If .env is not present it will create in current working directory and then write the config
write_config = Writer(WriteEnvFile())
write_config.set_config({"test": 1}) 

# create json file in current working directory
write_config = Writer(WriteJsonFile())
write_config.set_json_config("test.json", {"test":2})

write_config = Writer(WriteOsVariables())
write_config.set_config({"test": 3})

# To test the vaiable
import os 
print(os.getenv("test"))
```
