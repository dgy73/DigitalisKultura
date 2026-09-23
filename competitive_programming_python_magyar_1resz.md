# Versenyprogramozás Pythonban -- magyar fordítás

> **Forrás:** Christoph Dürr -- Jill-Jênn Vie: *Competitive Programming
> in Python*\
> **Fordított rész:** 1.2.1--1.3.2 (a rendelkezésre bocsátott 12 oldalas
> részlet)
>
> Ez a fájl a feltöltött részlet magyar fordítása. A Python-kódok és az
> azonosítók az eredeti formájukban maradtak.

## 1.2 Python néhány szóban

### 1.2.1 Alapvető adattípusok

Pythonban lényegében négy alapvető adattípus létezik: a logikai értékek
(`bool`), az egész számok (`int`), a lebegőpontos számok (`float`) és a
karakterláncok (`str`).

A legtöbb más programozási nyelvvel ellentétben az egész számok mérete
nincs rögzített bitszámra -- tipikusan 64 bitre -- korlátozva, hanem
tetszőleges pontosságú ábrázolást használnak.

A függvények -- pontosabban konstruktorok -- `bool`, `int`, `float` és
`str` segítségével egy objektum a megfelelő alapvető típusra alakítható.

Ha például egy tízes számrendszerben megadott egész szám számjegyeihez
szeretnénk hozzáférni, először karakterlánccá alakíthatjuk, majd
elérhetjük a karakterlánc egyes karaktereit. A C-hez hasonló nyelvekkel
ellentétben azonban egy karakterlánc valamely karakterét nem lehet
közvetlenül módosítani, mert a karakterláncok megváltoztathatatlanok
(*immutable*). Ehhez először a karaktereket tartalmazó listává kell
alakítani.

### Adatszerkezetek

A legfontosabb összetett adatszerkezetek:

-   szótárak (`dict`),
-   halmazok (`set`),
-   listák (`list`),
-   n-esek, azaz tuple-ök (`tuple`).

Ezeket az adatszerkezeteket konténereknek nevezzük, mivel több
objektumot tartalmaznak valamilyen strukturált formában.

A `dict`, `set`, `list` és `tuple` függvények segítségével egy objektum
a megfelelő adatszerkezetté alakítható.

Egy `s` karakterlánc esetén például

``` python
list(s)
```

egy olyan `L` listát ad vissza, amely a karakterlánc karaktereit
tartalmazza. Ezután a lista egyes elemei módosíthatók, majd az elemekből
ismét karakterlánc készíthető:

``` python
''.join(L)
```

Az üres karakterlánc helyett elválasztó karakterláncot is használhatunk.
Például:

``` python
'-'.join(['A', 'B', 'C'])
```

eredménye:

``` text
A-B-C
```

### Listák, n-esek és szótárak kezelése

Fontos megjegyezni, hogy a Python listái nem láncolt listák, amelyekben
minden elem a következő elemre mutató hivatkozást tartalmaz. A listák
ehelyett tömbszerű adatszerkezetek, amelyek elemei index alapján érhetők
el és módosíthatók.

Egy listát szögletes zárójelek között, vesszővel elválasztott elemekkel
adunk meg:

``` python
[1, 2, 3]
```

#### Listák

A lista indexelése `0`-tól kezdődik. Az utolsó elem `-1`, az utolsó
előtti `-2` indexszel is elérhető, és így tovább.

A lista elemeinek vagy részlistáinak kiválasztását *szeletelésnek*
(*slicing*) nevezzük. Ugyanez a mechanizmus karakterláncok esetén is
használható.

  -----------------------------------------------------------------------
  Kifejezés                           Jelentés
  ----------------------------------- -----------------------------------
  `L[i]`                              az `L` lista `i` indexű eleme

  `L[i:j]`                            az `i` indextől a `j` indexig tartó
                                      elemek, a `j` indexű elem nélkül

  `L[:j]`                             az első `j` elem

  `L[i:]`                             az `i` indexű elemtől kezdődő
                                      összes elem

  `L[-3:]`                            az utolsó három elem

  `L[i:j:k]`                          az `i` indextől a `j` indexig,
                                      minden `k`-adik elem

  `L[::2]`                            a páros indexű elemek

  `L[::-1]`                           a lista fordított sorrendű másolata
  -----------------------------------------------------------------------

