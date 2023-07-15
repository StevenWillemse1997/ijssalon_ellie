from algemene_functies import mijn_functie_2

smaak1 = "aardbei"
prijs1 = 4
korting1 = 0.1 * prijs1


def aanbieding(smaak=smaak1, prijs=prijs1, korting=korting1):
    prijs2 = prijs - korting
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak van {smaak}, van {prijs} euro voor {prijs2} euro."

print(aanbieding())


btw = 0.09
inkomsten = [220,430,125,160,205,90,345]
def inkomsten_totaal(inkomsten,btw):  
    opsom = sum(inkomsten)
    return f"Het totaal van alle inkomsten deze week is {opsom} euro, waarover {opsom*btw} euro btw betaald dient te worden."
    
totaal = inkomsten_totaal(inkomsten,btw)
print(totaal)


mijn_lijst = [220,430,125,160,205,90,345]
def laag_en_hoog(mijn_lijst):
    return f"De laagste opbrengst is: {min(mijn_lijst)} euro, en de hoogste opbrengst is: {max(mijn_lijst)} euro."

l_en_h = laag_en_hoog(mijn_lijst)
print(l_en_h)


def gemiddelde(mijn_lijst):
    opsom = sum(mijn_lijst) / 7
    return f"De gemiddelde inkomsten deze week zijn {opsom} euro."

berkening = gemiddelde(mijn_lijst)
print(berkening)

invoerlijst = [10,5,3,2,1,2,9]  
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

meervoudig_inv = laag_en_hoog(invoerlijst)
print(meervoudig_inv)


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
