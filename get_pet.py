import Pet

def main():
    pet_name = input("What should the pets name be?: ")
    pet_type = input("What type of animal is your pet?: ")
    pet_age = int(input("How old should your pet be?: "))
    my_pet = Pet.Pet(pet_name, pet_type, pet_age)

    print("Your anmials name is ", my_pet.get_name() + ", the animal is a " + my_pet.get_animal_type() + " and it is ", str(my_pet.get_age(pet_age)), " years old")


main()
