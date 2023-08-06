#
# Simplify website creation
#
import re
from pscript import py2js
import inspect
import random
import json
from future.backports import html

# a fack apps in python
apps = None


# function for javascript
def main():
    Apps(apps).run()


# configurations
class Config:
    """ configurations """
    jquery_url = "http://libs.baidu.com/jquery/2.0.0/jquery.min.js"


class PageUtil:
    @staticmethod
    def html(obj, indent=0):
        """ convert object to html """
        if hasattr(obj, 'html'):
            return obj.html(indent)
        else:
            return str(obj) if obj is not None else ''

    @staticmethod
    def cameled(prop):
        """ convert property name to camel cased """
        return re.sub(r'-([a-z])', lambda m: m.group(1).upper(), prop)

    @staticmethod
    def dashed(prop):
        """ convert property name to dashed string """
        return re.sub(r'[A-Z]', lambda m: '-' + m.group().lower(), prop)

    @staticmethod
    def trim_var_quote(var_name):
        """ trim variable quote marks """
        if var_name.startswith('{') and var_name.endswith('}'):
            return var_name[1:len(var_name)-1]
        return var_name

    @staticmethod
    def random_str(prefix='', length=8):
        """ return a random string """
        ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        return prefix + ''.join(random.sample(ascii_lowercase, length))


class Variable:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def html(self, indent=0):
        val = self.value if self.value is not None else ''
        return '%s' % val

    def __repr__(self):
        return "<Variable %s>" % repr(self.name)


class Expression:

    @staticmethod
    def parse(expr_str=None, element=None):
        ex = Expression(expr_str, element)
        if len(ex.items) == 0:
            return ''
        elif len(ex.items) == 1 and isinstance(ex.items[0], str):
            return ex.items[0]
        else:
            return ex

    def __init__(self, expr=None, element=None):
        self.element = element
        self.vars = {}
        self.items = []
        if expr:
            self.load(expr)

    def load(self, expr):
        if not isinstance(expr, str):
            self.items.append(expr)
            return

        var_started = False
        varname = ""
        text = ''
        last_c = ''
        for index, c in enumerate(expr):
            if c == '{' and last_c == '{':
                text = text[:len(text) - 1]
                if text:
                    self.items.append(text)
                text = ''
                var_started = True
                varname = ''
                continue
            elif c == '}' and last_c == '}':
                varname = varname[:len(varname) - 1]
                self.items.append(Variable(varname))
                var_started = False
                varname = ''
                continue

            if var_started:
                varname += c
            else:
                text += c
            last_c = c

        if text:
            self.items.append(text)

        return self
        # if len(self.items) <= 0:
        #     return ''
        # elif len(self.items) == 1 and isinstance(self.items[0], str):
        #     return self.items[0]
        # else:
        #     return self

    def get_vars(self):
        var_list = []
        for item in self.items:
            if isinstance(item, Variable):
                var_list.append(item)
        return var_list

    def html(self, indent=0):
        ret = ''
        for item in self.items:
            ret += PageUtil.html(item)
        return ret

    def js_string(self):
        ret = ''
        for index, item in enumerate(self.items):
            if index > 0:
                ret += '`~`'

            if isinstance(item, Variable):
                ret += '{{' + item.name + '}}'
            else:
                ret += str(item)
        return html.escape(ret)

    def __repr__(self):
        ret = '['
        for index, item in enumerate(self.items):
            if index > 0:
                ret += ', '
            if isinstance(item, Variable):
                ret += '{{' + item.name + '}}' if item.name is not None else ''
            else:
                ret += str(item)
        ret += ']'
        return ret


