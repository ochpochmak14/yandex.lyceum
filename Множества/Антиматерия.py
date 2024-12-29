current_items = set()
repeated = set()

local_items = set()

while True:
    item = input()
    if item == "":
        break
    if item == "-1":
        for local_item in local_items:
            current_items.add(local_item)
        local_items = set()
        continue
    if item in current_items:
        repeated.add(item)
    local_items.add(item)
print(*current_items.difference(repeated))