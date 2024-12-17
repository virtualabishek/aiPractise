class FamilyMember:
    def __init__(self, name, relation):
        self.name = name
        self.relation = relation
def display_family(family):
    print("Family Members and Their Relationships:")
    for member in family:
        print(f"{member.relation}: {member.name}")
if __name__ == "__main__":
    # Defining family members
    family = [
        FamilyMember("Ram", "Father"),
        FamilyMember("Usha", "Mother"),
        FamilyMember("Rita", "Daughter"),
        FamilyMember("Abi", "Son"),
        FamilyMember("Sita", "Grandmother"),
        FamilyMember("Deepak", "Grandfather")
    ]
    
    # Display family members
    display_family(family)

