# Python – Szótárak (`dict`) – komplex gyakorlófeladatok

A feladatsor célja a Python **szótár (`dict`) adatszerkezetének gyakorlása** nagyobb adathalmazokon.

A feladatok az emelt szintű digitális kultúra érettségi programozási feladatainak jellegét követik. Minden feladatban fájlból kell adatokat beolvasni, azokat megfelelő adatszerkezetben tárolni, majd különböző lekérdezéseket és statisztikákat készíteni.

A forrásállományok:

```text
bufe.txt
kolcsonzesek.txt
verseny.txt
meresek.txt
konyvek.txt
kolcsonzes.txt
```

A szövegfájlok:

* UTF-8 kódolásúak;
* az adatokat pontosvessző (`;`) választja el;
* nem tartalmaznak fejlécet.

---

# 1. Iskolai büfé

Egy középiskolai büfé egy hónap alatt történt vásárlásainak adatai állnak rendelkezésre a `bufe.txt` állományban.

Az állomány **820 vásárlás adatait** tartalmazza.

Egy sor például:

```text
2026-09-03;10A;ÁSVÁNYVÍZ;2;350
```

Az adatok jelentése sorrendben:

```text
dátum;osztály;termék;darabszám;egységár
```

A fenti sor szerint 2026. szeptember 3-án a 10A osztály egy tanulója 2 darab ásványvizet vásárolt 350 Ft-os egységáron.

## Feladatok

### 1. feladat – Beolvasás

Olvassa be a `bufe.txt` állomány adatait, és tárolja azokat a további feladatok megoldására alkalmas adatszerkezetben!

### 2. feladat – Vásárlások száma

Határozza meg és írja ki, hány vásárlás adata szerepel az állományban!

Például:

```text
2. feladat
A hónapban 820 vásárlást rögzítettek.
```

### 3. feladat – Bevétel

Határozza meg a büfé teljes havi bevételét!

Ügyeljen arra, hogy egy vásárlás során ugyanabból a termékből több darabot is vásárolhattak!

### 4. feladat – Termékek forgalma

Határozza meg, hogy az egyes termékekből összesen hány darabot adtak el!

Az eredmény tárolásához használjon szótárat!

Például:

```python
{
    "ÁSVÁNYVÍZ": 187,
    "SZENDVICS": 143,
    "KAKAÓ": 98
}
```

Írja ki a termékek nevét és az eladott darabszámokat!

### 5. feladat – Legnépszerűbb termék

Határozza meg, melyik termékből adták el a legtöbb darabot!

Írja ki a termék nevét és az eladott mennyiséget!

### 6. feladat – Osztályok költése

Határozza meg, hogy az egyes osztályok tanulói összesen hány forintot költöttek!

Az eredményt szótárban tárolja!

### 7. feladat – Legtöbbet költő osztály

Határozza meg, melyik osztály tanulói költötték összesen a legtöbb pénzt a büfében!

### 8. feladat – Napi bevétel

Határozza meg minden nap teljes bevételét!

A dátumokat és a hozzájuk tartozó bevételeket tárolja szótárban!

### 9. feladat – Legforgalmasabb nap

Határozza meg, melyik napon volt a büfé bevétele a legnagyobb!

### 10. feladat – Termék keresése

Kérjen be a felhasználótól egy terméknevet!

Írja ki, hogy a megadott termékből összesen hány darabot adtak el!

Ha a termék nem szerepel az adatok között, erről is tájékoztassa a felhasználót!

### 11. feladat – Osztályok kedvenc terméke

Határozza meg minden osztály esetében azt a terméket, amelyből az adott osztály tanulói a legtöbb darabot vásárolták!

A megoldás során célszerű egymásba ágyazott szótárat használni.

### 12. feladat – Statisztika fájlba

Készítse el a `bufe_statisztika.txt` állományt!

Az állomány tartalmazza az osztályok nevét és az általuk elköltött összeget az összeg szerint **csökkenő sorrendben**!

---

# 2. Kerékpárkölcsönző

Egy város automata kerékpárkölcsönző rendszert működtet.

A júliusi kölcsönzések adatai a `kolcsonzesek.txt` állományban találhatók.

Az állomány **700 kölcsönzés adatait** tartalmazza.

Egy sor például:

```text
K023;2026-07-01;08:13;A12;D05;27
```

Az adatok jelentése:

```text
kerékpár azonosítója;dátum;indulási idő;induló állomás;érkező állomás;időtartam
```

