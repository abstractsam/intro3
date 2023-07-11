class Base:
    def __init__(self):
        self.__a = "I have rights"
        self.b = "and privileges"
        self.c = "more rights"
        self.d = "and powers"


class Derived(Base):
    def __init__(self):
        print(self.a)  # inaccessible
        print(self.b)  # accessible
        print(self.c)  # accessible
        print(self.d)  # accessible


# Create an instance or duplicate of parent class
# you can hide proprties i code using (_) or underscore

obj1 = Base()
# print(obj1.a) - "You don't have rights and permission"
print(obj1.b)
print(obj1.c)
print(obj1.d)

# https://justpaste.it/adl6w
