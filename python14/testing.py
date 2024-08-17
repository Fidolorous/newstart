class PartyAnimal:

   def __init__(self):
     self.x = "Oliver"

   def party(self) :
     self.x = self.x + " likes"
     print("So far",self.x)

   def party2(self) :
    self.x = self.x + " party mix"
    print("So far",self.x)

    
an = PartyAnimal()
an.party()
print(an)
an.party2()
print(an)