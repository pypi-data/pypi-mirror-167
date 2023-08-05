import unittest
from localc.scanner import *
from localc.parser import *


class TestParser(unittest.TestCase):
    def test_priority(self):
        tokens = scan("false or true and false")
        # print(expression(tokens))
        self.assertFalse(expression(tokens).calc())
        tokens = scan("(not false or true and false) and true")
        # print(expression(tokens))
        self.assertTrue(expression(tokens).calc())

    def test_identifier_parse(self):
        tokens = scan("not p and q")
        IdentifierNode.reset()
        root = expression(tokens)
        # print(root)
        self.assertEqual(repr(root), 'AndNode(NotNode(IdentifierNode("p")), IdentifierNode("q"))')

        tokens = scan("not p:true or q:true")
        IdentifierNode.reset()
        root = expression(tokens)
        # print(root)
        self.assertEqual(repr(root), 'OrNode(NotNode(IdentifierNode("p", True)), IdentifierNode("q", True))')

    def test_complex_parse(self):
        tokens = scan("a if b iff c oif d and f")
        IdentifierNode.reset()
        root = expression(tokens)
        # print(repr(root))
        self.assertEqual(repr(root), 'IffNode(IfNode(IdentifierNode("a"), IdentifierNode("b")), OifNode('
                                     'IdentifierNode("c"), AndNode(IdentifierNode("d"), IdentifierNode("f"))))')

        tokens = scan("a:true if b:false iff c:true oif d:false and f:true")
        IdentifierNode.reset()
        root = expression(tokens)
        # print(repr(root))
        self.assertEqual(repr(root), 'IffNode(IfNode(IdentifierNode("a", True), IdentifierNode("b", False)), OifNode('
                                     'IdentifierNode("c", True), AndNode(IdentifierNode("d", False), IdentifierNode('
                                     '"f", True))))')


if __name__ == '__main__':
    unittest.main()
