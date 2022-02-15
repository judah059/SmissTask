# -*- coding: utf-8 -*-
from gilded_rose import *

if __name__ == "__main__":
    itemss = [
             CustomItem("+5 Dexterity Vest", 10, 20, True),
             CustomItem("Aged Brie", 2, 10, True),
             CustomItem("Elixir of the Mongoose", 5, 3),
             CustomItem("Backstage passes", 0, 40),
             CustomItem("Conjured", 3, 5),  # <-- :O
             CustomItem("Sulfuras", 10, 80)
            ]
    gr = GildedRose(itemss)
    gr.update_quality()
    for item in gr.items:
        print(item.name + ' ' + str(item.sell_in) + ' ' + str(item.quality))
    gr.update_quality()
    for item in gr.items:
        print(item.name + ' ' + str(item.sell_in) + ' ' + str(item.quality))
