# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, CustomItem

class GildedRoseTest(unittest.TestCase):
    def test_normal_item(self):
        items = [CustomItem("Some normal item", 10, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(5, items[0].quality)

    def test_conjured_item(self):
        items = [CustomItem("Some conjured item", 10, 6, True)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].quality)

    def test_brie(self):
        items = [CustomItem("Aged Brie", 10, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(7, items[0].quality)

    def test_backstage(self):
        items = [CustomItem("Backstage passes", 10, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)
    
    def test_sulfuras(self):
        items = [CustomItem("Sulfuras", 10, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(6, items[0].quality)

    def test_conjured_brie(self):
        items = [CustomItem("Aged Brie", 10, 6, True)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)

    def test_conjured_backstage(self):
        items = [CustomItem("Backstage passes", 10, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)





if __name__ == '__main__':
    unittest.main()
