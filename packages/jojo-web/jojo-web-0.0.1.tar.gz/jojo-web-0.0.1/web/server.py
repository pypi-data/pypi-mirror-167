import flask
from flask import Flask
from werkzeug.serving import make_server

import threading
import logging
import inspect
from inspect import Parameter
from collections import OrderedDict
import os
import re


# request from flask
request = flask.request

# render_template from flask
render_template = flask.render_template


class HttpServer:
    """
    Http server.

    Example:

    HttpServer(port=8080).run(threaded=True)

    """
    WelcomeHtml = '<html><body><h1>Welcome</h1></body></html>'

    FileExts = ['.txt', '.htm', '.html', '.jpg', '.jpeg', '.css', '.gif', '.png',
                '.wav', '.mp3', '.mp4', '.mpg', '.mpeg', '.m3u', '.flv',
                '.json', '.js', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx']

    def __init__(self, port=80, ip='0.0.0.0', debug=False, app=None):
        """
        Http server

        :param port:  server post
        :param ip:    ip address, '0.0.0.0' or '127.0.0.1'
        :param debug: (optional) whether in debug mode
        :param app:   (optional) flask app object
        """
        self.ip = ip if isinstance(ip, str) else '0.0.0.0'
        self.port = port
        self.app: flask.Flask = app  # flask app
        self.debug = debug
        self._server = None
        self._has_root = False
        self._static_folder = None
        self._static_url_path = None

    def _confirm_app(self):
        """ confirm self.app is initialized """
        if self.app is None:
            self.app = Flask(__name__)

    def _get_func_params(self, func):
        """ get func parameters ans its values, return a dict """
        defaults = OrderedDict()
        if inspect.ismethod(func) or inspect.isfunction(func):
            params = inspect.signature(func).parameters
            for i in params:
                if params[i].default == Parameter.empty:
                    defaults[params[i].name] = None
                else:
                    defaults[params[i].name] = params[i].default
        return defaults

    def _convert_return_value(self, ret):
        """ convert return value to flask response value """
        status_code = 200
        if isinstance(ret, tuple) and len(ret) == 2 and isinstance(ret[1], int):
            status_code = ret[1]
            ret = ret[0]

        if isinstance(ret, str):
            # return string
            return ret, status_code
        elif isinstance(ret, Exception):
            name = ret.__class__.__name__
            ret = {'return_value': -1, 'exception': name + ': ' + str(ret)}
            return flask.jsonify(ret), 500
        elif hasattr(ret, 'html') and inspect.ismethod(getattr(ret, 'html')):
            # for Element, convert to html
            return ret.html(), status_code
        elif isinstance(ret, dict):
            return flask.jsonify(ret), 200
        elif isinstance(ret, list):
            return flask.jsonify(ret), 200
        elif isinstance(ret, int) or isinstance(ret, float):
            ret = {'return_value': ret}
            return flask.jsonify(ret), 200
        else:
            return str(ret), status_code

    def _decorator(self, func, defaults):
        """ decorate the func """
        def inner(*args):
            print('request.args', request.args)

            kwargs = OrderedDict()  # kwargs to call func
            for name in defaults:
                # get default value
                val = defaults[name]
                # if arg name exists in request
                # replace value with request
                if name in request.args:
                    val = request.args[name]
                kwargs[name] = val
            # call func with kwargs
            try:
                ret = func(**kwargs)
            except Exception as e:
                ret = e
            # analysis return value
            return self._convert_return_value(ret)

        return inner

    def _find_static_file(self, path):
        if self._static_folder and ServerUtil.is_valid_path(path):
            filename = self._static_folder + path
            if os.path.exists(filename):
                return filename
        return ''

    def _on_404_not_found(self, e):
        """ process when 404 not found"""
        file_ext = ServerUtil.file_ext(request.path)
        if file_ext not in HttpServer.FileExts:
            return e

        filename = self._find_static_file(request.path)
        if filename:
            # url = self._static_url_path + request.path
            # return flask.redirect(url)
            return flask.send_file(filename)
        else:
            return e

    def add_url(self, url_rule, view_func, endpoint=None):
        """
        add url rule

        :param url_rule: url rule, such as "/bin"
        :param view_func: function or method or object
        :param endpoint: (optinal) endpoint name str
        :return: self
        """
        self._confirm_app()

        if inspect.ismethod(view_func) or inspect.isfunction(view_func):
            # add url_rule from function
            # auto detect endpoint name
            if endpoint is None:
                if view_func:
                    url = url_rule if url_rule.endswith('/') else url_rule + '/'
                    endpoint = url + view_func.__name__

            if url_rule == '/':
                self._has_root = True

            params = self._get_func_params(view_func)
            func = self._decorator(view_func, params)
            self.app.add_url_rule(url_rule, endpoint, func, methods=['POST', 'GET'])
            # if params:
            #     func = self._decorator(view_func, params)
            #     self.app.add_url_rule(url_rule, endpoint, func)
            # else:
            #     self.app.add_url_rule(url_rule, endpoint, view_func)

        elif view_func is not None:
            # add url_rule from object
            obj = view_func

            if not url_rule.endswith('/'):
                url_rule += '/'

            for name, method in inspect.getmembers(obj):
                if not name.startswith('_'):
                    if inspect.ismethod(method):
                        if name == 'index':
                            url = url_rule
                        else:
                            url = url_rule + name
                        self.add_url(url, method)

        return self

    def _index_page(self):
        """ default home page of the server """
        return HttpServer.WelcomeHtml

    def static_folder(self, path, url=None):
        """ set static folder """
        if not (path.startswith("/") or path.find(':') == 1):
            path = os.path.join(os.getcwd(), path)

        if not os.path.exists(path):
            raise ValueError("Path %s not exists" % path)

        self._static_folder = path
        self._static_url_path = url
        return self

    def _prepare_static_folder(self):
        # static folder
        static_folder = self._static_folder
        if not static_folder:
            path = os.path.join(os.getcwd(), "www")
            if os.path.exists(path):
                static_folder = path
                self._static_folder = path

        if os.path.exists(static_folder):
            self.app.static_folder = static_folder
            if not self._static_url_path:
                self._static_url_path = 'static'
            self.app.static_url_path = self._static_url_path

    def run(self, threaded=False):
        """
        run the server

        :param threaded: (optional) whether run in thread
        :return: self
        """
        self._confirm_app()
        self._prepare_static_folder()

        # register 404 handler
        self.app.register_error_handler(404, self._on_404_not_found)

        # add default page
        if not self._has_root:
            self.add_url('/', self._index_page)

        if threaded:
            self._server = ServerThread(self.app, self.port, self.ip)
            self._server.start()
        else:
            self.app.run(host=self.ip, port=self.port, debug=self.debug)

        return self

    def stop(self):
        """ stop the server (available when run in thread) """
        if self._server:
            self._server.shutdown()
            self._server = None
            self.app = None
        return self


class ServerUtil:
    @staticmethod
    def file_ext(path):
        if isinstance(path, str):
            offset = path.find("?")
            path = path[:offset] if offset >= 0 else path
            offset = path.rfind('.')
            if offset:
                return path[offset:].lower()
        return ''

    @staticmethod
    def is_valid_path(path):
        if not isinstance(path, str):
            return False

        if path.find('..') >= 0:
            return False

        if re.search('[?$#]', path):
            return False

        return True


class ServerLogFilter(logging.Filter):
    def __init__(self, name='', log_file=None):
        super().__init__(name=name)
        self.log_file = log_file
        # self.logger = logging.Logger()

    def filter(self, rec):
        return False
        # filter all records except ERROR
        # return rec.levelno == logging.ERROR


class ServerThread(threading.Thread):
    # https://pyquestions.com/how-to-stop-flask-application-without-using-ctrl-c
    def __init__(self, flask_app, port, host='0.0.0.0', log_file=None):
        """  A server thread """
        super().__init__()
        self.log_file = log_file
        self.server = make_server(host, port, flask_app, threaded=True)
        self.change_logger()
        self.ctx = flask_app.app_context()
        self.ctx.push()

    def change_logger(self):
        logger = logging.getLogger("werkzeug")
        if logger:
            logger.addFilter(ServerLogFilter())
        # print(logger)
        # for handler in logger.handlers:
        #     print(handler)

        # # Create handlers
        # c_handler = logging.StreamHandler()
        # f_handler = logging.FileHandler('file.log')
        # c_handler.setLevel(logging.WARNING)
        # f_handler.setLevel(logging.INFO)
        #
        # # Create formatters and add it to handlers
        # c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        # f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # c_handler.setFormatter(c_format)
        # f_handler.setFormatter(f_format)
        #
        # # Add handlers to the logger
        # logger.addHandler(c_handler)
        # logger.addHandler(f_handler)

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()
