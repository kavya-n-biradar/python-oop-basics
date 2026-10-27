# Object-Oriented Programming Concepts

Object-oriented programming (OOP) organises code around **objects** that bundle data (attributes) and behaviour (methods). It makes code easier to reuse, organise and maintain.

## Classes and objects

A **class** is a blueprint. An **object** (or instance) is something built from that blueprint.

```python
class Student:
    school = "CodeMore Academy"      # class attribute (shared)

    def __init__(self, name, marks):  # constructor
        self.name = name              # instance attribute
        self.marks = marks

student1 = Student("Asha", [85, 90])  # instantiation
```

- `__init__` runs automatically when an object is created.
- `self` refers to the object being created or used.
- Each object has its own instance attributes, while a class attribute is shared by all objects.
- `__str__` controls how an object is printed.

## Encapsulation

Encapsulation keeps data safe inside the class. `BankAccount` stores its balance in a private attribute (`__balance`) and only changes it through `deposit()` and `withdraw()`, which check the amount first. A `@property` lets outside code read the balance without changing it directly.

## Inheritance

A **subclass** inherits attributes and methods from a **parent class**, so common code is written once.

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # reuse the parent's constructor
        self.breed = breed
```

- `Dog`, `Cat` and `Bird` all inherit `describe()` from `Animal`.
- A subclass can **override** a method to change its behaviour (`Dog.speak` returns "barks").
- A subclass can add its own methods, such as `Dog.fetch()`.
- Inheritance can have several levels: `Square` inherits from `Rectangle`, which inherits from `Shape`.
- `super()` calls the parent class's version of a method.

## Polymorphism

Polymorphism means "many forms": the same method call works on different types of objects, and each one responds in its own way.

```python
for animal in animals:
    print(animal.describe())   # each object uses its own speak() and move()
```

The loop doesn't need to know whether each object is a dog, a cat or a bird. Likewise, calling `shape.area()` works for a `Rectangle`, a `Square` and a `Circle`, each with its own formula.

## Abstract classes

An abstract class, made with `ABC` and `@abstractmethod`, defines methods that every subclass **must** implement. `Shape` requires `area()` and `perimeter()`, and Python refuses to create a plain `Shape` object.

## Why OOP is useful

- **Reusability:** shared code lives in the parent class.
- **Modularity:** each class has one clear job.
- **Maintainability:** changing the parent class updates all subclasses.
- **Flexibility:** new classes can be added without changing the code that uses them.

## Where each concept appears

| Concept | File |
|---|---|
| Classes, objects, `__init__`, class attributes, `__str__` | `src/classes_and_objects.py` |
| Encapsulation and `@property` | `src/classes_and_objects.py` (`BankAccount`) |
| Inheritance, `super()`, overriding | `src/inheritance_polymorphism.py` (animals) |
| Polymorphism | `src/inheritance_polymorphism.py` (animals and shapes) |
| Abstract classes | `src/inheritance_polymorphism.py` (`Shape`) |