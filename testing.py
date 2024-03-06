# class Character():
#     def __init__(self, name, planet):
#         self.name = name
#         # self.status = status
#         # self.strength = strength
#         # self.midichlorian_count = mc
#         self.home = planet
#
#     def fight(self):
#         print("Lightsaber on, says", self.name)
#
# class Jedi(Character):
#     def force_hug(self):
#         print("Feel the love force, says", self.name)
#
#     def fight(self):
#         super().fight()
#         print("Come to the light side, says", self.name)
#
# class Sith(Character):
#     def __init__(self, name, home, apprentice):
#         super().__init__(name, home)
#         self.apprentice = apprentice
#
#     def force_choke(self):
#         print("Don't choke on your words, says", self.name)
#
#     def fight(self):
#         super().fight()
#         print("Come to the dark side, says", self.name)
#
# jedi = Jedi("Luke", "Tatooine")
# sith = Sith("Darth Maul", "Dathomir", "Savage")
#
#
# print("This object we just created was " + jedi.name + " from the planet " + jedi.home)
# print("This object we just created was " + sith.name + " from the planet " + sith.home)
# jedi.fight()
# sith.fight()
# sith.force_choke()
# jedi.force_hug()
# print(sith.name, "has an apprentice called", sith.apprentice)

# class Animal():
#     def __init__(self, name):
#         print("An animal has been born.")
#         self.name = name
#     def eat(self):
#         print("Munch munch.")
#     def make_noise(self):
#         print("Grrr says "+ self.name + ".")
#
# class Cat(Animal):
#     print("A cat has been born.")
#     def make_noise(self):
#         print("Meow says "+ self.name + ".")
#
# cat = Cat("Leo")