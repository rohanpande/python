class Student(object):
    """
    Returns a ```Student``` object with the given name, branch and year.

    """

    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year
        print(" A student object was created.")

    def print_details(self):
        """
        Prints the details of the student. 

        """
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)

try:
    std1 = Student();
except TypeError:
    print("A Type error has occurred")

std2 = Student("Rohan Pande", "Computers", "2001")
std2.print_details()


