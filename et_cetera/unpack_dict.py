def total(gold, silver, copper):
    return (gold * 10 + silver) * 10 + copper

coins = {'gold': 100, 'silver': 50, 'copper': 25}

#print(total(coins['gold'], coins['silver'], coins['copper']), 'copper coins')
print(total(**coins), 'copper coins')