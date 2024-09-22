class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of Pet.")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string.")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Pet type must be one of: {', '.join(Pet.PET_TYPES)}")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        # If the pet is assigned an owner, add the pet to the owner's list
        if owner is not None:
            owner.add_pet(self)
