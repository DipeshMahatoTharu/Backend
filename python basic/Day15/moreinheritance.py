# Exercise 1 (Method Overriding)

# Don't look at any example while coding.

# Create:

class Animal:
    def sound(self):
        print("Animal make a sounf ")
class Dog(Animal):
    def sound(self):
        print("Dog Bark")
dog1 = Dog()
dog1.sound()


# Method:

# sound()

# Output:

# Animal makes a sound

# Now create:

# class Dog(Animal):

# Override the same method:

# sound()

# Output:

# Dog barks

# Then:

# dog1 = Dog()
# dog1.sound()
# Expected Output
# Dog barks