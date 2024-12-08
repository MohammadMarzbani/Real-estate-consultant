from abc import ABC,abstractmethod

def BassClass(ABC):
    _id = 0
    object_list = list()
    def __init__(self):
        self.id =  self.generate_id()
        self.store()
    @classmethod
    def  generate_id(cls):
        cls._id += 1
        return cls._id