class Children(list):
    def __init__(self, parent_element, *children):
        super().__init__()
        self.element = parent_element
        if children:
            self.add(children)

    def find(self, element):
        """ find a child element, return index """
        for index, child in enumerate(self):
            if element == child:
                return index

    def add(self, child, raw=False):
        """
        add a child element

        :param child: child element or a string
        :param raw:   (optional) whether the child is raw text
        :return: self
        """
        if not child:
            return self

        if isinstance(child, tuple):
            for c in child:
                self.add(c)
            return self

        if not isinstance(child, Element):
            child = Text(child) if not raw else child
            self.append(child)
            if isinstance(child, Element):
                child['@parent'] = self.element
        elif isinstance(child, Element):
            self.append(child)
            child['@parent'] = self.element

        return self

    def delete(self, element):
        """
        delete a child element

        :param element: element object or index int
        :return: self
        """
        if isinstance(element, int):
            if 0 <= element < len(self):
                element = self[element]
            else:
                return self

        for child in self:
            if element == child:
                self.remove(element)
                if isinstance(element, Element):
                    element['@parent'] = None
        return self

    def html(self, indent=0):
        """ convert to html """
        crlf = '\r\n' if indent > 0 else ''

        ret = ''
        for item in self:
            if isinstance(item, Element):
                val = item.html(indent) + crlf
                ret += val if val is not None else ''
            else:
                ret += str(item) if item is not None else ''
        return ret


