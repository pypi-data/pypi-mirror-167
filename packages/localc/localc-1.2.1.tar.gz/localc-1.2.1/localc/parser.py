from .node import *
from .operators import *

__tokens = []


def _set_token(token: list):
    global __tokens
    __tokens = token.copy()


def get_curr():
    if __tokens:
        return __tokens[0]
    else:
        return False


def match(token: str):
    if get_curr() == token.lower():
        __tokens.pop(0)
        return True
    else:
        return False


def consume(token: str, message):
    if match(token):
        return True
    raise Exception(message)


def expression(tokens: list = None) -> Node:
    if tokens is not None:
        global __tokens
        __tokens = tokens.copy()
    return logic_iff()


def logic_iff():
    expr = logic_if()

    while match("iff"):
        right = logic_if()
        expr = IffNode(expr, right)

    return expr


def logic_if():
    expr = logic_oif()

    while match("if"):
        right = logic_oif()
        expr = IfNode(expr, right)

    return expr


def logic_oif():
    expr = logic_xor()

    while match("oif"):
        right = logic_xor()
        expr = OifNode(expr, right)

    return expr


def logic_xor():
    expr = logic_or()

    while match("xor"):
        right = logic_or()
        expr = XorNode(expr, right)

    return expr


def logic_or():
    expr = logic_and()

    while match("or"):
        right = logic_and()
        expr = OrNode(expr, right)

    return expr


def logic_and():
    expr = logic_not()

    while match("and"):
        right = logic_not()
        expr = AndNode(expr, right)

    return expr


def logic_not():
    if match("not"):
        right = logic_not()
        return NotNode(right)
    return primary()


def primary():
    if match('('):
        expr = expression()
        consume(')', "Expect ')' after expression")
        return GroupNode(expr)
    if get_curr() != ')':
        curr: str = __tokens.pop(0)
        if curr.lower() in ['true', 'false']:  # keywords
            return Node(curr)
        else:  # identifier
            args = curr.split(':')
            if len(args) == 1:
                inode = IdentifierNode(curr)
            else:
                inode = IdentifierNode(args[0], args[1])
            return inode
