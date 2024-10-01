class Student:
  def __init__(self, name, year, id):
    self.name = name
    self.year = year
    self.id = id

  def __str__(self):
    return f"name = {self.name} year = {self.year} id = {self.id}"

ofer = Student("Ofer", 1964, "222131455")
shay = Student("Shay", 2000, "207635616")
print(ofer)
print(shay)