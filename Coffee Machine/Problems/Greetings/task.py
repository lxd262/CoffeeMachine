class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return "Hello, I am {}!".format(self.name)


my_name = input()
sample_person = Person(my_name)
print(sample_person.greet())
