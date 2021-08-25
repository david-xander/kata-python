
from logging import NOTSET, currentframe


class Hiker:
    valid_bills = [1,2,5,10,20,50,100]
    cents = 0
    bill = False
    PENNIES = 'P'
    NICKLES = 'N'
    DIMES = 'D'
    QUARTERS = 'Q'
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
            ways = []
            for coin in self.cents_in_coins.keys():
                ways += self.ways_change_all_coins(self.cents, coin)
                                
        return ways


    def ways_change_all_coins(self, amount, starting_coin):
        ways = []
        index = list(self.cents_in_coins.keys()).index(starting_coin)
        value = self.cents_in_coins[starting_coin]
        if value <= amount:
            if amount%value == 0:
                val = amount/value
                text = self.format_cash_way(val, starting_coin)
                ways.append( text )
            
            for i in range(value, amount, value):
                the_rest = amount - i
                othercoins = list(self.cents_in_coins.items())[index+1:]
                for subcoin, subvalue in othercoins:
                    otherways = self.ways_change_all_coins(the_rest, subcoin)                          
                    for otherway in otherways:
                        text = self.format_cash_way(i/value, starting_coin)
                        ways.append( text + ' and ' + otherway )                        
        return ways

    def format_cash_way(self, val, cash):
        return str( round(val) ) + cash

    def validate_value(self, value):
        if not isinstance(value, int): raise TypeError
        if self.bill and not value in self.valid_bills: 
            raise ValueError

if __name__ == '__main__':
    h = Hiker(15)
    print(h.ways_change())
