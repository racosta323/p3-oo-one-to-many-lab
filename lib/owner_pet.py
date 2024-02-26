class Pet:

    all = []

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
   
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, new_pet):
        # self._pet_type = new_pet
        pet = [pet for pet in Pet.PET_TYPES if new_pet == pet]
        if pet:
            self._pet_type = new_pet
        else:
            raise Exception
        
    def __repr__(self):
       return f'<name={self.name} type={self.pet_type} owner={self.owner}>'
   

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet,Pet):
            pet.owner = self
        else:
            raise Exception
           
    def get_sorted_pets(self):
        pets = [pet for pet in self.pets()]
        return sorted(pets, key=lambda pet: pet.name)

    
    def __repr__(self):
       return f'<owner_name={self.name}>'