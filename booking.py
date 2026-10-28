from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Booking:
    passenger_name: str
    train_number: str
    fare: float
    pnr: str


def create_booking(
    passenger_name: str,
    train_number: str,
    fare: float
) -> Booking:
    if not passenger_name.strip():
        raise ValueError("Passenger name is required")

    if not train_number.strip():
        raise ValueError("Train number is required")

    if fare <= 0:
        raise ValueError("Fare must be greater than zero")

    pnr = uuid4().hex[:10].upper()
    return Booking(passenger_name, train_number, float(fare), pnr)