class Element(dict):
    """ A Element is an element of HTML page """

    def __init__(self, *children, **properties):
        """
        init, add children elements, set options.

        :param children: children elements
        :param properties:  properties of the element.
        """
        super().__init__()
        tag = self._get_cls_attr('@tag', True)
        self['@tag'] = tag if tag else type(self).__name__.lower()
        self['@children'] = Children(self)
        self['@parent'] = None

        # add content from template
        template = self._get_cls_attr('template')
        if template:
            self.add_child(template)

        # add props
        props = self._get_cls_attr('props')
        if isinstance(props, dict):
            for k in props:
                if k == '@text':
                    self.add_child(props[k], raw=True)
                else:
                    self.add_prop(k, props[k])

        # add child from children
        for child in children:
            self.add_child(child)

        # add properties form kwargs
        for k in properties:
            if k == 'text':
                self.add_child(properties[k], raw=True)
            else:
                self.add_prop(k, properties[k])

    @property
    def parent(self):
        return self['@parent']

    @property
    def children(self):
        return self['@children']

    @property
    def tag(self):
        """ the tag of the element """
        return self['@tag']

    def _get_cls_attr(self, name, find_parent=True):
        """ get class static attribute of specified name """
        def get_parent_cls(cls):
            if len(cls.__bases__) > 0:
                return cls.__bases__[0]

        def find_cls(cls):
            """ find attribute in specified class """
            val = cls.__dict__.get(name, None)
            if val:
                return val

            # if find in parent is needed
            if find_parent and cls != Element:
                parent_cls = get_parent_cls(cls)
                # if parent class is Element and find '@tag'
                if parent_cls == Element and name == '@tag':
                    return cls.__name__.lower()

                # find in parent class
                if parent_cls == object:
                    return None
                elif parent_cls is not None:
                    return find_cls(parent_cls)

        return find_cls(type(self))

    @property
    def _root_parent(self):
        """ get the root parent """
        p = self
        while p.parent:
            p = p.parent
        return p

    def _html_props(self):
        """ convert properties to html """
        ret = ''
        for item in self:
            if item.startswith('@'):
                continue
            val = self[item]
            if item == 'expr_props' and isinstance(val, list):
                val = '`~`'.join(val)
            item_name = 'class' if item == 'clazz' else item
            ret += ' '
            ret += PageUtil.dashed(item_name) + '="' + html.escape(PageUtil.html(val)) + '"'
        return ret

    def add_prop(self, prop, value):
        """
        add a property

        :param prop:  property name
        :param value: property value
        :return: self
        """
        expr = Expression.parse(value)
        self[prop] = expr
        if isinstance(expr, Expression):
            var_list = expr.get_vars()
            if var_list:
                expr_props = self.get('expr_props', [])
                if prop not in expr_props:
                    expr_props.append(prop)
                self['expr_' + prop] = expr.js_string()
                self['expr_props'] = expr_props
        return self

    def add_child(self, child, raw=False):
        """
        add a child element

        :param child: child element or a string
        :param raw:   (optional) whether the child is raw text
        :return: self
        """
        self.children.add(child, raw=raw)
        return self

    def add_script(self, *codes, **kwargs):
        """
        add script

        :param codes:  list of code, code could be str or Script object
        :param kwargs: input arguments for the script
        :return: self
        """
        def js_code(name, value):
            """ convert to javascript statement 'var name=value' """
            if isinstance(value, list) or isinstance(value, dict):
                return 'var %s=%s;\n' % (name, json.dumps(value))
            elif isinstance(value, str):
                return 'var %s=%s;\n' % (name, repr(value))
            elif isinstance(value, int) or isinstance(value, float):
                return 'var %s=%s;\n' % (name, value)
            elif value is None:
                return 'var %s=null;' % name
            else:
                return 'var %s=%s;\n' % (name, str(value))

        # code list
        code_list = []

        # if not init in root element
        root = self._root_parent
        if not root.get('@init'):
            # add jquery script
            self.add_child(Script(src=Config.jquery_url))
            # add class and function for javascript
            code_list = code_list + [App, Apps, getElement]
            root['@init'] = True

        # add arguments
        for index, key in enumerate(kwargs):
            if index == 0:
                code_list.append("//arguments\n")
            code_list.append((js_code(key, kwargs[key])))

        # add codes
        code_list = code_list + list(codes)
        # create Script(object)
        self.add_child(Script(*code_list))

    def html(self, indent=0):
        """ convert to html """
        prefix = ''
        crlf = ''

        if indent is True:
            indent = 1

        if indent > 0:
            crlf = '\n'
            prefix = ' ' * (indent - 1) * 2
            indent += 1

        if self.get('@tag', None):
            ret = ''
            ret += prefix + '<' + self.tag + self._html_props() + '>' + crlf
            if len(self.children) > 0:
                ret += self.children.html(indent)
            ret += prefix + '</' + self.tag + '>'
            return ret
        else:
            return self.children.html(indent)

    def get_vars(self):
        """return a list of Variable declared within the element """
        var_list = []
        # set data of props
        for item in self:
            if item in ['tag', 'parent', 'children', '_data']:
                continue
            else:
                val = self[item]
                if isinstance(val, Expression):
                    var_list += val.get_vars()

        # set data of children
        for child in self.children:
            if isinstance(child, Element):
                var_list += child.get_vars()

        return var_list

    def __repr__(self):
        return type(self).__name__

    def __getattr__(self, item):
        if item in self:
            return self[item]

        for child in self.children:
            if isinstance(child, Element):
                if child.get('id') == item:
                    return child

        for child in self.children:
            if isinstance(child, Element):
                if child.get('@tag') == item:
                    return child

        if item == 'clazz':
            item = 'class'
        for child in self.children:
            if isinstance(child, Element):
                cls = child.get('class', '')
                if (cls + ' ').find(item+' ') >= 0:
                    return child

        return None

    def walk(self, func):
        """
        walk through the children element, for each element call function

        :param func: the function which should accept one parameter
        :return: self
        """
        func(self)
        for item in self.children:
            if isinstance(item, Element):
                item.walk(func)
        return self

    def save_html(self, filename, apps=None, encoding='utf-8'):
        """
        save element to html file

        :param filename:  html filename
        :param apps:  (optional) a diction which defines app_ids
        :param encoding:  (optional) encoding of the file
        :return: self
        """
        if apps:
            self.add_script(main, apps=apps)

        with open(filename, 'w', encoding=encoding) as f:
            f.write(self.html(True))


class NoContentElement(Element):
    def html(self, indent=0):
        return '<%s%s/>' % (self.tag, self._html_props())


class Text(Element):
    tag = 'span'

    def __init__(self, text):
        super().__init__()
        expr = Expression.parse(text)
        self['@text'] = expr
        self['@has_var'] = False

        if isinstance(expr, Expression):
            self['expr_text'] = expr.js_string()
            self['@has_var'] = True

    def html(self, indent=0):
        if self['@has_var']:
            return super().html(indent)
        else:
            return PageUtil.html(self['@text'], indent)


