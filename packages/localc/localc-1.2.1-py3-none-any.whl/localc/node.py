from .operators import *


_space = '     '
_branch = '│    '
_tee = '├─── '
_last = '└─── '


def to_string(op_name: str, prefix: list, *operands):
    prefix_str = "".join(prefix)

    if prefix:
        prefix[-1] = _branch if prefix[-1] == _tee else _space

    result = prefix_str + op_name + "\n"

    for operand in operands:
        if operand is not operands[-1]:
            result += operand.to_string(prefix + [_tee]) + '\n'
        else:
            result += operand.to_string(prefix + [_last])

    return result


class Node:
    def __init__(self, value=None):
        if isinstance(value, str):
            value = True if value.lower() == "true" else False
        elif value is None or isinstance(value, bool):
            pass
        else:
            raise Exception("Unsupported value")
        self.value = value

    def calc(self):
        if self.value is not None:
            return self.value
        else:
            raise Exception("Can't calc an empty Node")

    def __bool__(self):
        return self.calc()

    def __repr__(self):
        return "Node({0})".format(repr(self.value))

    def to_string(self, prefix):
        prefix_str = "".join(prefix)
        return str(self.value) if not prefix else prefix_str + str(self.value)

    def __str__(self):
        return self.to_string([])

    def to_descriptive_string(self):
        return repr(self.value)


class IdentifierNode(Node):
    identifiers = {}

    def __new__(cls, name=None, *args, **kwargs):
        if name in IdentifierNode.identifiers:
            return IdentifierNode.identifiers[name]
        else:
            instance = super().__new__(cls)
            IdentifierNode.identifiers[name] = instance
            return instance

    def __init__(self, name=None, value=None):
        self.name = name
        if value is not None:
            Node.__init__(self, value)
        elif "value" in self.__dict__ and isinstance(self.__dict__['value'], bool):
            # test if there's a bool value already
            pass
        else:
            Node.__init__(self)

    def calc(self):
        if self.value is not None:
            return self.value
        else:
            raise Exception("Can't calc a value with an unspecified identifier")

    def to_string(self, prefix):
        prefix_str = "".join(prefix)
        if self.value is None:
            name = "[ {} ]".format(self.name)
        else:
            name = "[ {} -> {} ]".format(self.name, self.value)
        return name if not prefix else prefix_str + name

    def __repr__(self):
        if self.value is None:
            return "IdentifierNode(\"{}\")".format(self.name)
        else:
            return "IdentifierNode(\"{}\", {})".format(self.name, self.value)

    def set_value(self, value: bool):
        assert isinstance(value, bool) or value is None, \
            "an identifier can only have a bool value"
        self.__dict__['value'] = value

    def get_value(self):
        return self.__dict__['value']

    value = property(get_value, set_value)

    @staticmethod
    def reset():
        IdentifierNode.identifiers.clear()

    def to_descriptive_string(self):
        return "[{}]".format(self.name)


class GroupNode(Node):
    def __init__(self, sub_node: Node):
        self.operand = sub_node
        Node.__init__(self)

    def calc(self):
        return self.operand.calc()

    def __bool__(self):
        return self.operand.calc()

    def __repr__(self):
        return "GroupNode({0})".format(repr(self.operand))

    def to_string(self, prefix):
        return to_string("GROUP", prefix, self.operand)

    def to_descriptive_string(self):
        return '({})'.format(
            self.operand.to_descriptive_string()
        )


class AndNode(Node):
    def __init__(self, operand1, operand2):
        if not isinstance(operand1, Node):
            operand1 = Node(operand1)
        if not isinstance(operand2, Node):
            operand2 = Node(operand2)
        self.operand1 = operand1
        self.operand2 = operand2
        Node.__init__(self)

    def calc(self):
        self.value = self.operand1.calc() and self.operand2.calc()
        return self.value

    def __repr__(self):
        return "AndNode({0}, {1})".format(repr(self.operand1), repr(self.operand2))

    def to_string(self, prefix):
        return to_string("AND", prefix, self.operand1, self.operand2)

    def to_descriptive_string(self):
        return '{}{}{}'.format(
            self.operand1.to_descriptive_string(),
            operators['and'],
            self.operand2.to_descriptive_string()
        )


