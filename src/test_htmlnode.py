import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.example.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.example.com"')

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        #print(node.to_html())
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )



if __name__ == "__main__":
    unittest.main() 