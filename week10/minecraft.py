def create_minecrafter(name, health, inventory, is_dead):
    return (name, health, inventory, is_dead)

def print_inventory(minecrafter):
    inventory = minecrafter[2]
    for value in inventory:
        print(value)

def add_item(minecrafter, item):
    minecrafter[3].append(item)

def clear_inventory(minecrafter):
    inventory = minecrafter[2]
    while(len(inventory) != 0):
        inventory.pop()

def kill(minecrafter):
    return (minecrafter[0], 0, [], True)

def damage(minecrafter, damage):
    health_left = minecrafter[1] - damage
    if health_left <= 0:
        return kill(minecrafter)
    return (minecrafter[0], health_left, minecrafter[2], True)

def print_minecrafter(minecrafter):
    if minecrafter[3] == True:
        print(minecrafter[0], ": DEAD", sep = "")
    else:
        print(minecrafter[0], ": ALIVE", sep = "")
        print("Health:", minecrafter[1])
        print("Inventory:", minecrafter[2])

def main():
    name = "Christian"
    health = 10
    inventory = ["rose", 3, True]
    is_dead = False
    me = create_minecrafter(name, health, inventory, is_dead)
    print_minecrafter(me)

main()