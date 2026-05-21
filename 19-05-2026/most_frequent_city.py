'Given an array of order cities ["Chennai", "Madurai", "Chennai", "Salem", "Chennai"]. '
'return the most Frequent. Tests basics counting with hash maps'


def maximum_Frequent(places: list[str]):

    if len(places) == 0:
        return "Invalid Input"

    city_count = {}

    # Counting cities
    for city in places:
        if city not in city_count:
            city_count[city] = 1
        else:
            city_count[city] += 1

    # Find maximum occurring city
    max_count = 0
    result = ""

    for key in city_count:
        if city_count[key] > max_count:
            max_count = city_count[key]
            result = key

    return result


print(maximum_Frequent(["Chennai", "Madurai", "Chennai", "Salem", "Chennai"]))