Az időtartam percben értendő.

## Feladatok

### 1. feladat – Beolvasás

Olvassa be és tárolja a `kolcsonzesek.txt` állomány adatait!

### 2. feladat – Kölcsönzések száma

Határozza meg a júliusban történt kölcsönzések számát!

### 3. feladat – Összes használati idő

Határozza meg, hogy a kerékpárokat összesen hány percig használták!

### 4. feladat – Átlagos kölcsönzési idő

Számítsa ki egy kölcsönzés átlagos időtartamát!

Az eredményt egy tizedesjegyre kerekítve jelenítse meg!

### 5. feladat – Leghosszabb kölcsönzés

Határozza meg a leghosszabb kölcsönzés adatait!

Írja ki:

* a kerékpár azonosítóját;
* a dátumot;
* az indulási időt;
* az időtartamot.

### 6. feladat – Kerékpárok használata

Készítsen szótárat, amely megadja minden kerékpár esetében, hogy hányszor kölcsönözték ki!

### 7. feladat – Leggyakrabban használt kerékpár

Határozza meg, melyik kerékpárt kölcsönözték ki a legtöbbször!

### 8. feladat – Kerékpárok száma

Határozza meg, hány különböző kerékpárt használtak a hónap során!

### 9. feladat – Induló forgalom

Határozza meg állomásonként, hogy hány kölcsönzés indult az adott állomásról!

### 10. feladat – Legforgalmasabb indulási állomás

Határozza meg azt az állomást, ahonnan a legtöbb kölcsönzés indult!

### 11. feladat – Érkező forgalom

Határozza meg állomásonként az oda érkező kerékpárok számát!

Adja meg azt az állomást is, ahová a legtöbb kerékpár érkezett!

### 12. feladat – Kerékpárok összes használati ideje

Határozza meg minden kerékpár teljes kölcsönzési idejét!

Az eredményt szótárban tárolja!

### 13. feladat – Sokat használt kerékpárok

Írja ki azoknak a kerékpároknak az azonosítóját, amelyek összes használati ideje meghaladta a 300 percet!

### 14. feladat – Napi forgalom

Határozza meg minden nap kölcsönzéseinek számát!

### 15. feladat – Legforgalmasabb nap

Határozza meg, melyik napon történt a legtöbb kölcsönzés!

### 16. feladat – Nettó kerékpárforgalom

Egy állomás nettó kerékpárforgalma:

```text
érkező kerékpárok száma - induló kerékpárok száma
```

Határozza meg minden állomás nettó kerékpárforgalmát!

Adja meg:

* azt az állomást, ahol legjobban nőtt a kerékpárok száma;
* azt az állomást, ahol legjobban csökkent a kerékpárok száma.

---

# 3. Programozási verseny

Egy országos programozási verseny eredményei a `verseny.txt` állományban találhatók.

Az állomány **300 versenyző eredményét** tartalmazza.

Például:

```text
KOV123;Diósgyőri Gimnázium;Miskolc;11;78;64;92;81
```

A mezők:

```text
azonosító;iskola;város;évfolyam;1. feladat;2. feladat;3. feladat;4. feladat
```

Minden feladatra legfeljebb 100 pont szerezhető.

## Feladatok

### 1. feladat – Beolvasás

Olvassa be a `verseny.txt` állomány adatait!

### 2. feladat – Versenyzők száma

Írja ki a versenyen részt vevő tanulók számát!

### 3. feladat – Összpontszám

Határozza meg minden versenyző összpontszámát!

### 4. feladat – Győztes

Határozza meg a legmagasabb összpontszámot elért versenyző azonosítóját, iskoláját és pontszámát!

### 5. feladat – Városok

Készítsen szótárat, amely megadja, hogy az egyes városokból hány versenyző érkezett!

### 6. feladat – Legtöbb versenyzőt küldő város

Határozza meg, melyik városból érkezett a legtöbb versenyző!

### 7. feladat – Iskolák

Határozza meg iskolánként a versenyzők számát!

### 8. feladat – Legnagyobb létszámú iskola

Határozza meg, melyik iskola indította a legtöbb versenyzőt!

### 9. feladat – Iskolai átlagok

Határozza meg minden iskola esetében az ott tanuló versenyzők összpontszámának átlagát!

A megoldás során célszerű olyan szótárat létrehozni, amelyben egy iskolához több adat tartozik.

Például:

```python
iskolak = {
    "Diósgyőri Gimnázium": {
        "pont": 1245,
        "db": 5
    }
}
```

