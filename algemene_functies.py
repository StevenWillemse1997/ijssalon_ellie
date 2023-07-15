def mijn_functie_1(a=2,b=4,c=10,d=12):
    return a*a,b*b,c*c,d*d

berekening1 = mijn_functie_1()
print(berekening1)

def mijn_functie_2(a=12,b=3,c=2,d=10,e=5,f=100,g=20):
    print(a + b, a - b, a * b, a / b)
    print(a + c, a - c, a * c, a / c)
    print(d + e, d - e, d * e, d / e)
    print(f + g, f - g, f * g, f / g)

berekening2 = mijn_functie_2()
print(berekening2)           
           
