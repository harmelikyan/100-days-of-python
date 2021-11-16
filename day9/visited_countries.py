travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_name, visited, cities_visited):
  new_country = {}
  new_country["country"] = country_name
  new_country["visits"] = visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)







#🚨 Do not change the code below
add_new_country("Armenia", 20, ["Yerevan", "Gyumri", "Tatev", "Gavar"])
print(travel_log)