### 10. feladat – Legeredményesebb iskola

Határozza meg, melyik iskola versenyzőinek volt a legmagasabb az átlagpontszáma!

### 11. feladat – Évfolyamok

Határozza meg külön-külön a 9., 10., 11. és 12. évfolyamos versenyzők átlagpontszámát!

### 12. feladat – Legnehezebb feladat

Számítsa ki a négy versenyfeladatra kapott pontszámok átlagát!

Tekintse azt a feladatot a legnehezebbnek, amelynek a legalacsonyabb az átlagpontszáma!

Írja ki a feladat sorszámát és átlagpontszámát!

### 13. feladat – Városok legjobbjai

Határozza meg minden város legeredményesebb versenyzőjét!

### 14. feladat – Ranglista

Készítse el a `ranglista.txt` állományt!

Az állomány a verseny **20 legeredményesebb versenyzőjét** tartalmazza összpontszám szerint csökkenő sorrendben!

---

# 4. Időjárási mérőállomások

Nyolc magyarországi mérőállomás egy teljes éven keresztül végzett napi méréseket.

Az adatokat a `meresek.txt` állomány tartalmazza.

Az állomány **2920 rekordból** áll.

Egy sor:

```text
2025-01-01;Miskolc;-3.2;82;3.4;0.0
```

A mezők:

```text
dátum;állomás;hőmérséklet;páratartalom;szélsebesség;csapadék
```

A hőmérséklet Celsius-fokban, a páratartalom százalékban, a szélsebesség m/s-ban, a csapadék milliméterben szerepel.

## Feladatok

### 1. feladat – Beolvasás

Olvassa be a `meresek.txt` állomány adatait!

### 2. feladat – Mérések száma

Határozza meg az állományban található mérések számát!

### 3. feladat – Minimum-hőmérséklet

Határozza meg az év során mért legalacsonyabb hőmérsékletet!

### 4. feladat – A minimum helye

Adja meg, hogy melyik mérőállomáson és melyik napon mérték az előző feladatban meghatározott minimumot!

### 5. feladat – Maximum-hőmérséklet

Határozza meg az év legmagasabb mért hőmérsékletét, valamint a mérés helyét és dátumát!

### 6. feladat – Állomások adatai

Csoportosítsa a hőmérsékleti adatokat mérőállomásonként!

Használjon szótárat!

Például:

```python
{
    "Miskolc": [-3.2, -4.1, ...],
    "Eger": [-1.8, ...]
}
```

### 7. feladat – Éves átlag

Határozza meg minden mérőállomás éves átlaghőmérsékletét!

### 8. feladat – Legmelegebb állomás

Határozza meg, melyik állomáson volt a legmagasabb az éves átlaghőmérséklet!

### 9. feladat – Csapadék

Határozza meg minden állomás éves csapadékmennyiségét!

### 10. feladat – Legcsapadékosabb állomás

Melyik mérőállomáson hullott összesen a legtöbb csapadék?

### 11. feladat – Fagyos napok

Határozza meg állomásonként azoknak a napoknak a számát, amikor a mért hőmérséklet 0 °C alatt volt!

### 12. feladat – Csapadékos napok

Határozza meg minden állomás esetében azoknak a napoknak a számát, amikor legalább 1 mm csapadék hullott!

### 13. feladat – Országos napi hőmérséklet-különbség

Egy adott nap **országos hőmérséklet-különbsége** legyen az aznap mért legmagasabb és legalacsonyabb hőmérséklet különbsége.

Csoportosítsa a méréseket dátum szerint!

Például:

```python
{
    "2025-01-01": {
        "Miskolc": -3.2,
        "Eger": -1.8,
        "Győr": 1.2
    }
}
```

Határozza meg, melyik napon volt a legnagyobb országos hőmérséklet-különbség!

Írja ki:

* a dátumot;
* a minimum-hőmérsékletet;
* a maximum-hőmérsékletet;
* a kettő különbségét.

---

# 5. Iskolai könyvtár

Egy középiskolai könyvtár kölcsönzési adatai állnak rendelkezésre.

A feladat megoldásához két állományt kell használni:

```text
konyvek.txt
kolcsonzes.txt
```

## A könyvek adatai

A `konyvek.txt` **180 könyv adatait** tartalmazza.

Például:

```text
B017;Egri csillagok;Gárdonyi Géza;regény
```

A mezők:

```text
könyv azonosítója;cím;szerző;kategória
```

