import re


def validate_input(input_str, regex_pattern, error_message):
    if not re.match(regex_pattern, input_str):
        raise ValueError(error_message)
    return input_str
