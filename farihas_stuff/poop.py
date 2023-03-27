"""
poop poop poop poop poop poop poop poo p
"""

def hourly_wages():
    hours_worked = input("Please enter hours worked: ")
    rate = 15
    try: 
        if int(hours_worked) > 40:
            wages = (float(hours_worked) * float(rate)) * 1.5
            print(wages)
        else:
            wages = (float(hours_worked) * float(rate))
            print(wages)
    except:
        print("ERROR: Please insert a digit.")

def main():
    hourly_wages()


main()