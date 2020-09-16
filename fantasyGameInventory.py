# Write your code here :-)
#Rule keys are string values describe item
#value is integer of how many

import pprint

inventory = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
dragonLoot = ['gold coin','rope','gold coin','dagger','dagger','arrow','ruby']

def displayInventory(inventory):
    total = 0
    print("Inventory:")
    for k,v in inventory.items():
        print(str(v) + " "+k)
        total = v + total
    print("Total number of items: " + str(total))

def addLootToInventory(inventory,loots):
    for x in range(len(loots)):
        loot = loots[x]
        inventory.setdefault(loot,0)
        inventory[loot] = inventory[loot] + 1
    return inventory

displayInventory(inventory);
inventory = addLootToInventory(inventory,dragonLoot)
displayInventory(inventory)
