# -*- coding: utf-8 -*-

from unicodedata import name


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _update_backstage(self, item):
        if item.quality < 50:
            if item.sell_in <= 0:
                item.quality = 0
            elif item.sell_in <= 5:
                item.quality += 3
                if item.quality > 50:
                    item.quality = 50
            elif item.sell_in <= 10:
                item.quality += 2
                if item.quality > 50:
                    item.quality = 50
            else:
                item.quality += 1
        item.sell_in -= 1
        return item

    def _update_brie(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        return item


    def _update_conjured_item(self, item):
        if item.name == 'Aged Brie':
            self._update_brie(item)
            self._update_brie(item)
        elif item.name == 'Backstage passes':
            self._update_backstage(item)
            self._update_backstage(item)
        elif item.name == 'Sulfuras':
            self._update_sulfuras(item)
        else:
            if item.quality > 1:
                item.quality = item.quality - 2
            elif item.quality == 1:
                item.quality = item.quality - 1
            elif item.quality <= 0:
                pass 
            item.sell_in -= 1
        return item
    
    def _update_sulfuras(self, item):
        pass


    def update_quality(self):
        for item in self.items:
            if item.conjured:
                self._update_conjured_item(item)
            elif item.name == 'Aged Brie':
                self._update_brie(item)
            elif item.name == 'Backstage passes':
                self._update_backstage(item)
            elif item.name == 'Sulfuras':
                self._update_sulfuras(item)
            else:
                if item.quality == 0:
                    item.quality = 0
                else:
                    item.quality -= 1
                item.sell_in -= 1
        return self.items


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class CustomItem(Item):
    def __init__(self, name, sell_in, quality, conjured=False):
        self.conjured = conjured
        Item.__init__(self, name, sell_in, quality)
        if self.quality <= 0:
            raise ValueError('quality must be greater than zero')
        if self.name != 'Sulfuras' and self.quality > 50:
            raise Exception('quality must be lower or equal 50')
        