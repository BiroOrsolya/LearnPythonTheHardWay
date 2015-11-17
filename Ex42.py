# http://learnpythonthehardway.org/book/ex42.html


# Animal is-a object


class Animal(object):
    pass

# Dog is-a object


class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

# Cat is-a object


class Cat(Animal):

    def __init__(self, name):
        # cat has-a name
        self.name = name

# Person is-a object


class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is a object


class Employee(Person):

    def __init__(self, name, salary):
        # Employee has-a name and a salary hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # Employee has-a salary which is salary
        self.salary = salary

# Fish is-a object


class Fish(object):
    pass

# Salmon is-a object


class Salmon(Fish):
    pass

# halibut is-a object


class Halibut(Fish):
    pass


# rover is-a Dog

rover = Dog("Rover")

# satan is-a cat

satan = Cat("Satan")

# Mary is-a person

mary = Person("Mary")

# satan is-a pet which belongs to mary

mary.pet = satan

# Frank is a employee with a salary of 1200000

frank = Employee("Frank", 120000)

# Rover is-a pet which belongs to frank

frank.pet = rover

# Flipper is-a fish

flipper = Fish()

# crouse is-a salmon

crouse = Salmon()

# harry is-a halibut

harry = Halibut()
