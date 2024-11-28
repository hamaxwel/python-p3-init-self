class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

# Example Usage
if __name__ == "__main__":
    fido = Dog("Fido")
    print(f"Name: {fido.name}, Breed: {fido.breed}")  # Output: Name: Fido, Breed: Mutt

    snoopy = Dog("Snoopy", "Beagle")
    print(f"Name: {snoopy.name}, Breed: {snoopy.breed}")  # Output: Name: Snoopy, Breed: Beagle
