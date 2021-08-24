
from logging import currentframe


class Hiker:
    valid_bills = [1,2,5,10,20,50,100]
    cents = 0
    bill = False
    QUARTERS = 'Q'
    DIMES = 'D'
    NICKLES = 'N'
    PENNIES = 'P'
    cents_in_coins = {
        PENNIES: 1,
        NICKLES: 5,
        DIMES: 10,
        QUARTERS: 25,                          
    }

    def __init__(self, value, is_bill=False, *args, **kwargs):
        super(Hiker, self).__init__(*args, **kwargs)
        self.bill = is_bill
        self.validate_value(value)
        if is_bill:    
            self.cents = value*100
        else:
            self.cents = value
            
    def ways_change(self, use_only=None):
        ways = []
        if use_only != None:
            val = self.cents/self.cents_in_coins[ use_only ]
            ways.append( self.format_cash_way(val, use_only) )
        else:
            ways = self.ways_change_all_coins(self.PENNIES)
                                
        return ways

    def ways_change_all_coins(self, startcoin):
        ways = []
        startcoin_cents = self.cents_in_coins[startcoin]
        if startcoin_cents < self.cents:
            mod = self.cents%startcoin_cents
            val = self.cents//startcoin_cents
            if mod == 0:
                ways.append( self.format_cash_way(val, startcoin) )
            
            for anothercoin, anothercoin_cents in self.cents_in_coins.items():
                if startcoin_cents < anothercoin_cents < self.cents:
                    
        
        return ways


    def format_cash_way(self, val, cash):
        return str( round(val) ) + cash

    def validate_value(self, value):
        if not isinstance(value, int): raise TypeError
        if self.bill and not value in self.valid_bills: 
            raise ValueError