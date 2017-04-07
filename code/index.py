import web
from controller import add_book, update_book, detail_book, list_book, delete_book

web.config.load('config.yml')


def global_filter(f):
    web.header('Access-Control-Allow-Origin', '*')
    web.header('Access-Control-Allow-Headers', 'Cache-Control, Accept-Encoding, token, Origin, X-Requested-With, Content-Type, Accept, Authorization,Referer,User-Agent')
    if web.ctx.method == 'OPTIONS':
        return ''
    return f()


app = web.application()
app.add_processor(global_filter)

app.add_mapping('/book/add', post=add_book)
app.add_mapping('/book/(?<id>[0-9]+)', get=detail_book, put=update_book, delete=delete_book)
app.add_mapping('/book/list', get=list_book)
app.add_mapping('/apidoc', get=lambda: web.apidoc)

application = app.wsgifunc()
if __name__ == '__main__':
    app.run()
