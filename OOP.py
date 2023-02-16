class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def say_Hello(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}")
# creating my object
person1=person("Elon", 123)
person1.say_Hello()
person2=person("Eunice", 12)
person2.say_Hello()
person3=person("You", 11)
person3.say_Hello()
 # create a class called cars with following attributes/properties
 # make.model.year then create function that prints model and year
 # then create three
class cars:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def model_year(self):
        print(f"Car model {self.model} and year is {self.year}")
car1=cars("Bugati", "Veyron", 2022)
car1.model_year()
car2=cars("Lamborghini", "Veneno", 2026)
car2.model_year()
car3=cars("Bugati", "Mclaren", 2023)
car3.model_year()
car4=cars("BToyota", "Prado", 2012)
car4.model_year()
# another class
class movies:
    def __init__(self, actors, model, year):
        self.actors=actors
        self.model=model
        self.year=year
    def model_year(self):
        print(f"movie model {self.model}, actors {self.actors} and year is {self.year}")
movie1=movies("Top gun maverick", "Waulize", 2022)
movie1.model_year()