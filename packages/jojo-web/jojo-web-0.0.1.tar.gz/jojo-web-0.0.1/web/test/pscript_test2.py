from pscript import py2js
from web.page import *


window = None
document = None
jQuery = None


class TestA:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("hello", self.name)


class TestB:
    def m2(self):
        print("me")


def main():
    # TestA("Peter", 18).hello()
    Object("#title").html("Hello,你好")


class Page(Element):
    tag = 'html'
    template = Head(), Body()


import random


page = Html(
    Head(),
    Body(
        Div(id="hello"),
        Div(clazz='abb')
    )
)

# print(PageUtil.random_str())

page = Body(Div("ttt"))
# page.body.add("Pure")
# page.body.\
# page.add(Div("{{content}}", clazz="{{clz}}"))

# page.body.add(Div("{{message}}", id="title"))
# vars = page.body.get_vars()
# print(vars)
print(page.html())
exit()

# page.bind_data({'message': 'Hello, world'})
# page.body.set_data({'message': 'Hello, world'})
# page.add_script(TestA, TestB, main)
# page.add_script(main)
print(page.html())
save_html(page, "test2.html")


# page.head.append(script)

# import inspect
#
# save_html(page, "test2.html")
# # print(inspect.isclass(TestA))
#
# print(inspect.isfunction(start_func))
# item = start_func
# print(item.__name__)
# print(inspect.ismethod(start_func))
# print(inspect.ismethod(TestA.hello))

# print(py2js(TestA))
