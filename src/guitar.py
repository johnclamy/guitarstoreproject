class Guitar:
    def __init__(self, serial_number: str, price: float, builder: str, model: str, guitar_type: str, backwood: str, topwood: str):
        self._serial_number = serial_number
        self._price = price
        self._builder = builder
        self._model = model
        self._guitar_type = guitar_type
        self._backwood = backwood
        self._topwood = topwood

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

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, new_builder: str):
        self._builder = new_builder
    
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model: str):
        self._model = new_model

    @property
    def guitar_type(self):
        return self._guitar_type
    
    @guitar_type.setter
    def guitar_type(self, new_type: str):
        self._guitar_type = new_type

    @property
    def backwood(self):
        return self._backwood

    @backwood.setter
    def backwood(self, new_backwood: str):
        self._backwood = new_backwood

    @property
    def topwood(self):
        return self._topwood
    
    @topwood.setter
    def topwood(self, new_topwood: str):
        self._topwood = new_topwood

    def __str__(self):
        return f"Guitar(serial_number={self._serial_number}, price={self._price}, builder={self._builder}, model={self._model}, type={self._guitar_type}, backwood={self._backwood}, topwood={self._topwood})"
