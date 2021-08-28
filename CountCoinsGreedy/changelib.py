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
        self.coin_list.push(name='Q', value=25) #QUARTERS
        self.coin_list.push(name='D', value=10) #DIMES
        self.coin_list.push(name='N', value=5) #NICKLES
        self.coin_list.push(name='P', value=1) #PENNIES

    def Change(self):
        current_node = self.coin_list.head
        previous_node = None
        done = False

        # restar o sumar para que llegue a 10, 20, 30...
        # recorrer todas las monedas y comprobar su divisibilidad:
        #  - la original y la decimal (ambas)
        # posteriormente realizar el recorrido que ya está escrito

        while not done or not current_node == None:
            if self.cents < current_node.value: done = True
            elif self.cents == current_node.value:
                current_node.amount = 1
                done = True
            elif not current_node.next == None or \
                self.cents < current_node.next.value:
                    current_node.amount = self.cents
                    done = True
            
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
    p = ChangeUS(1)
    print(p.Change())