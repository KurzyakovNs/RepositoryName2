class Vehicle:
    """Родительский класс транспортных средств"""

    def __init__(self, name:str, cost: int, access_age: int):
        self.name = name
        self.cost = cost
        self.access_age = access_age

    def __str__(self):
        return f"Название:{self.name}. Цена:{self.cost}. Возраст доступа:{self.access_age}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, topic={self.cost!r}, access_age={self.access_age!r})"

    def Info(self):
        print(f'Марка - {self.name}/ Цена - {self.cost}/ Возраст доступа - {self.access_age}')

class Auto(Vehicle):
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
        return f"Название - {self.name}. Цена-{self.cost}. Возраст доступ-{self.access_age}. Номер модели-{self.model}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, topic={self.cost!r}, access_age={self.access_age!r}, model={self.model!r})"

    def Info(self):
        print(f'Марка - {self.name}/ Цена - {self.cost}/ Возраст доступа - {self.access_age}/ Номер модели - {self.model}')

vehicle1 = Vehicle ('boeing',320000,32)
vehicle1.Info()
vehicle2 = Auto('BMW','32000',18, 3)
vehicle2.Info()

