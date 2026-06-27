from textnode import TextNode, TextType, text_node_to_html_node
def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)

    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")


def test_bold(self):
    node = TextNode("Bold", TextType.BOLD)
    html_node = text_node_to_html_node(node)

    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "Bold")


def test_italic(self):
    node = TextNode("Italic", TextType.ITALIC)
    html_node = text_node_to_html_node(node)

    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "Italic")


def test_code(self):
    node = TextNode("print()", TextType.CODE)
    html_node = text_node_to_html_node(node)

    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "print()")


def test_link(self):
    node = TextNode(
        "Google",
        TextType.LINK,
        "https://google.com"
    )
    html_node = text_node_to_html_node(node)

    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "Google")
    self.assertEqual(
        html_node.props,
        {"href": "https://google.com"}
    )


def test_image(self):
    node = TextNode(
        "Logo",
        TextType.IMAGE,
        "logo.png"
    )
    html_node = text_node_to_html_node(node)

    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(
        html_node.props,
        {
            "src": "logo.png",
            "alt": "Logo",
        },
    )
