import os

def urljoin(*args):
    """
    Joins given arguments into a url. Trailing but not leading slashes are
    stripped for each argument.
    https://stackoverflow.com/a/11326230
    """
    return "/".join(map(lambda x: str(x).strip('/').rstrip('/'), args))

def validate_file_path(file_path):
    if not os.path.exists(file_path):
        raise ValueError(f'File path {file_path} does not exist on the host')