from .node import *
from .operators import *
from .scanner import *
from .parser import *
from prettytable import PrettyTable


def _bin_enumerate(items: int):
    result = [False] * items
    for bin_result in range(2 ** items):
        for i in range(items):
            result[i] = bool((bin_result >> i) & 1)
        yield list(reversed(result))


def _add_every_step(root: Node, title: dict):
    for operand_name, operand in root.__dict__.items():
        if operand_name.startswith("operand"):
            _add_every_step(operand, title)
    s = root.to_descriptive_string()
    if s not in title:
        title[s] = []


def _calc_every_step(root: Node, result: dict, calculated: list):
    for operand_name, operand in root.__dict__.items():
        if operand_name.startswith("operand"):
            _calc_every_step(operand, result, calculated)
    s = root.to_descriptive_string()
    if s not in calculated:
        result[s].append(root.calc())
        calculated.append(s)


def _search_unspecified(root: Node, identifiers: list, unspecified: list):
    for operand_name, operand in root.__dict__.items():
        if operand_name.startswith("operand"):  # get operands
            if isinstance(operand, IdentifierNode) and operand not in identifiers:  # get new identifiers
                identifiers.append(operand)
                if operand.value is None:  # get unspecified identifiers
                    unspecified.append(operand)
            _search_unspecified(operand, identifiers, unspecified)


class Proposition:
    def __init__(self, statement):
        self._statement = statement
        self._tokens = scan(statement)
        self.root: Node = expression(self._tokens)
        self.identifiers = None
        self.unspecified = None
        self.table = None
        self.columns = None
        self.init()

    def __repr__(self):
        return "Proposition(\"{}\")".format(self._statement)

    def __str__(self):
        return str(self.root)

    def calc(self):
        return self.root.calc()

    def init(self):
        self.identifiers = []
        self.unspecified = []
        if isinstance(self.root, IdentifierNode):
            self.identifiers = [self.root]
            if self.root.value is None:
                self.unspecified = [self.root]
        else:
            _search_unspecified(self.root, self.identifiers, self.unspecified)
        IdentifierNode.reset()

        self.table = PrettyTable()
        self.columns = {}
        _add_every_step(self.root, self.columns)
        self.get_truth_table()
        self.put_truth_table()

    def get_truth_table(self):
        for assignment in _bin_enumerate(len(self.unspecified)):
            for i, item in enumerate(self.unspecified):
                item: Node
                item.value = assignment[i]
            result = []
            _calc_every_step(self.root, self.columns, [])
            # self.table.add_row(result)
        for item in self.unspecified:
            item.value = None

    def put_truth_table(self):
        order = [column for column in self.columns]
        order.sort(key=str.__len__)
        for column in order:
            self.table.add_column(column, self.columns[column])
