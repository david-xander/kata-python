class CoinNodes:
    name = 'give a name'
    value = None
    amount = 0
    next = None
    def __init__(self, name, value, next_node=None):
        self.name = name
        self.value = value
        self.next = None

class CoinList:
    head = None

    def push(self, name, value):
        new = CoinNodes(name, value)
        new.next = self.head
        self.head = new

    def isEmpyt(self):
        return self.head == None


class ChangeUS:
    cents = 0
    coin_list = None

    def __init__(self, input, is_a_one_dollar_bill=False):
        
        if is_a_one_dollar_bill:
            self.cents = input * 100
        else:
            self.cents = input

        self.coin_list = CoinList()
        self.coin_list.push(name='P', value=1) #PENNIES
        self.coin_list.push(name='N', value=5) #NICKLES
        self.coin_list.push(name='D', value=10) #DIMES
        self.coin_list.push(name='Q', value=25) #QUARTERS

    def Change(self):
        current_node = self.coin_list.head
        previous_node = None
        cents = self.cents
        while not current_node == None:
            if cents < current_node.value: 
                pass
            elif cents == current_node.value:
                current_node.amount = 1
                cents -= current_node.value
            else:
                current_node.amount = cents//current_node.value
                cents = cents%current_node.value
            
            previous_node = current_node
            current_node = previous_node.next
        
        return self.PrintChange()

    def PrintChange(self):
        ans = []
        current_node = self.coin_list.head
        previous_node = None

        while not current_node == None:
            if current_node.amount > 0:
                ans.append(str(current_node.amount) + current_node.name)
            
            previous_node = current_node
            current_node = previous_node.next
        
        return ', '.join(ans)


if __name__ == '__main__':
    p = ChangeUS(98)
    print(p.Change())