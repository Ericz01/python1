def total(gold, silver, copper):
    return (gold * 10 + silver) * 10 + copper

coins = [100, 50, 25]

#print(total(coins[0], coins[1], coins[2]), 'copper coins')
print(total(*coins), 'copper coins')