def check_key_exist(key: str, dictionary: dict) -> dict:
    return key in dictionary


def get_input_data(key: str, dictionary: dict) -> dict:
    if check_key_exist(key, dictionary):
        return dictionary[key]
    else:
        return {}
