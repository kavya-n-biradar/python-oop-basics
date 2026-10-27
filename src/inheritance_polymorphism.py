"""Inheritance and polymorphism with animals and shapes."""

import math
from abc import ABC, abstractmethod


# ---------- Part 1: inheritance with animals ----------

class Animal:
    """Base class for all animals."""

    def __init__(self, name):
        """Create an animal with a name."""
        self.name = name

    def speak(self):
        """Return the sound the animal makes (overridden by subclasses)."""
        return "makes a sound"

    def move(self):
        """Return how the animal moves."""
        return "moves"

    def describe(self):
        """Return a sentence using this object's own speak and move."""
        return f"{self.name} {self.speak()} and {self.move()}."


class Dog(Animal):
    """A dog is an Animal that barks and can fetch."""

    def __init__(self, name, breed):
        """Create a dog, reusing Animal's __init__ through super()."""
        super().__init__(name)
        self.breed = breed

    def speak(self):
        """Override: dogs bark."""
        return "barks"

    def fetch(self):
        """A method only dogs have."""
        return f"{self.name} the {self.breed} fetches the ball."


class Cat(Animal):
    """A cat is an Animal that meows."""

    def speak(self):
        """Override: cats meow."""
        return "meows"


class Bird(Animal):
    """A bird is an Animal that tweets and flies."""

    def speak(self):
        """Override: birds tweet."""
        return "tweets"

    def move(self):
        """Override: birds fly."""
        return "flies"


# ---------- Part 2: abstract base class with shapes ----------

class Shape(ABC):
    """Abstract base class: every shape must provide area and perimeter."""

    def __init__(self, name):
        """Create a shape with a name."""
        self.name = name

    @abstractmethod
    def area(self):
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""

    def __str__(self):
        """Describe the shape (shared by every subclass)."""
        return (f"{self.name}: area = {self.area():.2f}, "
                f"perimeter = {self.perimeter():.2f}")


class Rectangle(Shape):
    """A rectangle defined by width and height."""

    def __init__(self, width, height, name="Rectangle"):
        """Create a rectangle."""
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        """Return width times height."""
        return self.width * self.height

    def perimeter(self):
        """Return twice the sum of width and height."""
        return 2 * (self.width + self.height)


class Square(Rectangle):
    """A square is a Rectangle whose sides are equal (multilevel)."""

    def __init__(self, side):
        """Create a square by reusing Rectangle's __init__."""
        super().__init__(side, side, name="Square")


class Circle(Shape):
    """A circle defined by its radius."""

    def __init__(self, radius):
        """Create a circle."""
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """Return pi times radius squared."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the circumference, 2 times pi times radius."""
        return 2 * math.pi * self.radius


def main():
    """Demonstrate inheritance and polymorphism."""
    print("=== Part 1: Animals (inheritance and method overriding) ===")
    animals = [Animal("Generic animal"), Dog("Buddy", "Labrador"),
               Cat("Whiskers"), Bird("Tweety")]

    # Polymorphism: the same call behaves differently for each object
    for animal in animals:
        print(animal.describe())

    dog = animals[1]
    print(dog.fetch())
    print("Is Buddy a Dog?", isinstance(dog, Dog))
    print("Is Buddy an Animal?", isinstance(dog, Animal))
    print("Is Whiskers a Dog?", isinstance(animals[2], Dog))

    print("\n=== Part 2: Shapes (abstract class and polymorphism) ===")
    shapes = [Rectangle(4, 5), Square(3), Circle(2)]
    for shape in shapes:
        print(shape)
    total = sum(shape.area() for shape in shapes)
    print(f"Total area of all shapes: {total:.2f}")

    # An abstract class cannot be instantiated directly
    try:
        Shape("Mystery")
    except TypeError as error:
        print("Cannot create a Shape directly:", error)


if __name__ == "__main__":
    main()