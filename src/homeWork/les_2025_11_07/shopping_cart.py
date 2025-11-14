#DZ 12.2. Shopping cart

class Item:
    """
    A class that represents a product in a store.

    name (str): product name
    price (float): product price
    description (str): product description
    dimensions (str): product size or version
    """
    def __init__(self, name: str, price: float,
                 description: str, dimensions: str) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) ->str:
        """return product presentation."""
        return f"{self.name} ({self.description}, {self.dimensions}), price: {self.price}₴"

witcher = Item("The Witcher 3: Wild Hunt - Blood and Wine", 649.00, "DLC expansion", "PC edition")
lastofus = Item("The Last of Us™ Part II Remastered", 1499.00, "Story survival game", "PS5")

print(witcher)
print(lastofus)

print()

class User:
    """
    A class representing a customer.
    Attributes:
    surname (str): username
    name (str): username
    numberphone (str): phone number
    """
    def __init__(self, surname: str, name: str, numberphone: str) -> None:
        self.surname = surname
        self.name = name
        self.numberphone = numberphone

    def __str__(self) -> str:
        """Returns a string representation of the customer."""
        return (f"User:\n{self.surname} {self.name} "
                f"\nnumberphone: {self.numberphone}")

buyer = User("OfWengerberg", "Yennefer", "0987600001")
print(buyer)

print()

class Purchase:
    """
    A class representing a user's order.
    Attributes:
    user (User): the user who placed the order
    products (dict): products in the format {Item: quantity}
    total (float): the total amount of the order
    """
    def __init__(self, user: User) -> None:
        self.products: dict[Item, int] = {}
        self.user = user
        self.total = 0.0

    def add_item(self, item: Item, cnt: int) -> None:
        """Adds an item to the order."""
        self.products[item] = cnt

    def __str__(self) -> str:
        """Returns a string representation of the order."""
        items_list = []
        for item, count in self.products.items():
            items_list.append(f"{item.name}: {count} pcs.")
        items_str = "\n".join(items_list)
        return f"User: {self.user}\n\nItems:\n{items_str}"

    def get_total(self) -> float:
        """Calculates the total cost of the order."""
        total_sum = sum(item.price * self.products[item] for item in self.products)
        return total_sum

order = Purchase(buyer)
order.add_item(witcher, 1)
order.add_item(lastofus, 2)

print(f"Order:\n{order}")
print(f"Total: {order.get_total()}₴")
