# Drone Flight Planner
# You’re an engineer at a disruptive drone delivery startup and your CTO
# asks you to come up with an efficient algorithm that calculates the minimum
# amount of energy required for the company’s drone to complete its flight.
# You know that the drone burns 1 kWh(kilowatt-hour is an energy unit) for every mile
# it ascends, and it gains 1 kWh for every mile it descends.
# Flying sideways neither burns nor adds any energy.

# Given an array route of 3D points, implement a function calcDroneMinEnergy that computes and returns
# the minimal amount of energy the drone would need to complete its route.
# Assume that the drone starts its flight at the first point in route.
# That is, no energy was expended to place the drone at the starting point.

# For simplicity, every 3D point will be represented as an integer array whose length is 3.
# Also, the values at indexes 0, 1, and 2 represent the x, y and z coordinates in a 3D point, respectively.

# Explain your solution and analyze its time and space complexities.

def calc_drone_min_energy(route):
    maxH = route[0][2]
    for i in range(1, len(route)):
        maxH = route[i][2]
    return maxH - route[0][2]


print(calc_drone_min_energy([[0, 2, 10], [10, 10, 0]])) # 0
print(calc_drone_min_energy([[0, 2, 6], [10, 10, 20]]))  # 14
print(calc_drone_min_energy(
    [[0, 2, 10], [10, 10, 0], [0, 0, 6], [0, 0, 15]]))  # 5
