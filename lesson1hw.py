class Fraction:
    def __init__(self, ch, zn):
        self.ch = ch
        self.zn = zn

    def add(self,other):
        ch = self.ch * other.zn + self.zn * other.ch
        zn = self.zn * other.zn
        print(ch)
        print('-')
        print(zn)

    def sub(self, other):
        ch = self.ch * other.zn - self.zn * other.ch
        zn = self.zn * other.zn
        print(ch)
        print('-')
        print(zn)

    def mult(self,other):
        ch = self.ch * other.ch
        zn = self.zn * other.zn
        print(ch)
        print('-')
        print(zn)

    def div(self,other):
        ch = self.ch * other.zn
        zn = self.zn * other.ch
        print(ch)
        print('-')
        print(zn)


f1 = Fraction(5, 3)
f2 = Fraction(1, 2)
print(f1.ch)
print('-')
print(f1.zn)
print()
print(f2.ch)
print('-')
print(f2.zn)
print()
print('---plus---')
f1.add(f2)
print('---minus---')
f1.sub(f2)
print('---umnojenie---')
f1.mult(f2)
print('---delenie---')
f1.div(f2)