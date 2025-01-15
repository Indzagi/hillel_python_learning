class Item:
    """
    Product creation class with attributes name, price,
    description, dimensions
    """

    def __init__(self, name: str, price: int or float,
                 description: str, dimensions: str) -> None:
        """
        :param name: str
        :param price: int ore float
        :param description: str
        :param dimensions: str
        """
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) -> str:
        """
        :return: str
        """
        return f"{self.name}, price: {self.price}"

    def __repr__(self) -> tuple:
        """
        :return: tuple with item attributes
        """
        my_list_repr = (self.name, self.price,
                        self.description, self.dimensions)
        return my_list_repr


class User:
    """
    User creation class with attributes name, surname and
    phone number
    """

    def __init__(self, name: str, surname: str, number_phone: str) -> None:
        """
        :param name: str
        :param surname: str
        :param number_phone: str
        """
        self.name = name
        self.surname = surname
        self.number_phone = number_phone

    def __str__(self) -> str:
        """
        :return: str with name and surname
        """
        return f"{self.name} {self.surname}"


class Purchase:
    """
    Class creates a shopping cart with customer information, and
    makes it possible to add and change the number of products in
    the cart, as well as display the total amount of all purchases
    in the car
    """

    def __init__(self, user: User) -> None:
        """
        Function create dict products, and take user information
        :param user: Class User
        """
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item: Item, cnt: int) -> None:
        """
        Function add number of products in purchase and
        change quantity
        :param item: Class Item
        :param cnt: int number of products
        """
        self.products[item.__repr__()] = cnt

    def __str__(self) -> str:
        """
        Function return information about the buyer
         as well as products and their quantity
        :return: str
        """
        my_list_prod = list(self.products.items())
        my_iter = 0
        my_item_list = ""
        for my_list_prod[my_iter] in my_list_prod:
            my_item_list = (f"{my_item_list + my_list_prod[my_iter][0][0]}:"
                            f" {my_list_prod[my_iter][1]} pcs.\n")
            my_iter += 1
        return f"User: {self.user}\nItems:\n{my_item_list}"

    def get_total(self) -> int or float:
        """
        Function returns the sum of all
         purchases in the cart
        :return: int or float
        """
        my_list_prod = list(self.products.items())
        my_iter = 0
        self.total = 0
        for my_list_prod[my_iter] in my_list_prod:
            self.total = self.total + round(my_list_prod[my_iter][0][1] *
                                            my_list_prod[my_iter][1], 2)
            my_iter += 1
        return self.total


lemon = Item("lemon", 5, "yellow", "small")
apple = Item("apple", 2, "red", "middle")
print(lemon)
buyer = User("Ivan", "Ivanov", "02628162")
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
assert cart.get_total() == 40
