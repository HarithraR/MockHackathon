#28000

import json

def read_input_data(input_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    return data

def solve_vrp(data):
    neighborhoods = data["neighbourhoods"]
    restaurant_distances = data["restaurants"]["r0"]["neighbourhood_distance"]

    routes = {"v0": {}}
    current_capacity = 0
    current_route = []
    current_distance = 0

    for neighborhood_id in neighborhoods:
        order_quantity = neighborhoods[neighborhood_id]["order_quantity"]
        distance_to_restaurant = restaurant_distances[int(neighborhood_id[1:]) - 1]

        if current_capacity + order_quantity <= data["vehicles"]["v0"]["capacity"]:
            current_capacity += order_quantity
            current_route.append(neighborhood_id)
            current_distance += distance_to_restaurant
        else:
            current_route.append("r0")
            routes["v0"][f"path{len(routes['v0']) + 1}"] = current_route
            current_route = ["r0", neighborhood_id]
            current_capacity = order_quantity
            current_distance = distance_to_restaurant

    current_route.append("r0")
    routes["v0"][f"path{len(routes['v0']) + 1}"] = current_route

    return routes

def write_output_file(output_data, output_file):
    with open(output_file, 'w') as file:
        json.dump(output_data, file, indent=2)

def main():
    input_file = 'level1a.json'
    output_file = 'output.json'

    data = read_input_data(input_file)
    routes = solve_vrp(data)

    output_data = {"v0": routes["v0"]}
    write_output_file(output_data, output_file)
    print(f"Solution written to {output_file}")

if __name__ == "__main__":
    main()
