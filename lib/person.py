class Person:
    def __init__(self, name):
        self.name = name

# Example Usage
if __name__ == "__main__":
    john = Person("John")
    print(f"Name: {john.name}")  # Output: Name: John

    jane = Person("Jane")
    print(f"Name: {jane.name}")  # Output: Name: Jane
