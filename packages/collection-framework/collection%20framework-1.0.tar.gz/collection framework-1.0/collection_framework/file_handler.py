def read_file(filename: str) -> str | None:
    """Read data from file"""
    data = ''
    limit = 5000
    with open(filename, 'r') as file:
        for line in file:
            if len(data) > limit:
                print(f'{filename} is too big, no more than {limit} characters')
                return None
            data += line.rstrip()
    return data