A fenti kifejezések futási ideje a lista hosszával lineárisan arányos,
kivéve az elsőt (`L[i]`), amely konstans idejű.

A legfontosabb listaműveletek, ahol `n` az `L` lista hossza:

  -----------------------------------------------------------------------
  Művelet                 Jelentés                Időigény
  ----------------------- ----------------------- -----------------------
  `len(L)`                az elemek száma         `O(1)`

  `sorted(L)`             rendezett másolatot ad  `O(n log n)`
                          vissza                  

  `L.sort()`              helyben rendezi a       `O(n log n)`
                          listát                  

  `L.count(c)`            megadja `c`             `O(n)`
                          előfordulásainak számát 

  `c in L`                eldönti, hogy `c`       `O(n)`
                          szerepel-e a listában   

  `L.append(c)`           `c` hozzáfűzése a lista amortizált `O(1)`
                          végéhez                 

  `L.pop()`               az utolsó elem          amortizált `O(1)`
                          eltávolítása és         
                          visszaadása             
  -----------------------------------------------------------------------

Egy függvény amortizált konstans időigényű, ha több egymást követő hívás
esetén az átlagos időigény konstans, még akkor is, ha egy-egy konkrét
hívás `n`-nel arányos időt igényel.

A lista tehát rendelkezik a verem (*stack*) minden szükséges
műveletével.

#### n-es (`tuple`)

Az n-es a listához hasonlóan viselkedik, de leírásához zárójeleket
használunk:

``` python
(1, 2)
(left, 'X', right)
```

Az egyetlen elemet tartalmazó 1-esnél szükség van a vesszőre:

``` python
(2,)
```

Az üres, 0 elemű n-es megadható így:

``` python
()
```

vagy:

``` python
tuple()
```

A listákkal szemben az n-esek -- a karakterláncokhoz hasonlóan --
megváltoztathatatlanok. Emiatt egy n-es használható szótárkulcsként.

#### Szótárak

A szótárak objektumokat rendelnek értékekhez. Például egy szöveg
szavaihoz hozzárendelhetjük azok előfordulási gyakoriságát.

A szótár kapcsos zárójelek között, vesszővel elválasztott `kulcs:érték`
párokból áll:

``` python
{'the': 4, 'bread': 1, 'is': 6}
```

Az üres szótár:

``` python
{}
```

Annak vizsgálata, hogy az `x` kulcs megtalálható-e a `dic` szótárban:

``` python
x in dic
```

A szótár mögött hash-tábla áll, ezért a következő műveletek a
gyakorlatban konstans idejűek:

``` python
x in dic
dic[x]
dic[x] = 42
```

Legrosszabb esetben ugyan lineáris időigényűek lehetnek, ez azonban
olyan valószínűtlen esetben fordul elő, amikor minden kulcs ugyanazzal a
hash-értékkel rendelkezik.

Ha egy szótár kulcsai pontosan a `0` és `n - 1` közötti egész számok,
akkor lista használata lényegesen hatékonyabb.

### Ciklusok és bejárás

Pythonban ciklust a `for` vagy a `while` kulcsszóval írhatunk.

A `for` ciklus általános alakja:

``` python
for x in S:
```

Az `x` változó egymás után felveszi az `S` konténer elemeinek értékét.
Szótár esetén a ciklus alapértelmezés szerint a kulcsokat járja be.

A

``` python
while L:
```

ciklus addig fut, amíg az `L` lista nem üres. Itt a lista implicit módon
logikai értékké alakul; az üres lista `False`, a nem üres lista `True`.

Gyakran egyszerre van szükségünk egy lista elemeire és azok indexére. Ez
megoldható így:

``` python
for index in range(len(L)):
    value = L[index]
    # ... az index és az érték feldolgozása
```

Az `enumerate` segítségével ugyanez tömörebben írható:

``` python
for index, value in enumerate(L):
    # ... az index és az érték feldolgozása
```

