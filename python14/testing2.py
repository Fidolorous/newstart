class PartyAnimal:

   def __init__(self, nam):
     self.x = 0
     self.name = nam
     print(self.name,'constructed')

   def party(self) :
     self.x = self.x + 1
     print(self.name,'party count',self.x)

s = PartyAnimal('Oliver')
j = PartyAnimal('Gehy')
y = PartyAnimal('Test')
h = PartyAnimal('Macska')

s.party()
j.party()
y.party()
h.party()
h.party()

