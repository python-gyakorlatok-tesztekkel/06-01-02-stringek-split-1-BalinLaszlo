from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestSzavakSzama(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.szavak_szama("Indul a bakterház")
        elvart = 3
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat02(self):
        aktualis = feladatok.szavak_szama("Megyen már a hajnal csillag lefelé. Az én édes galambom most megyen hazafelé")
        elvart = 13
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg a szavak számát")
    def test_feladat03(self):
        aktualis = feladatok.szavak_szama("Mindmegette")
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg a szavak számát")
    def test_feladat04(self):
        aktualis = feladatok.szavak_szama("")
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg a szavak számát")