class Comment(Element):
    def __init__(self, text):
        super().__init__()
        self['@text'] = text

    def html(self, indent=0):
        """ convert to html """
        if indent is True:
            indent = 1
        prefix = '  ' * (indent - 1) if indent > 1 else ''
        return prefix + '<!-- ' + html.escape(self['@text']) + ' -->'


class Script(Element):
    def __init__(self, *children, **properties):
        super().__init__(**properties)

        if len(children) == 1 and isinstance(children[0], str):
            self['src'] = children[0]
            return

        last_func = ''
        stdlib = True
        for item in children:
            if isinstance(item, str):
                self.add_child('\n' + item, raw=True)
            elif inspect.isfunction(item):
                self.add_child('\n' + py2js(item), raw=True)
                last_func = item.__name__
            elif inspect.isclass(item):
                self.add_child('\n' + py2js(item, inline_stdlib=stdlib), raw=True)
                stdlib = False

        if last_func:
            self.add_child('\njQuery.ready(' + last_func + '());\n')


class A(Element):pass
class B(Element):pass
class Abbr(Element): pass
class Acronym(Element): pass
class Address(Element): pass
class Applet(Element): pass
class Area(Element): pass
class Article(Element): pass
class Aside(Element): pass
class Audio(Element): pass
class Base(Element): pass
class Basefont(Element): pass
class Bdi(Element): pass
class Bdo(Element): pass
class Big(Element): pass
class Blockquote(Element): pass
class Body(Element): pass


class Br(NoContentElement):
    tag = 'br'
    pass

class Button(Element): pass
class Canvas(Element): pass
class Caption(Element): pass
class Center(Element): pass
class Code(Element): pass
class Col(Element): pass
class Command(Element): pass
class Dd(Element): pass
class Del(Element): pass
class Details(Element): pass
class Dir(Element): pass
class Div(Element): pass
class Dialog(Element): pass
class Dl(Element): pass
class Dt(Element): pass
class Em(Element): pass
class Embed(Element): pass
class Fieldset(Element): pass
class Figcaption(Element): pass
class Figure(Element): pass
class Font(Element): pass
class Footer(Element): pass
class Form(Element): pass
class Frame(Element): pass
class Frameset(Element): pass
class H1(Element): pass
class H2(Element): pass
class H3(Element): pass
class H4(Element): pass
class H5(Element): pass
class H6(Element): pass
class Head(Element): pass
class Header(Element): pass


class Hr(NoContentElement):
    tag = 'hr'


class Html(Element): pass
class Iframe(Element): pass
class Img(Element): pass


class Input(NoContentElement):
    tag = 'input'


class Label(Element): pass
class Legend(Element): pass
class Li(Element): pass
class Link(Element): pass
class Mark(Element): pass
class Menu(Element): pass
class Menuitem(Element): pass


class Meta(NoContentElement):
    tag = 'meta'


class Nav(Element): pass
class Noframes(Element): pass
class Noscript(Element): pass
class Object(Element): pass
class Ol(Element): pass
class Optgroup(Element): pass
class Option(Element): pass
class Output(Element): pass
class Param(Element): pass
class Pre(Element): pass
class Progress(Element): pass
class Rp(Element): pass
class Rt(Element): pass
class Ruby(Element): pass
class Samp(Element): pass
class Section(Element): pass
class Select(Element): pass
class Small(Element): pass
class Source(Element): pass
class Span(Element): pass
class Strike(Element): pass
class Strong(Element): pass
class Style(Element): pass
class Sub(Element): pass
class Summary(Element): pass
class Sup(Element): pass
class Svg(Element): pass
class Table(Element): pass
class Tbody(Element): pass
class Td(Element): pass
class Template(Element): pass
class Textarea(Element): pass
class Tfoot(Element): pass
class Th(Element): pass
class Thead(Element): pass
class Time(Element): pass
class Title(Element): pass
class Tr(Element): pass
class Track(Element): pass
class Tt(Element): pass
class U(Element): pass
class Ul(Element): pass
class Var(Element): pass
class Video(Element): pass
class Wbr(Element): pass
class Xmp(Element): pass


