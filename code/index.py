import web

web.config.load('config.yml')
app = web.application()

app.load_apidoc('apidoc.yml')

application = app.wsgifunc()

if __name__ == '__main__':
    app.run()
