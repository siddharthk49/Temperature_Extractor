import requests
from selectorlib import Extractor
class Temperature:
    """
    Represents temperature value extracted from timeanddate.com/weather
    """
    def __init__(self, country, city):
        self.country = country
        self.city = city


    def get(self):
        req = requests.get(f'https://www.timeanddate.com/weather/{self.country}/{self.city}')
        src = req.text
        extractor = Extractor.from_yaml_file('temperature.yaml')
        raw_result = extractor.extract(src)
        result = float(raw_result["temp"].replace("\xa0°C",""))
        print(f'The Temperature of {self.city}, {self.country} now is: {result}' )



country = input("Enter the Country: ")
city = input(("Enter the City: "))
t = Temperature(country= country, city=city)
t.get()



