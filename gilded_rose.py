# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_brie_or_backstage(self, item):
        if item.name == 'Backstage passes':
            if item.quality < 50:
                if item.sell_in <= 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    if item.quality == 49:
                        item.quality += 1
                    elif item.quality == 48:
                        item.quality += 2
                    else:
                        item.quality += 3
                elif item.sell_in <= 10:
                    if item.quality <= 48:
                        item.quality += 2
                    else:
                        item.quality += 1
                else:
                    item.quality += 1
        else:
            if item.quality < 50:
                item.quality += 1
        item.sell_in -= 1
        return item


    def update_conjured_item(self, item):
        if item.quality > 1:
            item.quality = item.quality - 2
        elif item.quality == 1:
            item.quality = item.quality - 1
        elif item.quality <= 0:
            pass 
        item.sell_in -= 1
        return item


    def update_quality(self):
        # for item in self.items:
        #     if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
        #         if item.quality > 0:
        #             if item.name != "Sulfuras, Hand of Ragnaros":
        #                 item.quality = item.quality - 1
        #     else:
        #         if item.quality < 50:
        #             item.quality = item.quality + 1
        #             if item.name == "Backstage passes to a TAFKAL80ETC concert":
        #                 if item.sell_in < 11:
        #                     if item.quality < 50:
        #                         item.quality = item.quality + 1
        #                 if item.sell_in < 6:
        #                     if item.quality < 50:
        #                         item.quality = item.quality + 1
        #     if item.name != "Sulfuras, Hand of Ragnaros":
        #         item.sell_in = item.sell_in - 1
        #     if item.sell_in < 0:
        #         if item.name != "Aged Brie":
        #             if item.name != "Backstage passes to a TAFKAL80ETC concert":
        #                 if item.quality > 0:
        #                     if item.name != "Sulfuras, Hand of Ragnaros":
        #                         item.quality = item.quality - 1
        #             else:
        #                 item.quality = item.quality - item.quality
        #         else:
        #             if item.quality < 50:
        #                 item.quality = item.quality + 1

        for item in self.items:
            if item.name == 'Aged Brie' or item.name == 'Backstage passes':
                self.update_brie_or_backstage(item)
            elif item.name == 'Conjured':
                self.update_conjured_item(item)
            elif item.name == 'Sulfuras':
                item.sell_in = item.sell_in
                item.quality == item.quality
            else:
                if item.quality == 0:
                    pass
                else:
                    item.quality -= 1
                item.sell_in -= 1
        return self.items


class Item:
    def __init__(self, name, sell_in, quality):
        if quality <= 0:
            try:
                raise Exception('quality must be greater than zero')
            except Exception as e:
                print(str(e))
        if name != 'Sulfuras' and quality > 50:
            raise Exception('quality must be lower or equal 50')
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
