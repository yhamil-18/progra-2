import math
class Linea():
    def __init__(self, p1, p2):
        self.p1=p1
        self.p2=p2
    def __str__(self):
        return f"Linea desde {self.p1} hasta {self.p2}"
    
    def dibujarLinea(n):
        for i in range(n):
            print("*", end="")
    dibujarLinea(6)
    
Linea = (6, 1)
print(Linea)