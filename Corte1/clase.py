class Square:
   def __init__(self,val):
      self.val=val
   def getVal(self):
      return self.val*self.val
 
class Calculadora:
   def add(self, a, b):
      return a + b
   def sub(self, a, b):
      return a - b
   def mul (self, a, b):
      return a * b
   def div (self, a, b):
      if b != 0:
         return a / b
      else:
         return "Error: La division es 0"
   