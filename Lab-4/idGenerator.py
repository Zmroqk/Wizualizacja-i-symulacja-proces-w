class IdGenerator():
   id = 0
   @staticmethod
   def generateId():
      IdGenerator.id = IdGenerator.id + 1
      return IdGenerator.id