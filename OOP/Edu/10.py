class Ball():
    MIN_COORD = 0
    MAX_COORD = 100
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
    
    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Er")
        else:
            return object.__getattribute__(self, item)
        
    def __setattr__(self, key, value) -> None:
        if key == "z":
            raise AttributeError("NONE")
        else:
            object.__setattr__(self, key, value)
    
    def __gelattr__(self, name: str) -> None:
        pass