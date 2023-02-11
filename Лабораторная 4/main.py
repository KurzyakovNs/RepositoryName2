class vehicle:
    """Родительский класс транспортных средств"""
    def __init__(self, name:str, cost: int, access_age: int):
        self.name = name
        self.cost = cost
        self.access_age = access_age
    def __str__(self):
        return f"Название:{self.name}. Цена:{self.cost}. Возраст доступа:{self.access_age}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, topic={self.cost!r}, access_age={self.access_age!r})"
class auto(vehicle):
    """Дочерний класс автомобили"""
    def __init__(self, name: str, cost: int, access_age: int, model: int):
        super().__init__(name, cost, access_age)
        if isinstance(model, int):
            if model > 0:
                self.model = model
            else:
                raise AttributeError("error number of model")
        else:
            raise AttributeError("error number of model")
    def __str__(self):
        return f"Марка авто - {self.name}. Цена-{self.cost}. Допустимый возраст-{self.access_age}. Номер модели-{self.model}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, topic={self.cost!r}, access_age={self.access_age!r}, model={self.model!r})"
class motobike(vehicle):
    """Дочерный класс мотоциклы"""
    def __init__(self,name:str, cost: int, access_age: int, hp: int):
        super().__init__(name, cost, access_age)
        if isinstance(hp, int):
            if hp > 0:
                self.hp = hp
            else:
                raise AttributeError("error quantity of hp")
        else:
            raise AttributeError("error quantity of hp")
    def __str__(self):
        return f"Название мотоцикла-{self.name}. Цена-{self.cost}. Допустимый возраст - {self.access_age}. Лошадиных сил-{self.hp}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, topic={self.cost!r}, access_age={self.access_age!r}, hp={self.hp})"
vehicle1 = vehicle ('boeing',320000,32)
print(vehicle1)
vehicle2 = auto('BMW','32000',18, 3)
print(vehicle2)
vehicle3 = motobike('Honda',3200 , 30 , 400)
print(vehicle3)