Szótár esetén a kulcsokon és értékeken egyszerre iterálhatunk:

``` python
for key, value in dic.items():
    # ... a kulcs és az érték feldolgozása
```

## 1.2.2 Sajátosságok: lista- és szótárkifejezések, iterátorok

### Lista- és szótárkifejezések

A Python olyan szintaxist biztosít, amely bizonyos objektumok esetén
közel áll a matematikai jelöléshez.

A `0`-tól `n²`-ig terjedő négyzetszámok listája például
listakifejezéssel (*list comprehension*) készíthető:

``` python
>>> n = 5
>>> squared_numbers = [x ** 2 for x in range(n + 1)]
>>> squared_numbers
[0, 1, 4, 9, 16, 25]
```

Ez matematikailag a következő halmaznak felel meg:

``` text
{x² | x = 0, ..., n}
```

A módszer különösen hasznos egy `n` hosszúságú lista inicializálására:

``` python
>>> t = [0 for _ in range(n)]
>>> t
[0, 0, 0, 0, 0]
```

Hasonlóan inicializálhatunk számlálókat egy karakterlánc betűihez:

``` python
>>> my_string = "cowboy bebop"
>>> nb_occurrences = {letter: 0 for letter in my_string}
>>> nb_occurrences
{'c': 0, 'o': 0, 'w': 0, 'b': 0, 'y': 0, ' ': 0, 'e': 0, 'p': 0}
```

A második sor egy szótárkifejezés (*dictionary comprehension*), amely
egyenértékű a következővel:

``` python
nb_occurrences = {}
for letter in my_string:
    nb_occurrences[letter] = 0
```

### `range` és más iterátorok

Egész számtartományok bejárásához használható:

``` python
for i in range(n):
```

Ez a `0, 1, ..., n - 1` értékeket járja be.

Néhány változat:

  Kifejezés                Bejárt értékek
  ------------------------ ----------------------------------------
  `range(k, n)`            `k`-tól `n - 1`-ig
  `range(k, n, 2)`         `k`-tól `n - 1`-ig kettesével
  `range(n - 1, -1, -1)`   `n - 1`-től `0`-ig csökkenő sorrendben

A Python korai verzióiban a `range` listát adott vissza. A mai Pythonban
hatékonysági okokból iterálható objektumot ad, amely az egész számokat
szükség szerint, egyenként szolgáltatja a `for` ciklus számára.

Egy függvény generátorként is működhet, ha végrehajtása különböző
pontjain a `yield` kulcsszóval ad vissza elemeket.

A következő függvény például egy lista elemeinek összes párján
végigiterál:

``` python
def all_pairs(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            yield (L[i], L[j])
```

## 1.2.3 Hasznos modulok és csomagok

### Modulok

Bizonyos Python-objektumokat modulból vagy csomagból kell importálni az
`import` utasítással. A csomag modulok gyűjteménye.

Két gyakori importálási mód:

``` python
>>> from math import sqrt
>>> sqrt(4)
2
```

vagy:

``` python
>>> import math
>>> math.sqrt(4)
2
```

A második forma segít elkerülni a különböző modulok azonos nevű
függvényei közötti névütközést.

### `math`

A `math` modul matematikai függvényeket és konstansokat tartalmaz,
például:

``` python
log
sqrt
pi
```

A Python egész számai tetszőleges pontosságúak, ezért nincs méretbeli
korlátjuk. Emiatt egész számként nincs külön `-∞` vagy `+∞` érték.

Lebegőpontos számoknál használható:

``` python
float('-inf')
float('inf')
```

Python 3.5-től:

``` python
math.inf
```

illetve:

``` python
from math import inf
```

egyenértékű a `float('inf')` értékkel.

### `fractions`

A modul a `Fraction` osztályt biztosítja, amely lehetővé teszi törtekkel
végzett számítások elvégzését a lebegőpontos számításokra jellemző
pontosságvesztés nélkül.

Ha `f` egy `Fraction` példány, akkor például:

``` python
str(f)
```

egy `"3/2"` alakú karakterláncot adhat vissza, amely az értéket
egyszerűsített tört alakban írja le.

