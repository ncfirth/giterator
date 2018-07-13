import base64
import struct
import re

# There's a licence here: https://gist.github.com/Cilyan/9424144



def fnv64(string):
    res = 0xcbf29ce484222325
    for byte in string:
        res *= 0x100000001b3
        res &= 0xffffffffffffffff
        res ^= byte
    return res

def hash_fn(string):
    new_string = string.encode("ascii")
    hash_res = fnv64(new_string)
    bhash = struct.pack("<Q", hash_res)
    return base64.urlsafe_b64encode(bhash)[:-1].decode("ascii")


def remove_pattern(string, pattern):
    new_string = string.split('\n')
    new_string = [x for x in new_string if re.match(pattern, x) is None]
    return '\n'.join(new_string)


def remove_human_lines(string):
    multiline_comment = re.compile('(^\s+""".*?"""$\n)|(^\s+#.+?$)|(^\s+$)',
                                   re.DOTALL|re.MULTILINE)
    new_string = re.sub(multiline_comment, '', string)
    new_string = re.sub('\n{2,}', '\n', new_string)
    return new_string