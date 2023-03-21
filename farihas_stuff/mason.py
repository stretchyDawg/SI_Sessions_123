"""
MASON MASON MASON MASON MASON MASON MASON MASON MASON
"""

def steal_robux(robux_left):
    print("Stole 1 robux. ", robux_left, " robux left.", sep = "")

def main():
    mason = True
    take_masons_robux = False
    while(mason):
        take_masons_robux = True
        masons_roblox_account = range(100, 0, -1)
        for robux in masons_roblox_account:
            steal_robux(robux)
        print("Stole all of masons robux!!!")
        if take_masons_robux == True:
            mason = False

    print()

    delete = input("Would you like to delete MAson's Roblox account?: ")
    if delete == "yes":
        print("Deleted Mason's Roblox account!")
    elif delete == "no":
        print("Did not deleted Mason's Roblox account!")

if __name__ == "__main__":
    main()