### `bisect`

Bináris -- más néven dichotomikus -- keresési függvényeket biztosít
rendezett listákhoz.

### `heapq`

Olyan függvényeket biztosít, amelyek segítségével egy lista kupacként
(*heap*) kezelhető. Egy elem hozzáadása vagy a legkisebb elem
eltávolítása a kupac méretének logaritmusával arányos idő alatt
végezhető el.

### `string`

A modul karakterláncokkal kapcsolatos segédeszközöket biztosít.

Maguk a karakterláncok is számos hasznos metódussal rendelkeznek.
Például:

-   `strip()` -- eltávolítja a karakterlánc elejéről és végéről a szóköz
    jellegű karaktereket;
-   `lower()` -- kisbetűssé alakítja a karaktereket;
-   `split()` -- részekre bontja a karakterláncot szóköz vagy más
    megadott elválasztó mentén.

Például:

``` python
"12/OCT/2018".split("/")
```

eredménye:

``` python
["12", "OCT", "2018"]
```

### Csomagok

A Python egyik erőssége a rendelkezésre álló csomagok nagy száma. Egy
részük a szabványos Python-telepítés része, másokat például a `pip`
segítségével kell telepíteni.

#### `tryalgo`

A könyvben szereplő kódok a `tryalgo` csomagban érhetők el:

``` bash
pip install tryalgo
```

Használata:

``` python
>>> import tryalgo
>>> help(tryalgo)          # a modulok listája
>>> help(tryalgo.arithm)   # egy adott modul dokumentációja
```

#### `collections.Counter`

A `collections` modul `Counter` osztálya kényelmes számláló
adatszerkezet.

Egy hagyományos szótárnál:

``` python
>>> c = {}
>>> c['a'] += 1
Traceback (most recent call last):
    ...
KeyError: 'a'
```

A kulcsot előbb létre kell hozni:

``` python
>>> c['a'] = 1
>>> c['a'] += 1
>>> c
{'a': 2}
```

`Counter` használatával:

``` python
>>> from collections import Counter
>>> c = Counter()
>>> c['a'] += 1
>>> c
Counter({'a': 1})
```

A nem létező kulcshoz automatikusan `0` értéket feltételez, és
módosításkor létrehozza a bejegyzést.

Karakterek gyakoriságának megszámlálása:

``` python
>>> c = Counter('cowboy bebop')
>>> c
Counter({'o': 3, 'b': 3, 'c': 1, 'w': 1, 'y': 1, ' ': 1, 'e': 1, 'p': 1})
```

#### `collections.deque`

A `collections` modul a `deque` osztályt is biztosítja, amely kétvégű
sor (*double-ended queue*).

Ezzel az adatszerkezettel a sor bal és jobb oldalán egyaránt hatékonyan
adhatunk hozzá vagy távolíthatunk el elemeket.

Ez többek között a Dijkstra-algoritmus olyan változatának
megvalósításában használható, ahol az élek súlya csak `0` vagy `1`.

#### `collections.defaultdict`

A `defaultdict` olyan szótár, amely alapértelmezett értéket rendel a még
nem létező kulcsokhoz. Bizonyos értelemben a `Counter` általánosítása.

``` python
>>> from collections import defaultdict
>>> g = defaultdict(list)
>>> g['paris'].append('marseille')
>>> g['paris'].append('lyon')
>>> g
defaultdict(<class 'list'>, {'paris': ['marseille', 'lyon']})
>>> g['paris']
['marseille', 'lyon']
```

A `'paris'` kulcs szükség esetén automatikusan létrejön.

#### `numpy`

A `numpy` általános numerikus számítási eszközöket biztosít, különösen
nagy mátrixok kezelésére.

Például:

``` python
numpy.linalg.solve
```

lineáris egyenletrendszert old meg, míg:

``` python
numpy.fft.fft
```

gyors diszkrét Fourier-transzformációt számít.

### PEP 8

A könyv kódjainak írásakor a szerzők a PEP 8 szabványt követték. Ez
részletes ajánlásokat tartalmaz többek között:

-   a szóközök használatára,
-   a változónevek megválasztására,
-   a Python-kód általános formázására.

A kód szerkezetének ellenőrzésére használható például a `pycodestyle`
eszköz.

## 1.2.4 Python, PyPy és PyPy3 értelmezők

A könyv algoritmusai Python 3-ban készültek, miközben a szerzők
igyekeztek megőrizni a Python 2-vel való visszafelé kompatibilitást.

A szövegben szereplő kódokat érintő legfontosabb különbségek a `print`
használatát és az egész számok osztását érintik.

Python 3-ban:

``` python
5 / 2
```

eredménye:

``` text
2.5
```

Python 2-ben ugyanez `2` eredményt adott.

Az egész osztás operátora mindkét verzióban:

``` python
//
```

A `print` Python 2-ben kulcsszó volt, Python 3-ban viszont függvény,
ezért az argumentumokat zárójelek közé kell írni.

A referenciaértelmező a **CPython**, amelynek futtatható állománya
általában:

``` text
python
```

A telepítéstől függően a Python 3 értelmező neve lehet:

``` text
python
```

vagy:

``` text
python3
```

Egy másik, gyakran lényegesen gyorsabb értelmező a **PyPy**. A Python
2-es változat futtatható állománya `pypy`, a Python 3-asé `pypy3`.

A PyPy a Python egy RPython nevű részhalmazára épít. Ennek korlátozásai
lehetővé teszik többek között a változók típusának forráskódelemzés
alapján történő következtetését.

Hátránya, hogy bizonyos modulok nem feltétlenül érhetők el benne.
Programozási versenyen azonban a jobb futási teljesítmény különösen
hasznos lehet szigorú időkorlát esetén.

## 1.2.5 Gyakori hibák

### Másolás

A Python-kezdők egyik gyakori hibája a listák másolásához kapcsolódik.

A következő példában `B` valójában ugyanarra az objektumra hivatkozik,
mint `A`:

``` python
A = [1, 2, 3]
B = A  # Vigyázat! Mindkét változó ugyanarra az objektumra hivatkozik
```

Ezért `B[0]` módosítása `A[0]` értékét is megváltoztatja.

Ha `B`-nek `A` különálló másolatának kell lennie:

``` python
A = [1, 2, 3]
B = A[:]  # B az A különálló másolata
```

A `[:]` jelölés tehát lista másolására használható.

További példák:

``` python
A[1:]     # minden elem az első kivételével
A[:-1]    # minden elem az utolsó kivételével
A[::-1]   # fordított sorrendű másolat
```

Különösen veszélyes a következő mátrixinicializálás:

``` python
M = [[0] * 10] * 10  # Ne írjuk így!
```

Ebben az esetben a mátrix sorai ugyanarra a listára hivatkoznak. Ezért
például `M[0][0]` módosítása az első oszlop több elemére is hatással
lesz.

Egy négyzetes mátrix helyesen inicializálható például így:

``` python
M1 = [[0] * 10 for _ in range(10)]
```

vagy:

``` python
M2 = [[0 for j in range(10)] for i in range(10)]
```

A `numpy` modul egyszerű eszközöket biztosít mátrixok kezelésére, a
könyv azonban szándékosan nem erre épít, hogy a bemutatott kód általános
maradjon, és könnyen átültethető legyen Java vagy C++ nyelvre.

### `range`

Egy másik tipikus hiba a `range` függvény használatához kapcsolódik.

A következő ciklus egy `A` lista `0`--`9` indexű elemeit dolgozza fel
növekvő sorrendben:

``` python
for i in range(0, 10):  # 0 benne van, 10 nincs benne
    process(A[i])
```

Csökkenő sorrendű feldolgozáshoz nem elegendő egyszerűen felcserélni a
két argumentumot.

A

``` python
range(10, 0, -1)
```

a `10` értéket tartalmazza, a `0` értéket azonban már nem.

Ezért a helyes ciklus:

``` python
for i in range(9, -1, -1):  # 9 benne van, -1 nincs benne
    process(A[i])
```

# 1.3 Bemenet és kimenet