class OrNode(Node):
    def __init__(self, operand1, operand2):
        if not isinstance(operand1, Node):
            operand1 = Node(operand1)
        if not isinstance(operand2, Node):
            operand2 = Node(operand2)
        self.operand1 = operand1
        self.operand2 = operand2
        Node.__init__(self)

    def calc(self):
        self.value = self.operand1.calc() or self.operand2.calc()
        return self.value

    def __repr__(self):
        return "OrNode({0}, {1})".format(repr(self.operand1), repr(self.operand2))

    def to_string(self, prefix):
        return to_string("OR", prefix, self.operand1, self.operand2)

    def to_descriptive_string(self):
        return "{} {} {}".format(
            self.operand1.to_descriptive_string(),
            operators['or'],
            self.operand2.to_descriptive_string()
        )


class XorNode(Node):
    def __init__(self, operand1, operand2):
        if not isinstance(operand1, Node):
            operand1 = Node(operand1)
        if not isinstance(operand2, Node):
            operand2 = Node(operand2)
        self.operand1 = operand1
        self.operand2 = operand2
        Node.__init__(self)

    def calc(self):
        self.value = self.operand1.calc() != self.operand2.calc()
        return self.value

    def __repr__(self):
        return "XorNode({}, {})".format(repr(self.operand1), repr(self.operand2))

    def to_string(self, prefix):
        return to_string("XOR", prefix, self.operand1, self.operand2)

    def to_descriptive_string(self):
        return "{} {} {}".format(
            self.operand1.to_descriptive_string(),
            operators['xor'],
            self.operand2.to_descriptive_string()
        )


class NotNode(Node):
    def __init__(self, operand):
        if not isinstance(operand, Node):
            operand = Node(operand)
        self.operand = operand
        Node.__init__(self)

    def calc(self):
        self.value = not self.operand.calc()
        return self.value

    def __repr__(self):
        return "NotNode({0})".format(repr(self.operand))

    def to_string(self, prefix):
        return to_string("NOT", prefix, self.operand)

    def to_descriptive_string(self):
        return "{}{}".format(
            operators['not'],
            self.operand.to_descriptive_string()
        )


class OifNode(Node):
    def __init__(self, operand1, operand2):
        if not isinstance(operand1, Node):
            operand1 = Node(operand1)
        if not isinstance(operand2, Node):
            operand2 = Node(operand2)

        self.operand1 = operand1
        self.operand2 = operand2
        Node.__init__(self)

    def calc(self):
        self.value = not self.operand1.calc() or self.operand2.calc()
        return self.value

    def __repr__(self):
        return "OifNode({}, {})".format(repr(self.operand1), repr(self.operand2))

    def to_string(self, prefix):
        return to_string("ONLY IF", prefix, self.operand1, self.operand2)

    def to_descriptive_string(self):
        return "{} {} {}".format(
            self.operand1.to_descriptive_string(),
            operators['oif'],
            self.operand2.to_descriptive_string()
        )


class IfNode(Node):
    def __init__(self, operand1, operand2):
        if not isinstance(operand1, Node):
            operand1 = Node(operand1)
        if not isinstance(operand2, Node):
            operand2 = Node(operand2)

        self.operand1 = operand1
        self.operand2 = operand2
        Node.__init__(self)

    def calc(self):
        self.value = not self.operand2.calc() or self.operand1.calc()
        return self.value

    def __repr__(self):
        return "IfNode({}, {})".format(repr(self.operand1), repr(self.operand2))

    def to_string(self, prefix):
        return to_string("IF", prefix, self.operand1, self.operand2)

    def to_descriptive_string(self):
        return "{} {} {}".format(
            self.operand1.to_descriptive_string(),
            operators['if'],
            self.operand2.to_descriptive_string()
        )


class IffNode(Node):
    def __init__(self, operand1, operand2):
        if not isinstance(operand1, Node):
            operand1 = Node(operand1)
        if not isinstance(operand2, Node):
            operand2 = Node(operand2)

        self.operand1 = operand1
        self.operand2 = operand2
        Node.__init__(self)

    def calc(self):
        both_true = self.operand1.calc() and self.operand2.calc()
        both_false = not self.operand1.calc() and not self.operand2.calc()
        self.value = both_false or both_true
        return self.value

    def __repr__(self):
        return "IffNode({}, {})".format(repr(self.operand1), repr(self.operand2))

    def to_string(self, prefix):
        return to_string("IF AND ONLY IF", prefix, self.operand1, self.operand2)

    def to_descriptive_string(self):
        return "{} {} {}".format(
            self.operand1.to_descriptive_string(),
            operators['iff'],
            self.operand2.to_descriptive_string()
        )
