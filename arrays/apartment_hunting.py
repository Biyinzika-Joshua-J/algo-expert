"""

"""

def apartment_hunting_brute_force(blocks, intrested_buildings):
    distances = []
    for idx, block in enumerate(blocks):
        distance = {}
        for intrest in intrested_buildings:
            min_distance = float('inf')
            for neighbour_idx, neighbour in enumerate(blocks):
                if neighbour_idx == idx:
                    continue
                if intrest in block:
                    distance[intrest] = 0
                elif intrest in neighbour:
                    min_distance = min(min_distance, abs(idx-neighbour_idx))
                    distance[intrest] = min_distance
        
        distances.append(distance)

    # compute total distance sum
    for idx, distance in enumerate(distances):
        furthest = max([i for i in distance.values()])
        distance["furthest_distance"] = furthest
        distance["building"] = idx

    distances.sort(key=lambda x:x["furthest_distance"])
    
    return distances[0]["building"]
            


blocks = [ # => index 3
    {
        "school":True,
    },
    {
        "gym":True,
    },
    {
        "school":True,
         "gym":True,
    },
    {
        "school":True,
    },
      {
        "school":True,
         "store":True,
    },
]

intrested_buildings = ["gym", "school", "store"]

print(apartment_hunting_brute_force(blocks, intrested_buildings))