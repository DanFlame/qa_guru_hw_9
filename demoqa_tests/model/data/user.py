from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_year: str
    birth_month: str
    birth_day: int
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str