## 1.3.1 A szabványos bemenet olvasása

A programozási versenyeken kitűzött feladatok többségénél a bemeneti
adatokat a szabványos bemenetről olvassuk, az eredményeket pedig a
szabványos kimenetre írjuk.

Ha a bemeneti fájl neve `test.in`, a program pedig `prog.py`, akkor a
bemenet a következő paranccsal irányítható a programhoz:

``` bash
python prog.py < test.in
```

Mac OS X alatt terminálablak általában a **Command + Space**, majd a
*Terminal* beírásával nyitható meg.

Windows alatt például:

``` text
Start → Run → cmd
```

Linuxon a terminál vagy parancsindító elérése az asztali környezettől
függ.

Ha a program kimenetét `test.out` fájlba szeretnénk menteni:

``` bash
python prog.py < test.in > test.out
```

Ha a kimenetet egyszerre szeretnénk látni és fájlba is írni:

``` bash
python prog.py < test.in | tee test.out
```

A `tee` parancs Windows alatt alapértelmezés szerint nem feltétlenül
érhető el.

### Soronkénti beolvasás

A bemenet soronként olvasható:

``` python
input()
```

Az `input()` a következő bemeneti sort karakterláncként adja vissza, a
sorvége karakterei nélkül.

A `sys` modul hasonló függvénye:

``` python
sys.stdin.readline()
```

Ez a sorvége karakterét is megtartja. A szerzők tapasztalata szerint
ugyanakkor lényegesen gyorsabb lehet az `input()` függvénynél.

Ha a bemeneti sor egy egész számot tartalmaz:

``` python
n = int(input())
```

Lebegőpontos szám esetén:

``` python
x = float(input())
```

Ha egy sor több, szóközzel elválasztott egész számot tartalmaz, először
a `split()` segítségével részekre bonthatjuk, majd a `map` segítségével
egész számmá alakíthatjuk őket.

Például két egész szám, `height` és `width` beolvasása:

``` python
import sys

height, width = map(int, sys.stdin.readline().split())
```

### Nagy bemenet gyors beolvasása

Ha a bemenet olvasása teljesítményproblémát okoz, gyorsabb lehet a
teljes bemenetet egyetlen rendszerhívással beolvasni.

Ha a bemenet kizárólag egész számokat tartalmaz:

``` python
import os

instance = list(map(int, os.read(0, M).split()))
```

Az `os.read` első paraméterében szereplő `0` a szabványos bemenetet
jelenti.

Az `M` konstansnak a bemeneti fájl méretének felső korlátját kell
megadnia.

Ha például a fájl `10^7` darab, `0` és `10^9` közötti egész számot
tartalmaz, egy szám legfeljebb 10 karakterből áll, és legfeljebb két
sorvége/elválasztó karakterrel számolunk, ezért választható:

``` text
M = 12 · 10^7
```

## Példa -- gráf beolvasása

Tegyük fel, hogy a bemenet:

``` text
3
paris tokyo 9471
paris new-york 5545
new-york singapore 15344
```

Az első sor a gráf éleinek számát adja meg.

Minden él formátuma:

``` text
<indulás> <érkezés> <távolság>
```

A gráf `defaultdict` segítségével a következőképpen építhető fel:

``` python
from collections import defaultdict

nb_edges = int(input())
g = defaultdict(dict)

for _ in range(nb_edges):
    u, v, weight = input().split()
    g[u][v] = int(weight)
    # g[v][u] = int(weight)  # irányítatlan gráf esetén
```

## Példa -- három mátrix beolvasása és az `AB = C` egyenlőség tesztelése

A bemenet első sora egyetlen `n` egész számot tartalmaz. Ezt `3n` sor
követi, amelyek mindegyike `n` darab, szóközzel elválasztott egész
számot tartalmaz.

Ezek három `n × n`-es mátrix -- `A`, `B` és `C` -- sorait írják le.

A cél annak eldöntése, hogy:

``` text
AB = C
```

A közvetlen mátrixszorzás időigénye:

``` text
O(n³)
```

Létezik azonban egy `O(n²)` időigényű valószínűségi megoldás.
Véletlenszerűen választunk egy `x` vektort, majd ellenőrizzük:

