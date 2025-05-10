#   - OOP Concepts, Encapsulation
class Presentation:
    def __init__(self, presenter, topic, date, time):
        self.__presenter = presenter  # encapsulation
        self.__topic = topic
        self.__date = date
        self.__time = time

    def show_info(self):
        print(f" {self.__presenter} |  {self.__topic} |  {self.__date} |  {self.__time}")

    #  Method Overloading (Manually done since Python doesn't support it natively)
    def update_info(self, topic=None, date=None, time=None):
        if topic:
            self.__topic = topic
        if date:
            self.__date = date
        if time:
            self.__time = time

    #  Operator Overloading
    def __eq__(self, other):
        return self.__presenter == other.__presenter

#  - Lambda Function
sort_by_name = lambda presentations: sorted(presentations, key=lambda x: x._Presentation__presenter)

#  Recursive Function (Counting Presentations Recursively)
def count_presentations(lst):
    if not lst:
        return 0
    return 1 + count_presentations(lst[1:])

#   - Assignment, Identity, Logical, Membership
p1 = Presentation("Pashupati", "Encapsulation", "2025-05-10", "10:00 AM")
p2 = Presentation("Aarati", "OOP", "2025-05-11", "11:00 AM")
p3 = Presentation("Sita", "Operators", "2025-05-12", "12:00 PM")

presentations = [p1, p2, p3]

# Identity Operator
print(" Is p1 same as p2?", p1 is p2)

# Logical Operator
if p1 != p2 and p3 in presentations:
    print(" p3 is in the list and p1 is not equal to p2")

# Membership Operator
if "Encapsulation" in p1._Presentation__topic:
    print(" 'Encapsulation' is part of the topic!")

# Show All Presentations
print("\n All Presentations:")
for p in sort_by_name(presentations):
    p.show_info()

# Count Presentations
print(f"\n Total Presentations: {count_presentations(presentations)}")
