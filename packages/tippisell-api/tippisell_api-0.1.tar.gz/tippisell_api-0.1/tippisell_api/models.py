import typing
import pydantic


class User(pydantic.BaseModel):
    id: int
    telegram_id: str
    username: typing.Optional[str]
    balance: float
    count_purchases: typing.Optional[int]
    joined_date_timestamp: int
    last_use_timestamp: int


class Product(pydantic.BaseModel):
    id: int
    name: str
    description: str
    type: str
    price: float
    category_id: typing.Optional[int]
    min_buy: int
    max_buy: int
    is_infinitely: bool
