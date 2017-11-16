import json


class Order:
    def __init__(self, type, price, quantity, satisfied=0):
        self.type = type
        self.price = price
        self.quantity = quantity
        self.satisfied = satisfied

    @property
    def required(self):
        return self.quantity - self.satisfied

    def save_to_json(self):
        temp_dict = {
                    'type': self.type,
                    'price': self.price,
                    'quantity': self. quantity,
                    'satisfied': self.satisfied
                    }
        return json.dumps(temp_dict)

    @classmethod
    def create_from_json(cls, json_str):
        order = json.loads(json_str)
        return cls(order['type'], order['price'], order['quantity'], order['satisfied'])

    def __str__(self):
        return self.type + str(self.price) + str(self.quantity) + str(self.satisfied) + str(self.required)


class StockExchange:
    def __init__(self, orders=None):
        self.orders = []
        if orders != None:
            for order in orders:
                self.orders.append(Order.create_from_json(order))

    def save_to_json(self):
        temp_list = []
        for order in self.orders:
            temp_list.append(order.save_to_json())
        return temp_list