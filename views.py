import tornado.web
from tornado.httpclient import AsyncHTTPClient
from json import loads, dumps
import tornadoredis
import tornado.gen
import settings, models


client = tornadoredis.Client()


class RateHandler(tornado.web.RequestHandler):
    async def get(self):
        if await tornado.gen.Task(client.exists, "USDrate1"):
            rate = await tornado.gen.Task(client.get, "USDrate1")
        else:
            http = AsyncHTTPClient()
            response = await http.fetch("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
            body = loads(response.body.decode())
            rate = body["bpi"]["USD"]["rate"]
            await tornado.gen.Task(client.set, "USDrate1", rate, expire=settings.REDIS_TTL)
        self.render('templates/current_rate.html', rate=rate)

class MMainHandler(tornado.web.RequestHandler):
    async def get(self):
        if await tornado.gen.Task(client.exists, "USDrate1"):
            rate = await tornado.gen.Task(client.get, "USDrate1")
        else:
            http = AsyncHTTPClient()
            response = await http.fetch("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
            body = loads(response.body.decode())
            rate = body["bpi"]["USD"]["rate"]

            await tornado.gen.Task(client.set, "USDrate1", rate, expire=settings.REDIS_TTL)
        self.render('templates/current_rate.html', rate=rate)


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        if await tornado.gen.Task(client.exists, "USDrate1"):
            rate = await tornado.gen.Task(client.get, "USDrate1")
        else:
            http = AsyncHTTPClient()
            response = await http.fetch("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
            body = loads(response.body.decode())
            rate = body["bpi"]["USD"]["rate"]
            await tornado.gen.Task(client.set, "USDrate1", rate, expire=settings.REDIS_TTL)
        se = models.StockExchange()
        i = 0
        while i < 20:
            se.orders.append(models.Order("buy", 10000, i))
            i += 1
        await tornado.gen.Task(client.lpush, "orders", *se.save_to_json())
        se1 = models.StockExchange(await tornado.gen.Task(client.lrange, "orders", 0, -1))
        self.render('templates/current_rate.html', rate=rate, stock_exchange=se1)


class DeleteHandler(tornado.web.RequestHandler):
    async def get(self):
        await tornado.gen.Task(client.delete, "orders")
        se1 = models.StockExchange(await tornado.gen.Task(client.lrange, "orders", 0, -1))
        self.render('templates/current_rate.html', rate="111", stock_exchange=se1)


class OrderHandler(tornado.web.RequestHandler):
    async def get(self, order_id):
        if await tornado.gen.Task(client.exists, "USDrate1"):
            rate = await tornado.gen.Task(client.get, "USDrate1")
        else:
            http = AsyncHTTPClient()
            response = await http.fetch("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
            body = loads(response.body.decode())
            rate = body["bpi"]["USD"]["rate"]

            await tornado.gen.Task(client.set, "USDrate1", rate, expire=settings.REDIS_TTL)
        self.write("USD rate: {}".format(rate))
