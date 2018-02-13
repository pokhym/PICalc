import json
import urllib2 as ul
from copy import deepcopy
import datastructures as ds

# testing fuzzwork market data api
# https://market.fuzzwork.co.uk/api/
"""
**** HUB IDS ****
Jita 4-4 CNAP - 60003760
Amarr VIII - 60008494
Dodixie - 60011866
Rens - 60004588
Hek - 60005686
"""
region="60003760" # Jita

"""
**** P2 MATS ****
2329 : Biocells
Constructive Blocks
Consumer Electronics
Coolant
Enriched Uranium
Fertilizer
Gen. Enhanced Livestock
Livestock
Mechanical Parts
Microfiber Shielding
Minature Electronics
2463 : Nanites
Oxides
Polyaramids
Polytextiles
Rocket Fuel
Silicate Glass
Superconductors
2312 : Supertensile Plastics
Synthetic Oil
2319 : Test Cultures
9840 : Transmitter
Viral Agent
2328 : Water-Cooled CPU
"""
P2_types=["2329", "2463", "2312", "2319", "9840", "2328"]

"""
**** P4 MATS ****
Broadcast Node
Integrity Response Drones
Nano-Factory
Organic Mortar Applicators
Recursive Computing Module
Self-Harmonizing Power Core
Sterile Conduits
Wetware Mainframe
"""
P4_types="1"

def test():
    url="https://market.fuzzwork.co.uk/aggregates/?region="+region+"&types="+','.join(P2_types)
    get_req=ul.urlopen(url)
    json_struct=json.loads(get_req.read())

    # test item creation
    test_item=ds.ITEM()
    test_item.parse(json_struct["2329"], "2329")

    # test day creation
    test_day=ds.DAY()
    test_day.add_ITEM(test_item)
    test_item2=deepcopy(test_item)
    test_item2.sell_max=100000.0
    test_day.add_ITEM(test_item2)

    # test day averaging
    test_day.average_DAY()

    # test averaging result
    for attr, value in vars(test_day.item_dict_avg["2329"]).items():
        print attr, value

test()