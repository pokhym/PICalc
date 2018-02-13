"""
ITEM
Description: After a url request each item should be parsed into an ITEM class which contains
the fields as a float instead of a string returned by fuzzwork
"""
class ITEM:
    # initializes fields to 0.0
    def __init__(self, in_id=0):
        # sell orders
        self.id=in_id
        self.sell_min=0.0
        self.sell_max=0.0
        self.sell_orderCount=0.0
        self.sell_median=0.0
        self.sell_volume=0.0
        self.sell_percentile=0.0
        self.sell_stddev=0.0
        self.sell_weightedAverage=0.0
        
        # buy orders
        self.buy_min=0.0
        self.buy_max=0.0
        self.buy_orderCount=0.0
        self.buy_median=0.0
        self.buy_volume=0.0
        self.buy_percentile=0.0
        self.buy_stddev=0.0
        self.buy_weightedAverage=0.0
    
    # inserts the data into the fields
    def parse(self, json_object, in_id):
        try:
            self.id=in_id

            self.sell_min=float(json_object["sell"]["min"])
            self.sell_max=float(json_object["sell"]["max"])
            self.sell_orderCount=float(json_object["sell"]["orderCount"])
            self.sell_median=float(json_object["sell"]["median"])
            self.sell_volume=float(json_object["sell"]["percentile"])
            self.sell_stddev=float(json_object["sell"]["stddev"])
            self.sell_weightedAverage=float(json_object["sell"]["weightedAverage"])

            self.buy_min=float(json_object["buy"]["min"])
            self.buy_max=float(json_object["buy"]["max"])
            self.buy_orderCount=float(json_object["buy"]["orderCount"])
            self.buy_median=float(json_object["buy"]["median"])
            self.buy_volume=float(json_object["buy"]["percentile"])
            self.buy_stddev=float(json_object["buy"]["stddev"])
            self.buy_weightedAverage=float(json_object["buy"]["weightedAverage"])

            return 0 # parsed
        except:
            return 1 # error unable to parse data

"""
DAY
Description: This holds all the market data for a day uses a dictionary for storing the data,
dictionary key is the id of the item and the value is a list of all the data grabbed for the 
"""
class DAY:
    # __init__
    # constructor to initialize empty dictionaries
    def __init__(self):
        # key = item ID, value = list of ITEM class objects
        self.item_dict_all={}
        self.item_dict_avg={}
    
    # add_ITEM
    # adds an item to the all dictionary before we average the day
    # also creates key value pair in average dict if it doesn't exist
    def add_ITEM(self, in_item):
        # check if key exists if not
        if in_item.id in self.item_dict_all:
            self.item_dict_all[in_item.id].append(in_item)
        # add new key and empty list then append the new it
        else:
            self.item_dict_all.update({in_item.id : []})
            self.item_dict_avg.update({in_item.id : ITEM(in_item.id)})            
            self.item_dict_all[in_item.id].append(in_item)

    # average_DAY
    # averages all the items in a day this is shitty fucking code
    def average_DAY(self):
        for key in self.item_dict_all:
            # sum all daily values for all keys
            for item_data in self.item_dict_all[key]:
                for attr, value in vars(item_data).items():
                    if(attr!="id"):
                        setattr(self.item_dict_avg[item_data.id], attr,
                            getattr(self.item_dict_avg[item_data.id], attr)+value)
            # averaging loop
            for attr, value in vars(self.item_dict_avg[key]).items():
                if(attr!="id"):
                    setattr(self.item_dict_avg[key], attr, 
                        getattr(self.item_dict_avg[key], attr)/len(self.item_dict_all[key]))

"""
WEEK
"""

# FIXME: NOT SURE IF THE ALL BELOW NEED TO BE IN A CLASS

"""
PROCESS
"""
class PROCESS:
    def __init__(self):
        a=0
    
    # retrive_and_update
    # grabs data from api given region and in_types and assigns to the data structs
    def retrive_and_update(self, region, in_types):
        return 0
    
    # write_out
    # outputs all the data to a file daily
    def write_out(self, in_DAY):
        return 0

"""
PROFIT_CALC
"""
class PROFIT_CALC:
    def __init__(self):
        a=0
    
    # immediate_profit
    # will calculate profit margin based upon the last obtained market data
    def immediate_profit(self):
        # profit will be calculated from the newest lowest current buy order
        # (predicted sell price - invested amount) / invested amount = % profit
        # return predicted sell order price as the average minimum price
        return 0
    
    # daily_sell_profit
    # will calculate the profit margin based up on daily averaged sell order prices
    def daily_sell_profit(self):
        # predicted sell order price will be se as the average minimum price 
        # (predicted sell price - invested amount) / invested amount = % profit
        # return predicted sell order price as the average minimum price
        return 0
    
    # weekly_sell_profit
    # will calculate the profit margin based upon weekly averaged sell order prices
    def weekly_sell_profit(self, invested_amount):
        # predicted sell order price will be se as the average minimum price 
        # (predicted sell price - invested amount) / invested amount = % profit
        # return predicted sell order price as the average minimum price
        return 0

"""
PI_CALC
"""
class PI_CALC:
    def __init__(self):
        a=0
    
    # resources_req
    # inputs P4_type, item_DAILY prices, and time to run
    # it will calculate investment price and amount of resources required to run a specific time (hrs)
    # for the specific P4_type (probably use an enum)
    def resources_req(self, P4_type, item_DAILY, time):
        return 0