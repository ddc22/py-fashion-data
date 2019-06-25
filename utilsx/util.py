import logging


class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'


def get_hash(string):
    nums = [str(ord(c)) for c in string]
    return "".join(nums)


def assert_max_length(string_val, length):
    if len(string_val) > length:
        raise Exception(
            ' Asserte failed, max string length {} for string : {} exceeded'.format(string_val, length))


def force_length(string_val, length):
    string_val = string_val.strip()
    if len(string_val) > length:
        truncated = string_val[:length]
        logging.warning(
            "Long description truncated due to size limit ["+str(length)+"] : "+string_val)
        logging.warning(
            "Long description truncated value : "+truncated)
        return truncated
    return string_val


def find_reverse_safe_split_index(string_val, max_length):
    reverse_string_val = string_val[::-1]
    string_length = len(string_val)
    if(string_length <= max_length):
        return string_length
    last_space_index = 0
    for i, char in enumerate(reverse_string_val):
        if(i+1 > max_length):
            return string_length - last_space_index
        if char is " ":
            last_space_index = i
    return string_length

# Sensitive to full stop space


def find_safe_split_index(string_val, max_length):
    string_length = len(string_val)
    if(string_length <= max_length):
        return string_length
    space_index = string_length
    full_stop_index = string_length
    for i, char in enumerate(string_val):
        if(i+1 >= max_length):
            if full_stop_index is not string_length:
                return full_stop_index + 1
            else:
                return space_index

        if char is " ":
            space_index = i
        elif char is ".":
            full_stop_index = i

    return string_length


def safe_force_reverse_length(string_val, length):
    string_val = string_val.strip()
    if len(string_val) > length:
        split_index = find_reverse_safe_split_index(string_val, length)
        truncated = string_val[split_index:]
        logging.warning(
            "Long description truncated due to size limit ["+str(length)+"] : "+string_val)
        logging.warning(
            "Long description truncated value : "+truncated)
        return truncated
    return string_val


def safe_force_length(string_val, length):
    string_val = string_val.strip()
    if len(string_val) > length:
        split_index = find_safe_split_index(string_val, length)
        truncated = string_val[:split_index]
        logging.warning(
            "Long description truncated due to size limit ["+str(length)+"] : "+string_val)
        logging.warning(
            "Long description truncated value : "+truncated)
        return truncated
    return string_val
# print(get_hash("asdsa"))
