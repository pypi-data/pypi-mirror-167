import time
from web.server import HttpServer, request
from web.page import *
import os


class TestClass:

    def test(self):
        return request.url

    def index(self):
        return Body(H1("Welcome To Me"))

    def hello(self, id, word="me"):
        return "Hello " + str(id) + ", word = " + str(word)

    def dict(self, name):
        print('in dict', request.args)
        return {'name': name, 'result': 0}

    def list(self):
        return [1, 88, 34]

    def number(self):
        return 99

    def exception(self):
        raise ValueError("Val invalid")


def serve():
    obj = TestClass()
    server = HttpServer(debug=True)
    # path = os.path.join(os.path.dirname(__file__), "www")
    # print(path)
    # server.static_folder("www")
    server.add_url('/', obj).run(threaded=True)
    print("start")
    time.sleep(300)
    print("stopping")
    server.stop()
    print("finished")


serve()
# Html(Body(Div("This is a page"))).save_html("www/test1.html")


