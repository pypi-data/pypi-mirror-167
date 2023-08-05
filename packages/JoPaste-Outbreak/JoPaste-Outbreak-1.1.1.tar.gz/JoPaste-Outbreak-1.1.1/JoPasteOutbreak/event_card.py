import csv
from JoPasteOutbreak.city import City
import json

class Event_Card:
    def __init__(self, name, event_type , area_affected, r0_difference, unemployment_rate_difference):
        self._name = name
        self._event_type = event_type
        self._area_affected = area_affected
        self.r0_difference = r0_difference
        self.unemployment_rate_difference = unemployment_rate_difference
        self._affected_cities = []

    def apply_to_affected_cities(self, City:City):
        City.r0 = round( City.r0 + self.r0_difference, 2)
        City.unemployment_rate = round(City.unemployment_rate + self.unemployment_rate_difference, 2)

    def apply_federally(self, list_of_citys):
        for city in list_of_citys:
            self.apply_to_affected_cities(city)

def load_events_from_json(file_path: str, events_list: list[Event_Card]):
    file = open(file_path, "r")
    loaded_events_list = json.load(file)
    for json_event in loaded_events_list:
        event = Event_Card(json_event["name"], json_event["event_type"], 
        json_event["area_affected"], json_event["r0_difference"], 
        json_event["unemployment_rate_difference"])
        if json_event["area_affected"] == "local":
            event._affected_cities = json_event["affected_cities"]
        events_list.append(event)
    file.close()

def load_events_from_csv(file_path: str, events_list: list[Event_Card]):
    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for event in csvreader:
            event_obj = Event_Card(event[0], event[1], event[2], float(event[3]), float(event[4]))
            if event[2] == "local":
                event_obj._affected_cities = event[5:12]
            events_list.append(event_obj)
    file.close()