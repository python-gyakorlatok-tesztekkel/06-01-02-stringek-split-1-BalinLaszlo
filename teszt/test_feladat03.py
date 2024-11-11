from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestHaromBetusSzavakSzama(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.harom_betus_szavak("Apa megy és edz")
        elvart = 2
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat03(self):
        aktualis = feladatok.harom_betus_szavak("Apa megy és edz de ha hoz kék pólót akkor kis ajándékot kap")
        elvart = 6
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat04(self):
        aktualis = feladatok.harom_betus_szavak("Apa")
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat05(self):
        aktualis = feladatok.harom_betus_szavak("Megy a gőzös Kanizsára vagy az állomásra")
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")
    def test_feladat06(self):
        aktualis = feladatok.harom_betus_szavak("")
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem jól határozta mega szavak számát")

