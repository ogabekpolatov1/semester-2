from abc import ABC, abstractmethod
class MenuItem(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def price(self):
        pass
class Food(MenuItem):
    def price(self):
        return 50_000
class Drink(MenuItem):
    def price(self):
        return 20_000
class Dessert(MenuItem):
    def price(self):
        return 30_000


class Receipt(ABC):
    @abstractmethod
    def display(self, items):
        pass
class ConsoleReceipt(Receipt):
    def display(self, items):
        for item in items:
            print(f'{item.name}: {item.price()}')
class Repository(ABC):
    @abstractmethod
    def save(self,items):
        pass
class DbRepository(Repository):
    def save(self, items):
        for item in  items:
            print(f'INSERT INTO orders VALUES ("{item.name}", {item.price()})')
                  

class OrderSystem:
    def __init__(self):
        self.items = []
    def add(self, item: MenuItem):
        self.items.append(item)
    def run(self, receipt: Receipt, repository: Repository):
        receipt.display(self.items)
        repository.save(self.items)


order = OrderSystem()
order.add(Food("Harry"))
order.add(Drink("Hermione"))
order.add(Dessert("Ron"))

order.run(ConsoleReceipt(), DbRepository())
