class Dog():
    def __init__(self, name, pronoun, age, size, color, breed):
        self.name = name
        self.pronoun = pronoun
        self.age = age
        self.size = size
        self.color = color
        self.breed = breed

    def introduction(self):
        print(f"My dog's name is {self.name} and {self.pronoun} is a/an {self.age} year-old, {self.size}, {self.color} {self.breed}!")


if __name__ == "__main__":


    Obiwan = Dog("Obiwan", "he", "10", "small", "white", "Morkie")
    print(Obiwan.name, Obiwan.pronoun, Obiwan.age, Obiwan.size, Obiwan.color, Obiwan.breed)
    Obiwan.introduction()

    Reuben = Dog("Reuben", "she", "12", "large", "gray", "Husky")
    print(Reuben.name, Reuben.pronoun, Reuben.age, Reuben.size, Reuben.color, Reuben.breed)
    Reuben.introduction()

    Yoru = Dog("Yoru", "he", "8", "large", "black", "Akira")
    print(Yoru.name, Yoru.pronoun, Yoru.age, Yoru.size, Yoru.color, Yoru.breed)
    Yoru.introduction()