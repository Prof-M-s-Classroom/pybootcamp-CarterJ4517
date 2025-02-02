class CrewMember:

    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience  # Years of experience

    def __str__(self):
        return f"{self.name} - {self.role} ({self.experience} yrs exp)"

class CrewRoster:

    def __init__(self):
        self.crew = []  # List of CrewMember objects

    def add_member(self, name, role, experience):
        """Creates a new crew member and adds to roster."""
        member = CrewMember(name, role, experience)
        self.crew.append(member)


    def remove_member(self, name):
        """Removes a crew member by name."""
        newCrew = [member for member in self.crew if member.name != name]
        self.crew = newCrew


    def list_crew(self):
        """Prints all crew members."""
        crewString = "["
        for member in self.crew:
            crewString = crewString + member.__str__() + ", "
        crewString = crewString[:len(crewString)-2]
        print(crewString + "]")

# === TEST CODE ===

roster=CrewRoster() #Empty Crew roster created

# TODO: Uncomment and implement methods
roster.add_member("Alice", "Engineer", 5)
roster.add_member("Bob", "Pilot", 10)
roster.list_crew()

roster.remove_member("Alice")
roster.list_crew()