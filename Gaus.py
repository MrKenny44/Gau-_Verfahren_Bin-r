class Vektor:
    def __init__(self, values):
        self.values = values

    def __gt__(self, other):
        for i in range(len(self.values)):
            if self.values[i] > other.values[i]:
                return True
            elif self.values[i] < other.values[i]:
                return False
        return False

    def __lt__(self, other):
        for i in range(len(self.values)):
            if self.values[i] < other.values[i]:
                return True
            elif self.values[i] > other.values[i]:
                return False
        return False
    
    def printValues(self):
        print(self.values)

    def addValue(self, value):
        self.values.append(value)

    def xorValues(self, other):
        result = []
        for bit_self, bit_other in zip(self.values, other.values):
            result.append((bit_self + bit_other)%2)
        self.values = result
    
class Matrix:
    def __init__(self, vektors):
        self.vektors = vektors

    def printVektors(self):
        for x in self.vektors:
            x.printValues()

    def addVektor(self, vektor):
        self.vektors.append(vektor)

    def getRelevantRows(self, column):
        result = []        
        for i in range (column, len(self.vektors)):
            vektor = self.vektors[i]
            if vektor.values[column] == 1:
                result.append(vektor)
        return result
    
    def sortVektors(self):
        self.vektors.sort(reverse=True)
        
    def dostuff(self):
        schritt =1
        self.printVektors()
        print("")
        for i in range(0, len(self.vektors[0].values) -1):
            rows = self.getRelevantRows(i)
            for k in range(1, len(rows) ):
                rows[k].xorValues(rows[0])
                print("Schritt: " + str(schritt))
                schritt += 1
                self.printVektors()
                print("")
            self.sortVektors()

vektor1 = Vektor([0,1,1,0,1,0,0])
vektor2 = Vektor([1,1,1,0,0,1,0])
vektor3 = Vektor([1,0,1,0,1,1,1])
vektor4 = Vektor([1,0,1,0,0,1,1])
vektor5 = Vektor([0,0,0,0,1,0,0])
vektor6 = Vektor([0,0,1,0,1,0,1])


matrix1 = Matrix([vektor1, vektor2, vektor3, vektor4, vektor5, vektor6])
matrix1.sortVektors()

matrix1.dostuff()
matrix1.printVektors()