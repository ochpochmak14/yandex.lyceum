def same_by(characteristic, objects):
    if not objects:
        return True
    first_value = characteristic(objects[0])
    return all(characteristic(obj) == first_value for obj in objects)
