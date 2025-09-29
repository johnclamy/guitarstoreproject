from builder import Builder
from guitar_type import GuitarType
from wood import Wood


class GuitarSpec:
    def __init__(self, builder: Builder, model: str, guitar_type: GuitarType, backwood: Wood, topwood: Wood):
        self._builder = builder
        self._model = model
        self._guitar_type = guitar_type
        self._backwood = backwood
        self._topwood = topwood

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

    def __str__(self) -> str:
        return f"GuitarSpec(builder={self._builder}, model={self._model}, type={self._guitar_type}, backwood={self._backwood}, topwood={self._topwood})"