## A kölcsönzések adatai

A `kolcsonzes.txt` **1000 kölcsönzés adatait** tartalmazza.

Például:

```text
2026-01-14;1023;B017;2026-01-28
```

A mezők:

```text
kölcsönzés dátuma;tanuló azonosítója;könyv azonosítója;visszahozás dátuma
```

## Feladatok

### 1. feladat – Beolvasás

Olvassa be mindkét állomány adatait!

A könyvek adatait célszerű olyan szótárban tárolni, amelynek kulcsa a könyv azonosítója.

### 2. feladat – Kölcsönzések száma

Határozza meg a kölcsönzések számát!

### 3. feladat – Olvasók száma

Határozza meg, hány különböző tanuló kölcsönzött legalább egyszer!

### 4. feladat – Kölcsönzött könyvek

Határozza meg, hány különböző könyvet kölcsönöztek ki legalább egyszer!

### 5. feladat – Könyvek népszerűsége

Határozza meg minden könyv esetében, hogy hányszor kölcsönözték ki!

Az eredményt szótárban tárolja!

### 6. feladat – Legnépszerűbb könyv

Határozza meg a legtöbbször kikölcsönzött könyv azonosítóját!

### 7. feladat – Könyvadatok összekapcsolása

A `konyvek.txt` adatai alapján írja ki az előző feladatban meghatározott könyv:

* címét;
* szerzőjét;
* kölcsönzéseinek számát.

### 8. feladat – Legaktívabb olvasó

Határozza meg minden tanuló kölcsönzéseinek számát!

Adja meg annak a tanulónak az azonosítóját, aki a legtöbb könyvet kölcsönözte!

### 9. feladat – Kategóriák

Határozza meg kategóriánként a kölcsönzések számát!

Ehhez kapcsolja össze a két forrásállomány adatait a könyv azonosítója alapján!

### 10. feladat – Legnépszerűbb kategória

Határozza meg, melyik kategóriába tartozó könyveket kölcsönözték ki a legtöbbször!

### 11. feladat – Szerzők

Határozza meg szerzőnként a könyveikhez tartozó összes kölcsönzés számát!

### 12. feladat – Legnépszerűbb szerzők

Írja ki az öt legnépszerűbb szerző nevét és kölcsönzéseik számát, csökkenő sorrendben!

### 13. feladat – Havi forgalom

Határozza meg, hogy az egyes hónapokban hány kölcsönzés történt!

### 14. feladat – Legforgalmasabb hónap

Határozza meg, melyik hónapban történt a legtöbb kölcsönzés!

### 15. feladat – Sokoldalú olvasók

Határozza meg minden tanuló esetében, hogy hány **különböző kategóriába tartozó** könyvet kölcsönzött!

Írja ki azoknak a tanulóknak az azonosítóját, akik legalább 5 különböző kategóriából kölcsönöztek!

Ehhez célszerű a `dict` mellett `set` adatszerkezetet is használni.

### 16. feladat – Közös olvasók

Készítsen olyan adatszerkezetet, amely minden könyvhöz tartalmazza azoknak a tanulóknak az azonosítóját, akik a könyvet legalább egyszer kikölcsönözték!

Például:

```python
{
    "B017": {"1023", "1051", "1087"},
    "B081": {"1023", "1098"}
}
```

### 17. feladat – Hasonló olvasótábor

Keresse meg azt a két **különböző könyvet**, amelyet a legtöbb azonos tanuló kölcsönzött ki!

Egy tanulót csak egyszer vegyen figyelembe akkor is, ha ugyanazt a könyvet többször kikölcsönözte!

Írja ki:

* mindkét könyv azonosítóját;
* mindkét könyv címét;
* a közös olvasók számát.

---

# Javaslat a megoldáshoz

A feladatok megoldásakor törekedjen a megfelelő adatszerkezet megválasztására.

Különösen hasznosak lehetnek:

```python
lista = []

szotar = {}

halmaz = set()
```

Szótár értékeként lista, halmaz vagy akár egy másik szótár is tárolható:

```python
adatok = {
    "10A": {
        "SZENDVICS": 23,
        "ÁSVÁNYVÍZ": 41
    }
}
```

A feladatok egy része megoldható kizárólag listák használatával is, azonban ahol egy **azonosítóhoz, névhez, dátumhoz vagy kategóriához valamilyen összesített értéket kell rendelni**, ott érdemes megvizsgálni a `dict` használatának lehetőségét.


