travel_log = [
    {
        "country" : "France",
        "visits" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visit_num, city_list):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visit_num
    new_country["cities"] = city_list
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)