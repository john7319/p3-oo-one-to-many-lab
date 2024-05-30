class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self, name, pet_type, owner= None):
        self.name = name 
        self.owner = owner
        if pet_type not in Pet.PET_TYPES:
            raise ValueError("Input a valid Dog")
        else:
            self.pet_type= pet_type
        Pet.all.append(self)
        if owner:
            owner.add_pet(self)
        
    

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets =[]
    def add_pet(self, pet):
        self._pets.append(pet)
        pet.owner = self
    def pets(self):
        return self._pets
    def get_sorted_pets(self):
        return sorted(self._pets, key = lambda pet: pet.name)