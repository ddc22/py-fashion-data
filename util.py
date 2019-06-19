class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'

def get_hash(string):
    nums = [str(ord(c)) for c in string]
    return "".join(nums)
  

# print(get_hash("asdsa"))