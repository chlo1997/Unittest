class Calculator():

    def addition(self, a, b):
        return a + b

    def addition2(self, a, b, c):
        return a + b + c

    def addition3(self, a, b, c):
        return a + b + c
    
    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        return a / b
    
class Aquarium():
    def add_fish_to_aquarium(self, fish_list):
        if len(fish_list) > 10:
            raise ValueError("A maximum of 10 fish can be added to the aquarium")
        return {"tank_a": fish_list}