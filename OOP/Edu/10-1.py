class Person:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        
        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight
        
    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("fio must be string")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Incorrect format fio")
        
        for s in f:
            if len(s) < 1:
                raise TypeError("fio must have one symbol")
            
p = Person("", 24, '1234 456789', 90.0)