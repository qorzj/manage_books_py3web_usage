import web
from controller import add_book, update_book, detail_book, list_book, delete_book
from sqlalchemy_plugin import plugin as sql_plugin
import datetime

web.config.load('config.yml')
web.add_json_encoder(lambda x: x.strftime('%Y/%m/%d %H:%M:%S') if isinstance(x, datetime.datetime) else None)

sql_plugin.init()

app = web.application()
app.add_processor(sql_plugin.processor)
app.add_processor(
    lambda f: [
        f(),
        web.ctx.db.commit() if web.ctx.method in ['PUT', 'DELETE'] else None
    ][0]
)

app.add_mapping('/book/add', post=add_book)
app.add_mapping('/book/(?<id>[0-9]+)', get=detail_book, put=update_book, delete=delete_book)
app.add_mapping('/book/list', get=list_book)
app.add_mapping('/apidoc', get=lambda: web.apidoc)

application = app.wsgifunc()
if __name__ == '__main__':
    app.run()
