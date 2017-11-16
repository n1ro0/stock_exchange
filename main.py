import tornado.ioloop
import wsgi


if __name__ == "__main__":
    app = wsgi.make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()