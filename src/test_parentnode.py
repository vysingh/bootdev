import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " normal "),
                LeafNode("i", "Italic"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold</b> normal <i>Italic</i></p>",
        )

    def test_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, []).to_html()

    def test_missing_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()


if __name__ == "__main__":
    unittest.main()
