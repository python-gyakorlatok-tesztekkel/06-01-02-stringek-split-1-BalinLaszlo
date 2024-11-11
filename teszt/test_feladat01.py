from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestEBetukSzama(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.ebetuk_szama("eeeaaaeee")
        elvart = 6
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az e betűk számát")
    def test_feladat02(self):
        aktualis = feladatok.ebetuk_szama("eabcdfgh")
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az e betűk számát")
    def test_feladat03(self):
        aktualis = feladatok.ebetuk_szama("abcdfghe")
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az e betűk számát")
    def test_feladat04(self):
        aktualis = feladatok.ebetuk_szama("abcdfgh12fdsd")
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az e betűk számát")
    def test_feladat00(self):
        aktualis = feladatok.ebetuk_szama("")
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az e betűk számát")
