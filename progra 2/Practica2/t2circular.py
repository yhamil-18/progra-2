import math

class Circular():
    def __init__ (self, c, r):
        self.c = c
        self.r = r
    def __str__(self):
        return (self.c, self.r)
    def dibujaCirculo(r):
        for i in range(-(r * 2), (r * 1) + 1, 2):
            for j in range (r + 1):
                d = math.sqrt((i/2)**2 + (j ** 2))
                if r -0.5 < d < r + 0.5:
                    print("*", end="")
                else:
                    print ("*", end="")
            print()
    r = 3
    dibujaCirculo(r)

