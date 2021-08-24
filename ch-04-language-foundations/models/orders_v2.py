import datetime
from typing import List, Optional
from pydantic import BaseModel

order_json = {
    'item_id': '123',
    'created_date': '2021-8-23 00:00',
    'pages_visited': [1, 2, '3'],
    'price': 17.22
}

order_json2 = {'item_id': '4', 'price': '25'}


class Order(BaseModel):
    item_id: int
    created_date: Optional[datetime.datetime]
    pages_visited: Optional[List[int]]
    price: float


o = Order(**order_json2)
print(o)
