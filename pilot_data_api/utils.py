from datetime import time



    # Get value from a nested dictionary by a string of keys separated by
    # a dot i.e: "key1.key.2.key3" -> dictionary["key1"]["key2"]["key3"]

def get_nested_value(keys_string, dictionary):

    keys = keys_string.split('.')

    for key in keys:
        if isinstance(dictionary, dict) and key in dictionary:
            dictionary = dictionary[key]
        else:
            return None

    return dictionary


#Converts int type (seconds) into time object
def seconds_to_time(seconds):

    hours = seconds // 3600  # Number of hours
    seconds %= 3600
    minutes = seconds // 60  # Number of minutes
    seconds %= 60

    return time(hour=hours, minute=minutes, second=seconds)