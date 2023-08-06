from web.page import *


class Button(Div):
    props = {"style": "color:red;", "@text": "Button"}


e = Div("Hello \n{{message}}", app_id="app1", style="color:{{color}};", id="message")
page = Html(Head(), Body(e, Button()))
# page.body.children.delete(page.body.div)
# page.body.children.delete(page.body.div)
page.body.add_child(Comment("this is <a> comment"))

apps = {"app1": {"message": "World", "color": "red"}}
apps = {"app1": "/jojo-web/data.json"}
apps = "/jojo-web/apps.json"
page.save_html("test2.html", apps=apps)
