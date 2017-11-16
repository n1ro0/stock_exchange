import tornado
import settings
from urls import urlpatterns


def make_app():
    return tornado.web.Application(urlpatterns, **settings.TORNADO_SETTINGS)