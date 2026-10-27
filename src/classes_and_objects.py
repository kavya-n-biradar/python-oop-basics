"""Classes and objects: creating classes and instantiating objects."""


class Student:
    """A student with a name, roll number and a list of marks."""

    # Class attribute: shared by every Student object
    school = "CodeMore Academy"

    def __init__(self, name, roll_no, marks):
        """Create a student.

        Args:
            name (str): The student's name.
            roll_no (int): The student's roll number.
            marks (list): The student's marks (numbers).
        """
        # Instance attributes: each object has its own copy
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
        """Return the average of the student's marks (0 if there are none)."""
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def grade(self):
        """Return a letter grade based on the average."""
        average = self.average()
        if average >= 80:
            return "A"
        if average >= 60:
            return "B"
        if average >= 40:
            return "C"
        return "F"

    def __str__(self):
        """Return a readable description of the student."""
        return (f"{self.name} (Roll {self.roll_no}): "
                f"average {self.average():.1f}, grade {self.grade()}")


class BankAccount:
    """A bank account that protects its balance (encapsulation)."""

    def __init__(self, owner, balance=0):
        """Open an account.

        Args:
            owner (str): The account holder's name.
            balance (float): The starting balance (default 0).
        """
        self.owner = owner
        self.__balance = balance  # double underscore makes it private

    @property
    def balance(self):
        """Return the balance (read-only from outside the class)."""
        return self.__balance

    def deposit(self, amount):
        """Add money to the account.

        Raises:
            ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self.__balance += amount

    def withdraw(self, amount):
        """Take money out of the account.

        Raises:
            ValueError: If the amount is not positive or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def __str__(self):
        """Return a readable description of the account."""
        return f"{self.owner}'s account: balance {self.__balance:.2f}"


def main():
    """Create objects from both classes and use them."""
    print("=== Student class ===")
    # Instantiation: each call to Student(...) creates a new object
    student1 = Student("Asha", 1, [85, 90, 78])
    student2 = Student("Ravi", 2, [55, 62, 48])
    student3 = Student("Meera", 3, [])
    for student in (student1, student2, student3):
        print(student)
    print("School (class attribute):", Student.school)
    print("Are student1 and student2 the same object?",
          student1 is student2)

    print("\n=== BankAccount class ===")
    account = BankAccount("Kavya", 1000)
    print(account)
    account.deposit(500)
    print("After depositing 500:", account.balance)
    account.withdraw(300)
    print("After withdrawing 300:", account.balance)

    # Errors are raised by the class and handled by the caller
    for action, amount in (("withdraw", 5000), ("deposit", -50)):
        try:
            getattr(account, action)(amount)
        except ValueError as error:
            print(f"Cannot {action} {amount}: {error}")

    # Direct access to the private attribute is blocked by name mangling
    try:
        print(account.__balance)
    except AttributeError:
        print("Direct access to the private balance is not allowed.")
    print(account)


if __name__ == "__main__":
    main()