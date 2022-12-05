import os
def flatten_dict(dict_object, key=''):
    result = {}
    if not dict_object:
        return result

    for main_key, value in dict_object.items():
        main_key = key+main_key
        if isinstance(value, dict):
            result.update(flatten_dict(value, main_key+'.'))
        else:
            result[main_key] = value
    return result

def get_file_name(file_name):
    file_name = os.path.join(os.getcwd(), file_name)
    if os.path.exists(file_name):
        return file_name
