class Dog:
  def __init__(self, name):
    self.name = name

  def dog_name(self):
    return self.name

Milo = Dog('Milo')
print(Milo.dog_name())