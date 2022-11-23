"""The cat module allows for creating instances of :class:`Cat`."""


class Cat:
    """The :class:`Cat` class."""
    
    def __init__(self, name: str, age: int, colour: str):
        """
        Instantiates a :class:`Cat`.
        :param name: The cats name.
        :param age: The cats age.
        :param colour: The cats colour.
        """
        self._name: str = name
        self._age: int = age
        self._colour: str = colour
    
    @property
    def name(self) -> str:
        """
        The cats name.
        
        :return: The cats name.
        """
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self) -> int:
        """
        The cats age.

        :return: The cats age.
        """
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    @property
    def colour(self) -> str:
        """
        The cats colour.

        :return: The cats colour.
        """
        return self._colour

    @colour.setter
    def colour(self, colour: str):
        self._colour = colour

    def __repr__(self):
        return (f"{self.__class__.__name__}(" 
                f"name='{self.name}', " 
                f"age={self.age}, "
                f"colour='{self.colour}')")

    def __hash__(self):
        return hash((self.name, self.age, self.colour))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return hash(self) == hash(other)
        return False
help(Cat)