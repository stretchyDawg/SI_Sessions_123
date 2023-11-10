"""
Council Class in Python
@ChristianMorgado
"""
#Administrator Class
class Administrator:
    """
    Administrator (or 'admin): Made up of said admin's name, region, departments, and languages, additionally if they're a chief or not. 
    """
    __slots__ = ["name", "region", "departments", "languages", "chief"]

    def __init__(self, name, region, chief=False):
        self.name = name
        self.region = region
        self.departments = set()
        self.languages = set()
        self.chief = chief

def add_departments(admin, department):
    """
    Adds a given department to a given admin's department set. 
    """
    admin.departments.add(department)

def add_languages(admin, language):
    """
    Adds a given language to a given admin's language set. 
    """
    admin.languages.add(language)

def admin_biography(admin):
    """
    Gives a biography of a given admin.
    """
    print(admin.name)
    print("Region:", admin.region)
    print("Departments:")
    if len(admin.departments) == 0:
        print("\tNone")
    else:
        for dep in admin.departments:
            print("\t", dep, sep = "")
    print("Languages:")
    if len(admin.languages) == 0:
        print("\tNone")
    else:
        for leng in admin.languages:
            print("\t", leng, sep = "")

#----------------------------------------------------------------------------------------------------------------------------
#Council Class
class Council:
    """
    Council Class - Made up of a chief admin and a data structure of admins. 
    """
    __slots__ = ["chief_admin", "admins"]

    def __init__(self, admins):
        self.chief_admin = admins["CHIEF"]
            
        admins.pop("CHIEF")   # THE CHIEF IS NOT APART OF THE ADMIN DATA STRUCTURE
        if len(admins) >= 3:
            self.admins = admins
        else:
            raise RuntimeError("Not enough admins.")

def chief_admin_bio(council):
    """
    Prints the biography of the chief admin of a given council
    """
    admin_biography(council.chief_admin)

def admin_bio(council, admin_name):
    """
    Prints the biography of a given admin's name in a given council. 
    """
    if admin_name in council.admins:
        admin_biography(council.admins[admin_name])
    else:
        print("Could not find an admin with that name.")

def display_council(council):
    """
    Displays a given council and their admin's names.
    """
    print("[Chief]", council.chief_admin.name)
    for admin_key in council.admins:
        print(council.admins[admin_key].name)

def display_council_biographies(council):
    """
    Displays a given council and their admin's biographies.
    """
    print("Chief Administrator:")
    admin_biography(council.chief_admin)
    print("\n")
    for admin_key in council.admins:
        admin_biography(council.admins[admin_key])
        print("\n")

#--------------------------------------------------------------------------------------------------
# Input Functions

def make_admin_group():
    """
    Makes a dictionary of admin names as keys and admins as values through user input.
    """
    admin_group = dict()
    admins = int(input("How many admins will be in this group? Must have 4 (1 chief and 3 regular) admins for a council: "))
    chief_found = False
    count = 0
    while count < admins:
        chief_already_found = False
        if chief_found == True:
            chief_already_found = True
        print()

        #Name, region, chief
        name = input("What is the name of this admin?: ")
        region = input("What region are they from?: ")
        if chief_found == False:
            chief = input("Are they the chief admin? (y/n): ")
            if chief == 'y':
                new_admin = Administrator(name, region, True)
                chief_found = True
            elif count == (admins - 1):
                print("This admin must and will be a chief admin, as no chief admin has been made before, and this is the last admin.")
                new_admin = Administrator(name, region, True)
                chief_found = True     
        else:
            new_admin = Administrator(name, region)

        #Departments, Languages
        departments = input("What departments are they in? ('n' for none): ")
        if departments != 'n':
            split_departments = departments.split(", ")
            for dep in split_departments:
                add_departments(new_admin, dep)
        languages = input("What languages do they speak? ('n' for none): ")
        if languages != 'n':
            split_languages = languages.split(", ")
            for lang in split_languages:
                add_languages(new_admin, lang)

        #Creates dictionary of admins
        if new_admin.name in admin_group:
            print("ADMIN NOT VIABLE: Admin of that key has already been added.")
            if chief_already_found == False:
                chief_found = False
                print("Chief admin still open.")
            continue
        else:
            if new_admin.chief == True:
                admin_group["CHIEF"] = new_admin
                count += 1
                continue
            else:
                admin_group[new_admin.name] = new_admin
                count += 1
                continue
    return admin_group




def main():
    # Original testing administrators I used:
    # irwin = Administrator("Irwin Cano", "Los Angeles")
    # ashton = Administrator("Ashton Michelstein", "Santa Clarita")
    # tyler = Administrator("Tyler \'Temmy\' Emerson", "Honey Falls")
    # christian = Administrator("Christian Morgado", "New York City", True)

    admin_dict = make_admin_group()
    for key in admin_dict:
        print(key, ":", admin_dict[key])
    print("\nMaking council...")
    council = Council(admin_dict)
    print("Council made!")
    while True:
        user_input = input("What would you like to do with this council? (i) for help: ")
        user_input = user_input.lower()
        if user_input == 'i':
            print("\nCommands:")
            print("\'Display Chief Admin Biography\' to print the biography of the chief admin.")
            print("\'Display Admin Biography\' to print the biography of an admin given their name.")
            print("\'Display Council\' to display council members.")
            print("\'Display Council Biographies\' to display council biographies.")
            print("\'exit\' to exit.\n")
        elif user_input == 'exit':
            break
        elif user_input == 'display chief admin biography':
            print()
            chief_admin_bio(council) #chief_admin_bio() and admin_biography() are being tested
            print()
        elif user_input == 'display admin biography':
            admin_name = input("Enter an admin name (that is not the chief admin's name): ")
            print()
            admin_bio(council, admin_name) # admin_bio() and admin_biography() are being tested here.
            print()
        elif user_input == 'display council':
            print()
            display_council(council) # display_council() is being tested here
            print()
        elif user_input == 'display council biographies':
            print()
            display_council_biographies(council) # display_council_biographies() and admin_biography() is being tested here
            print()
        else:
            print("Error: Command not found.")













    

if __name__ == "__main__":
    main()