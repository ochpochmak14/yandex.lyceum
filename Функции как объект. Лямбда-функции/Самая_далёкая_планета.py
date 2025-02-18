def find_farthest_orbit(orbits):
    valid_orbits = [orbit for orbit in orbits if orbit[0] != orbit[1]]
    areas = list(map(lambda o: o[0] * o[1] * 3.14, valid_orbits))
    return valid_orbits[areas.index(max(areas))]

