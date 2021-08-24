import datetime
from typing import List
from dateutil.parser import parse

order_json = {
    'item_id': '123',
    'created_date': '2021-8-23 00:00',
    'pages_visited': [1, 2, '3'],
    'price': 17.22
}


# class Order:
#
#     def __init__(self, item_id: int, created_date: datetime.datetime,
#                  pages_visited: List[int], price: float):
#         self.item_id = item_id
#         self.created_date = created_date
#         self.pages_visited = pages_visited
#         self.price = price
#
#     def __str__(self):
#         return str(self.__dict__)

class Order:

    def __init__(self, item_id: int, created_date: datetime.datetime,
                 pages_visited: List[int], price: float):
        if pages_visited is None:
            pages_visited = []

        try:
            self.item_id = int(item_id)
        except ValueError:
            raise Exception("Invalid item_id, it must be an integer.")

        try:
            self.created_date = parse(created_date)
        except ValueError:
            raise Exception("Invalid created_date, it must be an datetime object")

        try:
            self.pages_visited = [int(p) for p in pages_visited]
        except ValueError:
            raise Exception("invalid page list, it must be a list of integer")

        try:
            self.price = float(price)
        except ValueError:
            raise Exception("Invalid price value, it must be a float number")

    def __str__(self):
        return f"""item_id={self.item_id}, created_date={self.created_date}
                    price={self.price}, pages_visited={self.pages_visited}"""

    def __eq__(self, other):
        return isinstance(other, Order) and self.__dir__ == other.__dict__

    def __ne__(self, other):
        return isinstance(other, Order) and self.__dict__ != other.__dict__


o = Order(**order_json)
print(o)
