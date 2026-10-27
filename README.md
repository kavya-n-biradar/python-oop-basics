# Introduction to Object-Oriented Programming in Python

A beginner Python project for the CodeMore Python Programming Internship (Week 3, Task 3). It demonstrates classes and objects, inheritance and polymorphism.

## Project Overview

- `src/classes_and_objects.py` creates a `Student` class and a `BankAccount` class, instantiates objects from them, and shows constructors, instance and class attributes, methods, `__str__` and encapsulation.
- `src/inheritance_polymorphism.py` has an `Animal` hierarchy (`Dog`, `Cat`, `Bird`) and an abstract `Shape` hierarchy (`Rectangle`, `Square`, `Circle`) to show inheritance, method overriding, `super()`, polymorphism and abstract classes.
- `docs/oop_concepts.md` explains each OOP concept used.

## Project Structure

```
python-oop-basics/
├── README.md
├── .gitignore
├── src/
│   ├── classes_and_objects.py
│   └── inheritance_polymorphism.py
└── docs/
    ├── oop_concepts.md
    └── screenshots/
```

## Requirements

- Python 3.8 or newer. No external libraries.

## Setup and How to Run

```bash
git clone https://github.com/kavya-n-biradar/python-oop-basics.git
cd python-oop-basics
python src/classes_and_objects.py
python src/inheritance_polymorphism.py
```

Both scripts run without needing any input.

## OOP Concepts Demonstrated

| Concept | Example in this project |
|---|---|
| Class and object | `Student("Asha", 1, [85, 90, 78])` creates a `Student` object |
| Constructor | `__init__` sets each object's attributes |
| Encapsulation | `BankAccount` keeps its balance private and changes it only through `deposit()` and `withdraw()` |
| Inheritance | `Dog`, `Cat` and `Bird` inherit from `Animal`; `Square` inherits from `Rectangle` |
| Method overriding | Each animal overrides `speak()`, and birds also override `move()` |
| Polymorphism | One loop calls `describe()` or `area()` on different objects, each responding in its own way |
| Abstract class | `Shape` requires `area()` and `perimeter()`, and cannot be instantiated directly |

## Console Output

### `classes_and_objects.py` (shortened)
```
=== Student class ===
Asha (Roll 1): average 84.3, grade A
Ravi (Roll 2): average 55.0, grade C
Meera (Roll 3): average 0.0, grade F
```

### `inheritance_polymorphism.py` (shortened)
```
Buddy barks and moves.
Whiskers meows and moves.
Tweety tweets and flies.

Rectangle: area = 20.00, perimeter = 18.00
Square: area = 9.00, perimeter = 12.00
Circle: area = 12.57, perimeter = 12.57
```

Full screenshots are in [`docs/screenshots/`](docs/screenshots/):
- `classes_and_objects_output.png`
- `inheritance_polymorphism_output.png`

## What I Learned

- How a class acts as a blueprint and objects are instances of it
- How `__init__`, `self`, attributes and methods work together
- How inheritance lets subclasses reuse and extend a parent class
- How polymorphism lets one piece of code work with different object types
- Why encapsulation and abstract classes make code safer and more organised

## Author

Kavya Biradar