# a fake jQuery under python
class jQuery:
    def __init__(self, obj):
        self.obj = obj

    def attr(self, name, value=None):
        if value is None:
            return self.obj[name]
        else:
            self.obj[name] = value

    def html(self, text=None):
        if text is not None:
            children = self.obj.children
            if len(children) == 1 and isinstance(children[0], Text):
                children[0].add_child(text)
            else:
                children.clear()
                children.add_child(text)
        else:
            return self.obj.children.html()


# function for javascript
def getElement(selector):
    """ this function need to call under javascript """
    return jQuery(selector)


# class for javascript
class App:
    """
    An App is an element with app_id property in the html.
    Data is bound to the children element.
    """
    def __init__(self, name):
        self.name = name
        self.elem = getElement('[app_id=%s]' % name)
        if not self.elem:
            raise Exception("App %s not found" % repr(name))

    def html_decode(self, value):
        """ decode html entities """
        if value:
            return jQuery('<div />').html(value).text()
        else:
            return ''

    def html_encode(self, value):
        """ encode html entities """
        if value:
            return jQuery('<div />').text(value).html()
        else:
            return ''

    def _is_int(self, s):
        """ whether the string is an integer """
        for c in s:
            if '0' <= c <= '9':
                pass
            else:
                return False
        return True

    def _dict_value(self, data, key, default_val=''):
        """ get value from dictionary by key. key could be xxx.xxx.xxx """
        keys = key.split('.')
        d = data
        for k in keys:
            if isinstance(d, dict) and k in d:
                d = d[k]
            elif isinstance(d, list) and self._is_int(k) and len(d) > int(k):
                d = d[int(k)]
            else:
                return default_val
        return d

    def _expression_value(self, expr_text, data):
        """ get expression value from data """
        text = ''
        if expr_text:
            expr_text = self.html_decode(expr_text)
            items = expr_text.split('`~`')
            for item in items:
                if item.startswith('{{') and item.endswith('}}'):
                    item = item[2:len(item) - 2]
                    item = self._dict_value(data, item)
                text += item
        return text

    def _set_element_text(self, e, data):
        """ update variable value in the element text from the data """
        expr_text = e.attr('expr_text')
        text = self._expression_value(expr_text, data)
        tag = e.context.nodeName.lower()
        if tag in ['pre', 'code', 'input', 'textarea']:
            e.text(text)
        else:
            text = self.html_encode(text)
            text = text.replace('\n', '<br>')
            e.html(text)

    def set_data(self, data):
        """ update variable value from the data """
        # set content text
        elems = self.elem.find('[expr_text]')
        if self.elem.attr('expr_text'):
            elems.push(self.elem)
        for i in range(elems.length):
            elem = getElement(elems[i])
            self._set_element_text(elem, data)

        # set props
        elems = self.elem.find('[expr_props]')
        if self.elem.attr('expr_props'):
            elems.push(self.elem)
        for i in range(elems.length):
            elem = getElement(elems[i])
            props = elem.attr('expr_props')
            props = props.split('`~`')
            for prop in props:
                expr_text = elem.attr('expr_' + prop)
                text = self._expression_value(expr_text, data)
                elem.attr(prop, text)

    def set_http(self, url):
        """ update variable value from the data which is get from the url """
        def on_success(result):
            self.set_data(result)

        jQuery.ajax({'url': url, 'dataType': 'JSON', 'success': on_success})


# class for javascript
class Apps:
    """ Apps"""
    def __init__(self, apps):
        """
        init the apps definition

        :param apps:  A dict of App
        """
        self.input = apps
        self.apps = {}

    def run(self):
        """ run the apps """
        def on_success(result):
            self.apps = result
            self.update()

        if isinstance(self.input, dict):
            self.apps = self.input
            self.update()
        elif isinstance(self.input, str):
            # get apps definition from the url
            jQuery.ajax({'url': self.input, 'dataType': 'JSON', 'success': on_success})

    def update(self):
        """ update all app """
        if isinstance(self.apps, dict):
            for app_id in self.apps:
                data = self.apps[app_id]
                if isinstance(data, dict):
                    App(app_id).set_data(data)
                elif isinstance(data, str):
                    App(app_id).set_http(data)

