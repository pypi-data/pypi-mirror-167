import unittest
from localc.proposition import *
from localc.proposition import _bin_enumerate
from io import StringIO


class TestProposition(unittest.TestCase):
    def test_proposition_pure(self):
        p = Proposition("s:true and (false or true)")
        self.assertTrue(p.calc())

    def test_init(self):
        p = Proposition("a and b or c")
        try:
            p.calc()
        except Exception as ex:
            self.assertEqual(str(ex), "Can't calc a value with an unspecified identifier")

        values = [True, False, True]
        for unspecified, value in zip(p.unspecified, values):
            unspecified: IdentifierNode
            unspecified.value = value
        self.assertTrue(p.calc())

    def test_bin_enum(self):
        answer = "[False, False, False, False, False] [False, False, False, False, True] [False, False, False, True, " \
                 "False] [False, False, False, True, True] [False, False, True, False, False] [False, False, True, " \
                 "False, True] [False, False, True, True, False] [False, False, True, True, True] [False, True, " \
                 "False, False, False] [False, True, False, False, True] [False, True, False, True, False] [False, " \
                 "True, False, True, True] [False, True, True, False, False] [False, True, True, False, True] [False, " \
                 "True, True, True, False] [False, True, True, True, True] [True, False, False, False, False] [True, " \
                 "False, False, False, True] [True, False, False, True, False] [True, False, False, True, " \
                 "True] [True, False, True, False, False] [True, False, True, False, True] [True, False, True, True, " \
                 "False] [True, False, True, True, True] [True, True, False, False, False] [True, True, False, False, " \
                 "True] [True, True, False, True, False] [True, True, False, True, True] [True, True, True, False, " \
                 "False] [True, True, True, False, True] [True, True, True, True, False] [True, True, True, True, " \
                 "True] "
        result = StringIO()
        for gen in _bin_enumerate(5):
            print(list(gen), end=' ', file=result)
        result = result.getvalue()
        self.assertEqual(answer, result)

    def test_unspecified(self):
        p = Proposition("a and b and a")
        self.assertEqual(len(p.unspecified), 2)
        self.assertEqual(len(p.identifiers), 2)

        q = Proposition("a or b and a:true")
        self.assertEqual(len(q.unspecified), 1)
        self.assertEqual(len(q.identifiers), 2)

    def test_same_identifier(self):
        r = Proposition("a:false and a:true and b:true and a")
        self.assertTrue(r.calc())


if __name__ == '__main__':
    unittest.main()
