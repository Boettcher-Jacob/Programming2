class Shape:
  # Constructor: set up class data
  def __int__(self, length, width):
    self.length = length
    self.width = width
    self.area = 0
    self.perim = 0


  #Mutator: Modifies class data
  def calculate(self):
    self.area = self.length * self.width
    self.perim = 2 * self.length + 2 * self.width


  #Accessors: return class Data
  def getArea(self):
    return self.area

  def getPerimeter(self):
    return self.perim
    