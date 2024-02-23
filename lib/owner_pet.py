import ipdb

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
            

class Owner:
    def __init__(self, name):
        self.name = name

# pet = Pet("Fido", "human")
# ipdb.set_trace()