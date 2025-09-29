from guitar_spec import GuitarSpec


class Guitar:
    def __init__(self, serial_number: str, price: float, spec: GuitarSpec):
        self._serial_number = serial_number
        self._price = price
        self._spec = spec

    @property
    def serial_number(self):
        return self._serial_number

    @property
    def price(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        return self._price
    
    @price.setter
    def price(self, new_price: float):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    def get_guitar_spec(self):
        return self._spec   

    def __str__(self):
        return f"Guitar(serial_number={self._serial_number}, price={self._price}, spec={self._spec})"
