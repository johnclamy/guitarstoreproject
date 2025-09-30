from builder import Builder
from guitar_type import GuitarType
from guitar_string_number import GuitarStringNumber
from wood import Wood


class GuitarSpec:
    def __init__(self, builder: Builder, model: str, guitar_type: GuitarType, backwood: Wood, topwood: Wood, strings: GuitarStringNumber = GuitarStringNumber.SIX):
        self._builder = builder
        self._model = model
        self._guitar_type = guitar_type
        self._backwood = backwood
        self._topwood = topwood
        self._strings = strings

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, new_builder: Builder):
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
    def guitar_type(self, new_type: GuitarType):
        self._guitar_type = new_type

    @property
    def backwood(self):
        return self._backwood

    @backwood.setter
    def backwood(self, new_backwood: Wood):
        self._backwood = new_backwood

    @property
    def topwood(self):
        return self._topwood
    
    @topwood.setter
    def topwood(self, new_topwood: Wood):
        self._topwood = new_topwood

    @property
    def strings(self):
        return self._strings

    @strings.setter
    def strings(self, string_number: GuitarStringNumber):
        self._strings = string_number

    def __str__(self) -> str:
        return f"GuitarSpec(builder={self._builder}, model={self._model}, type={self._guitar_type}, backwood={self._backwood}, topwood={self._topwood}, strings={self._strings})"
