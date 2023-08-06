import unittest
from web.page import *


class TestUtil(unittest.TestCase):
    def test_dashed(self):
        s = "text-color"
        dashed = PageUtil.dashed(s)
        self.assertEqual(dashed, 'text-color')
        cameled = PageUtil.cameled(dashed)
        self.assertEqual(cameled, 'textColor')

        s = "TextColor"
        dashed = PageUtil.dashed(s)
        self.assertEqual(dashed, '-text-color')
        cameled = PageUtil.cameled(dashed)
        self.assertEqual(cameled, 'TextColor')

        s = "color"
        dashed = PageUtil.dashed(s)
        self.assertEqual(dashed, 'color')
        cameled = PageUtil.cameled(dashed)
        self.assertEqual(cameled, 'color')

    def test_html(self):
        pass


class TestExpression(unittest.TestCase):
    def test_parse(self):
        ret = Expression("hello")
        self.assertEqual(len(ret.items), 1)
        self.assertEqual(ret.items[0], "hello")

        ret = Expression("hello, {{name}}")
        self.assertEqual(len(ret.items), 2)
        self.assertEqual(ret.items[0], "hello, ")
        self.assertEqual(type(ret.items[1]), Variable)


class TestElement(unittest.TestCase):
    def test1(self):
        self.assertEqual(Element().html(), '<element></element>')
        self.assertEqual(Html().html(), '<html></html>')
        self.assertEqual(Div("text").html(), '<div>text</div>')
        self.assertEqual(Div(id=3).html(), '<div id="3"></div>')
        self.assertEqual(Br().html(), '<br/>')
        self.assertEqual(Meta(charset="utf-8").html(), '<meta charset="utf-8"/>')


if __name__ in "__main__":
    unittest.main()
