# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("Conjured", 10, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals('ssolk', items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
