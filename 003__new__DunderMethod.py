"""

-> __new__
In Python, __new__ is a special method that is called to create a new instance of a class before the __init__ method is invoked.
While the __init__ method is responsible for initializing the attributes of an object after it has been created, the __new__ method
is responsible for creating the instance itself.

* __new__ can be used to create singleton object of a class


-> super

In Python, super is a built-in function that is used to refer to the parent or superclass of a class.
It is often used inside a derived class (subclass) to call a method or access an attribute from its parent class.
The primary purpose of super is to enable cooperative multiple inheritance.
"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, value=None):
        if not hasattr(self, 'initilized'):
            self.value = value
            self.initialized = True


singleton1 = Singleton(value=10)
singleton2 = Singleton(value=42)

print(f"Is singleton1 and singleton2 is same ? {singleton1 is singleton2}")

print(f"Singleton1 value is {singleton1.value} and Singleton2 value is {singleton2.value}")

singleton2.value = 101

print(f"Singleton1 value is {singleton1.value} and Singleton2 value is {singleton2.value}")



"""
1. **`__new__` Method:**
   - This method checks whether the class attribute `_instance` is `None`.
   - If `_instance` is `None`, it creates a new instance of the class using `super()` and assigns it to `_instance`.
   - If `_instance` is not `None`, it returns the existing instance.
   - This ensures that only one instance of the class is created.

2. **`__init__` Method:**
   - This method is responsible for initializing the attributes of the instance.
   - It checks whether the instance has an attribute named `initialized`.
   - If `initialized` is not present, it initializes the `value` attribute and sets `initialized` to `True`.
   - This ensures that initialization logic is executed only once for each instance.

Now, let's look at the example usage:

```python
singleton1 = Singleton(value=10)
singleton2 = Singleton(value=42)

print(f"Is singleton1 and singleton2 the same? {singleton1 is singleton2}")
```

- The first two instances, `singleton1` and `singleton2`, are created. Since the Singleton pattern is implemented, both variables reference the same instance.

```python
print(f"Singleton1 value is {singleton1.value} and Singleton2 value is {singleton2.value}")
```

- Outputs the values of `value` for both instances.

```python
singleton2.value = 101

print(f"Singleton1 value is {singleton1.value} and Singleton2 value is {singleton2.value}")
```

- Modifies the `value` attribute of `singleton2` and prints the updated values for both instances.

The output demonstrates that modifying the `value` attribute of one instance affects the other, as they both reference the same underlying instance due to the Singleton pattern.


"""
