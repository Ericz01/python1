class Bank:
    def __init__(self, gold=0, silver=0, copper=0):
        self.gold = gold
        self.silver = silver
        self.copper = copper

    def __str__(self):
        return f'{self.gold} gold, {self.silver} silver, {self.copper} copper'

    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        copper = self.copper + other.copper
        
        return Bank(gold, silver, copper)
eric = Bank(100, 50, 25)
print(eric)

job = Bank(25, 50, 100)
print(job)

total = eric + job
print(total)