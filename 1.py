class Dog:
    species = "Dog"   

    def __init__(self, breed, name): 
        self.breed = breed
        self.name = name

    def display(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Name:", self.name)
        print()


dog1 = Dog("Golden Retriever", "Buddy")
dog2 = Dog("German Shepherd", "Rocky")

dog1.display()
dog2.display()