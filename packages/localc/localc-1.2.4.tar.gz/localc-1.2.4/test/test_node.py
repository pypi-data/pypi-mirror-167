import unittest
from localc.node import *

true = Node(True)
false = Node(False)


class TestNode(unittest.TestCase):
    def test_node_pure(self):
        true_node = Node(True)
        true_node_str = Node("true")
        false_node = Node(False)
        false_node_str = Node("false")
        self.assertTrue(true_node.calc())
        self.assertTrue(true_node_str.calc())
        self.assertFalse(false_node.calc())
        self.assertFalse(false_node_str.calc())

    def test_not_node(self):
        not_node = NotNode(true)
        self.assertFalse(not_node.calc())
        not_node = NotNode(false)
        self.assertTrue(not_node.calc())

    def test_non_node_construction(self):
        not_node = NotNode(False)
        and_node = AndNode(True, False)
        self.assertTrue(not_node.calc())
        self.assertFalse(and_node.calc())

    def test_bool(self):
        not_node = NotNode(False)
        self.assertTrue(not_node)

    def test_and_node(self):
        and1 = AndNode(false, false)
        and2 = AndNode(false, true)
        and3 = AndNode(true, false)
        and4 = AndNode(true, true)
        self.assertFalse(and1)
        self.assertFalse(and2)
        self.assertFalse(and3)
        self.assertTrue(and4)

    def test_or_node(self):
        or1 = OrNode(false, false)
        or2 = OrNode(false, true)
        or3 = OrNode(true, false)
        or4 = OrNode(true, true)
        self.assertFalse(or1)
        self.assertTrue(or2)
        self.assertTrue(or3)
        self.assertTrue(or4)

    def test_repr(self):
        node = AndNode(NotNode(true), false)
        self.assertEqual(repr(node), "AndNode(NotNode(Node(True)), Node(False))")

    def test_str(self):
        node = AndNode(OrNode(NotNode(true), false), AndNode(true, false))
        self.assertEqual(str(node),
                         """AND
├─── OR
│    ├─── NOT
│    │    └─── True
│    └─── False
└─── AND
     ├─── True
     └─── False"""
                         )

    def test_group_node(self):
        node = AndNode(true, GroupNode(OrNode(true, false)))
        self.assertTrue(node.calc())
        self.assertEqual(
            repr(node),
            "AndNode(Node(True), GroupNode(OrNode(Node(True), Node(False))))"
        )

    def test_identifier_node(self):
        node = AndNode(IdentifierNode("p"), IdentifierNode("q"))
        self.assertEqual(repr(node), 'AndNode(IdentifierNode("p"), IdentifierNode("q"))')
        try:
            node.calc()
        except Exception as ex:
            self.assertEqual(str(ex), "Can't calc a value with an unspecified identifier")

        node = AndNode(IdentifierNode("p", True), IdentifierNode("q", False))
        self.assertEqual(repr(node), 'AndNode(IdentifierNode("p", True), IdentifierNode("q", False))')
        self.assertFalse(node.calc())
        IdentifierNode.reset()

    def test_oif_node(self):
        oif1 = OifNode(false, false)
        oif2 = OifNode(false, true)
        oif3 = OifNode(true, false)
        oif4 = OifNode(true, true)
        self.assertTrue(oif1)
        self.assertTrue(oif2)
        self.assertFalse(oif3)
        self.assertTrue(oif4)

    def test_if_node(self):
        if1 = IfNode(false, false)
        if2 = IfNode(false, true)
        if3 = IfNode(true, false)
        if4 = IfNode(true, true)
        self.assertTrue(if1)
        self.assertFalse(if2)
        self.assertTrue(if3)
        self.assertTrue(if4)

    def test_iff_node(self):
        iff1 = IffNode(false, false)
        iff2 = IffNode(false, true)
        iff3 = IffNode(true, false)
        iff4 = IffNode(true, true)
        self.assertTrue(iff1)
        self.assertFalse(iff2)
        self.assertFalse(iff3)
        self.assertTrue(iff4)

    def test_xor_node(self):
        xor1 = XorNode(false, false)
        xor2 = XorNode(false, true)
        xor3 = XorNode(true, false)
        xor4 = XorNode(true, true)
        self.assertFalse(xor1)
        self.assertTrue(xor2)
        self.assertTrue(xor3)
        self.assertFalse(xor4)


if __name__ == '__main__':
    unittest.main()
