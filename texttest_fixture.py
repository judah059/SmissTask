# -*- coding: utf-8 -*-
from gilded_rose import *

if __name__ == "__main__":
    itemss = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=10),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Backstage passes", sell_in=10, quality=40),
             Item(name="Conjured", sell_in=3, quality=5),  # <-- :O
            ]
    gr = GildedRose(itemss)
    gr.update_quality()
    for item in gr.items:
        print(item.name + ' ' + str(item.sell_in) + ' ' + str(item.quality))
    gr.update_quality()
    for item in gr.items:
        print(item.name + ' ' + str(item.sell_in) + ' ' + str(item.quality))