``` text
A(Bx) = Cx
```

Ez az 1979-ből származó **Freivalds-teszt**.

Ha a számításokat modulo `d` végezzük, annak valószínűsége, hogy az
algoritmus tévesen egyenlőséget jelez akkor is, amikor `AB ≠ C`,
legfeljebb:

``` text
1 / d
```

A hibavalószínűség a teszt többszöri megismétlésével tetszőlegesen
kicsivé tehető.

A könyvben szereplő megvalósítás:

``` python
from random import randint
from sys import stdin


def readint():
    return int(stdin.readline())


def readarray(typ):
    return list(map(typ, stdin.readline().split()))


def readmatrix(n):
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M


def mult(M, v):
    n = len(M)
    return [
        sum(M[i][j] * v[j] for j in range(n))
        for i in range(n)
    ]


def freivalds(A, B, C):
    n = len(A)
    x = [randint(0, 1000000) for j in range(n)]
    return mult(A, mult(B, x)) == mult(C, x)


if __name__ == "__main__":
    n = readint()
    A = readmatrix(n)
    B = readmatrix(n)
    C = readmatrix(n)
    print(freivalds(A, B, C))
```

Figyeljük meg a következő tesztet:

``` python
if __name__ == "__main__":
```

Ez `True` értékű, ha a kódot tartalmazó fájlt közvetlenül futtatjuk, és
`False`, ha a fájlt az `import` kulcsszó segítségével modul formájában
töltjük be.

### Feladat

**Enormous Input Test** `[spoj:INTEST]`

## 1.3.2 Kimeneti formátum

A program kimenetét a `print` függvénnyel jeleníthetjük meg.
Alapértelmezés szerint a `print` az argumentumok kiírása után új sort
kezd.

A sorvége kiírása kikapcsolható:

``` python
print(value, end='')
```

### Formázás a `%` operátorral

Rögzített pontosságú és szélességű számok megjelenítésének egyik módja a
`%` operátor, amely a C nyelv `printf` függvényéhez hasonlóan működik.

Példa:

``` python
>>> i_test = 1
>>> answer = 1.2142
>>> print("Case #%d: %.2f gigawatts!!!" % (i_test, answer))
Case #1: 1.21 gigawatts!!!
```

A `%d` egész számot jelöl, a `%f` lebegőpontos számot, a `%s` pedig
karakterláncot.

Százalékjel kiírásához:

``` text
%%
```

A típusjel előtt további formázási információ adható meg. Például:

``` text
%.2f
```

azt jelenti, hogy a tizedespont után két számjegyet jelenítünk meg.

### A `format()` metódus

Másik lehetőség a karakterlánc `format()` metódusa:

``` python
>>> print("Case #{}: {:.2f} gigawatts!!!".format(i_test, answer))
Case #1: 1.21 gigawatts!!!
```

Ez több formázási lehetőséget kínál, és általában könnyen kezelhető.

### f-stringek

Python 3.6-tól használhatók az úgynevezett **f-stringek**, azaz
formázott karakterlánc-literálok:

``` python
>>> print(f"Case #{i_test}: {answer:.2f} gigawatts!!!")
Case #1: 1.21 gigawatts!!!
```

A lebegőpontos pontosság akár változóval is megadható:

``` python
>>> precision = 2
>>> print(f"Case #{i_test}: {answer:.{precision}f} gigawatts!!!")
Case #1: 1.21 gigawatts!!!
```

Ebben a formában a formázási előírás közvetlenül az adott kifejezés
mellett jelenik meg.

------------------------------------------------------------------------

## Megjegyzés a fordításhoz

A fordításban a Python nyelvi elemeit, függvény- és változóneveit,
valamint a programkódokat nem magyarítottam. A fontosabb angol
szakkifejezéseknél -- például *slicing*, *immutable*, *heap*, *stack*,
*list comprehension* -- a magyar megfelelő mellett az eredeti terminust
is feltüntettem, hogy a dokumentum oktatási célra és angol nyelvű
dokumentációk használata mellett is jól használható legyen.
