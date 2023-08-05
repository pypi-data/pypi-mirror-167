from random import randint
import json
import csv

class City:
    def __init__(self, name, population, r0):
        self._name = name
        self._population = population
        self.r0 = r0
        self.unemployment_rate = round(randint(7,12), 2)
        self.set_infected_population(self.r0, self._population)
        self.set_open_hires(self.unemployment_rate, self._population)

    def set_open_hires(self, unemployment_rate, _population):
        self._open_hires = round((unemployment_rate / 100) * _population,2 )

    def set_infected_population(self, r0, _population):
        self._infected_population = int(round(_population / r0, 0))

def load_cities_from_json(file_path: str, cities_list: list[City]):
    file = open(file_path, "r")
    loaded_cities_list = json.load(file)
    for json_city in loaded_cities_list:
        city = City(json_city["name"], 
        json_city["population"], 
        json_city["r0"])
        cities_list.append(city)
    file.close()

def load_cities_from_csv(file_path: str, cities_list: list[City]):
    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for city in csvreader:
            city_obj = City(city[0], int(city[1]), float(city[2]))
            cities_list.append(city_obj)
    file.close()