fajl = "hivas.txt"
Hivasok = []
fejlec = ('o1', 'p1', 's1', 'o2', 'p2','s2')
with open(fajl)as BE:
    for sor in BE:
        sor = sor.strip()
        if not sor: continue
        sor = map(int,sor.split())
        Hivasok.append({f: e for f, e in zip(fejlec, sor)})

def mpbe(óra:int, perc: int, másodperc:int)-> int:
    return óra * 60 * 60 + perc * 60 + másodperc

Statisztika = {}
""" for h in Hivasok:
    if h['o1'] not in Statisztika.keys():
        Statisztika[h['o1']] = 1
    else:
        Statisztika[h['o1']] += 1 """
for h in Hivasok:
    Statisztika[h['o1']] = Statisztika.get(h['o1'], 0) + 1
print("3. feladat")
for o, e in Statisztika.items():
    print(f"{o} óra {e} hívás ")

print("\n4. feladat")
maxT, maxINDX = 0, None
for i, h in enumerate(Hivasok, 1):
    deltaT = mpbe(h["o2"], h["p2"], h["s2"]) - mpbe(h["o1"], h["p1"], h["s1"])
    if deltaT > maxT:
        maxT = deltaT
        maxINDX = i
print(f"A leghosszabb ideig vonalban levo hivo {maxINDX}. sorban szerepel, a hivas hossza: {maxT} masodperc.")

print("\n5. feladat")
O,P,M = map(int, input("Adjon meg egy időpontot! (ora perc masodperc) ").split())
KeresettIdő = mpbe(O,P,M)
beszélő = None
várakozók = 0
for i,h in enumerate(Hivasok,1):
    if mpbe(h["o2"], h["p2"], h["s2"]) >= KeresettIdő >= mpbe(h["o1"], h["p1"], h["s1"]):
        if not beszélő:
            beszélő = i
        else:
            várakozók += 1

        
if beszélő:
    print(f"A várakozok száma: {várakozók} a beszélő a {beszélő}. hivó.")
else:
    print("Nem volt beszélő")

def sikeres(INDX: int)-> bool:
    h = Hivasok[INDX]
    T1 = mpbe(h["o1"], h["p1"], h["s1"]) 
    T2 = mpbe(h["o2"], h["p2"], h["s2"]) 
    TMAX = max(mpbe(k["o2"], k["p2"], k["s2"]) for k in Hivasok[:INDX]) if INDX > 0 else 0
    return T2 >= 8 * 60 * 60 and T1 <= 12 * 60 * 60 and T2 > TMAX
utolso, elozo = None, None
for i in range(len(Hivasok)):
    if sikeres(i):
        elozo = utolso 
        utolso = i


várakozásiIdő = mpbe(Hivasok[elozo]["o2"], Hivasok[elozo]["p2"], Hivasok[elozo]["s2"])-mpbe(Hivasok[utolso]["o1"], Hivasok[utolso]["p1"], Hivasok[utolso]["s1"])

print(f"Az utolso telefonalo adatai a(z) {utolso + 1}. sorban vannak, {várakozásiIdő} masodpercig vart.")

Sikeresek = [i for i in range(len(Hivasok)) if sikeres(i)]

print(Sikeresek)

        
