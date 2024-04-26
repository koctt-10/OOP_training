class TheredData:
    __shared_attrs = {
        'name' : 'thered_1',
        'data' : {},
        'id' : 1
    }
    
    def __init__(self) -> None:
        self.__dict__ = self.__shared_attrs
        