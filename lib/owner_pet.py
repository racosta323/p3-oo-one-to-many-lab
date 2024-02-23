import ipdb

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

    @property
    def pet_type(self):
        ipdb.set_trace()
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, new_pet):
        new_pet = self._pet_type
        # if (pet for pet in Pet.PET_TYPES if new_pet == pet):
        #     ipdb.set_trace()
        #     self._pet_type == new_pet
        # else: 
        #     ipdb.set_trace()
        #     raise Exception

class Owner:
    def __init__(self, name):
        self.name = name

pet = Pet("Fido", "human")
# ipdb.set_trace()