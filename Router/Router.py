import re


def matcher(pattern, url):
    variable_pattern = r'(?P<{}>[^/]+)'

    def replacer(match):
        variable_type = match.group(1)
        if variable_type == 'str':
            return variable_pattern.format(match.group(2))
        elif variable_type == 'int':
            return r'(?P<{}>\d+)'.format(match.group(2))

    regex_pattern = re.sub(r'<(str|int):(\w+)>', replacer, pattern)
    match = re.match(f'^{regex_pattern}$', url)

    if match:
        return match.groupdict()
    return None


if __name__ == "__main__":
    print(matcher("/name", "/name"))
