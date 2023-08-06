# from collections import OrderedDict
#
#
# class PageUtil:
#     @staticmethod
#     def is_list_like(obj):
#         if isinstance(obj, list) or isinstance(obj, tuple):
#             return True
#         return False
#
#     @staticmethod
#     def to_string(obj):
#         s = str(obj)
#         if s.find('"') >= 0:
#             if s.find("'") >= 0:
#                 s = s.replace('"', '&quot;')
#                 return '"' + s + '"'
#             else:
#                 return "'" + s + "'"
#         else:
#             return '"' + s + '"'
#
#
# class Clazz:
#     @staticmethod
#     def is_child(child_cls, parent_cls):
#         """ whether child_cls is the child class of parent_cls"""
#         if child_cls == parent_cls:
#             return True
#
#         bases = child_cls.__bases__
#         for base_cls in bases:
#             if Clazz.is_child(parent_cls, base_cls):
#                 return True
#
#     @staticmethod
#     def find_attr(cls, attr):
#         """ find static attribute value in cls and its parent class """
#         if attr in cls.__dict__:
#             # the cls contains attr
#             return cls.__dict__[attr]
#         else:
#             # find attr in parent class
#             bases = cls.__bases__
#             for base_cls in bases:
#                 if Clazz.is_child(base_cls, Element):
#                     ret = Clazz.find_attr(base_cls, attr)
#                     if ret:
#                         return ret
#
#
# class Props(dict):
#     def __init__(self, element):
#         self.element = element
#         super().__init__()
#
#     def add(self, props):
#         if props is None:
#             return self
#
#         if isinstance(props, dict):
#             self.element._set_options(props)
#             return self
#
#         if not isinstance(props, list) and not isinstance(props, tuple):
#             props = [props]
#
#         if isinstance(props, list) or isinstance(props, tuple):
#             for p in props:
#                 self[p] = ''
#
#         return self
#
#     def gen(self, indent=0):
#         ret = ' ' if len(self) > 0 else ''
#         for index, p in enumerate(self):
#             if index > 0:
#                 ret += ' '
#             ret += str(p) + '=' + PageUtil.to_string(self[p])
#         return ret
#
#     def __repr__(self):
#         return repr(self.keys())
#
#
# class Classes(list):
#     def __init__(self, element):
#         self.element = element
#         super().__init__()
#
#
# class Element:
#     tag = 'div'
#
#     def __init__(self, *args, **kwargs):
#         self._tag = Clazz.find_attr(type(self), 'tag') or 'div'
#         self._no_content = False
#         self._classes = Classes(self)
#         self._props = Props(self)
#         self._children = Children(self)
#         self._parent = None
#
#         if len(args) == 1:
#             if isinstance(args[0], dict):
#                 kwargs = args[0]
#                 args = ()
#
#         self._set_no_content()
#         self._create_template()
#         self._create_props()
#         self._children.add(args)
#         self._set_options(kwargs)
#
#     def _set_no_content(self):
#         if 'no_content' in self.__class__.__dict__:
#             self._no_content = True
#
#     def _create_template(self):
#         if 'template' in self.__class__.__dict__:
#             template = self.__class__.__dict__['template']
#             self.children.add(template)
#         # template = Clazz.find_attr(type(self), 'template')
#         # self.children.add(template)
#
#     def _create_props(self):
#         p = Clazz.find_attr(type(self), 'props')
#         if p:
#             if isinstance(p, dict):
#                 self._set_options(p)
#             else:
#                 self.prop.add(p)
#
#     def _set_options(self, options):
#         for key in options:
#             if key in ['cls', 'class']:
#                 key = 'class'
#                 self._props[key] = options[key]
#             else:
#                 self._props[key] = options[key]
#         return self
#
#     @property
#     def children(self):
#         return self._children
#
#     @property
#     def prop(self):
#         return self._props
#
#     def _gen_props(self, indent=0):
#         return self._props.gen(indent)
#
#     def _gen_content(self, indent=0):
#         ret = ''
#         indent = 0
#         for child in self._children:
#             ret += child.gen(indent)
#         return ret
#
#     def gen(self, indent=0):
#         if self._no_content:
#             s = self._props.gen(indent)
#             if s:
#                 return '<%s%s />' % (self._tag, s)
#             else:
#                 return '<%s>' % self._tag
#         else:
#             return '<%s%s>%s</%s>' % (self._tag, self._props.gen(indent),
#                                       self._gen_content(indent), self._tag)
#
#     def __str__(self):
#         return self.gen()
#
#
# class Text(Element):
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         super().__init__(**kwargs)
#
#     def gen(self, indent=0):
#         ret = ''
#         for arg in self.args:
#             if arg is not None:
#                 ret += str(arg)
#         return ret
#
#
# class TITLE(Element):
#     tag = 'title'
#
#
# class META(Element):
#     tag = 'meta'
#     no_content = True
#
#
# class CharSet(Element):
#     tag = 'meta'
#     no_content = True
#     props = {'http-equiv': "Content-Type", 'content': "text/html; charset=UTF-8"}
#
#     def __init__(self, encoding=None):
#         super().__init__()
#         if encoding:
#             self._props['content'] = "text/html; charset=%s" % encoding
#
#
# class BR(Element):
#     tag = 'br'
#     no_content = True
#
#
# class HEAD(Element):
#     tag = 'head'
#     template = TITLE()
#
#
# class BODY(Element):
#     tag = 'body'
#
#
# class DIV(Element):
#     tag = 'div'
#
#
# class H1(Element):
#     tag = 'h1'
#
#
# class H2(Element):
#     tag = 'h2'
#
#
# class H3(Element):
#     tag = 'h3'
#
#
# class H4(Element):
#     tag = 'h4'
#
#
# class H5(Element):
#     tag = 'h6'
#
#
# class SPAN(Element):
#     tag = 'span'
#
#
# class A(Element):
#     tag = 'a'
#
#
# class IMG(Element):
#     tag = 'img'
#
#
# class Component(Element):
#     template = None
#
#
# class Page(Component):
#     tag = 'html'
#     template = HEAD(), BODY()
#
#
# class Child(H1):
#     props = ['message']
#
#
# if __name__ == "__main__":
#     # e = H1(A(IMG(src="http://abc.com/1.png"), href='http://www.baidu.com'))
#     # print(e)
#
#     # a = META({'http-equiv': "Content-Type", 'content': "text/html; charset=UTF-8"})
#     # a = CharSet('GB2312')
#     # print(a)
#
#     p = Page(BR(), "Hello, World")
#     # p.head.title = "hello"
#     print(p)
#
#     # r = Child("自定义组件!")
#     # r.prop['message'] = "Hello"
#     # print(r)
#
#
#
