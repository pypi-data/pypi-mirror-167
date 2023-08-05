from .node import *
from .operators import *


def scan(code: str):
    result = []
    words = code.split()

    for word in words:
        identifier = word.strip('(').strip(')')
        if word.startswith('('):
            result.append('(')
        if identifier:
            result.append(identifier)
        if word.endswith(')'):
            result.append(')')

    return result
