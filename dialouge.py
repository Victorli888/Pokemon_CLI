class Profesor():
     def __init__(self, name):
         self.name = name

     def diag_1(self):
         print(f"Ah... hello {self.name}, my name is Professor Oak")
         print(f"There's a vast world to be explored out there with millions of Pokemon to catch")
         print(f"Are you ready to start your adventure?")
     def diag_2(self):
         print("On the table are 3 Pokemon, Please choose wisely... "
               "1st we have WingWa a Grass type"
               "\n2nd we have Totodile a Water type"
               "\n3rd we have Cyndaquill a Fire type")


Profesor.diag_2()
