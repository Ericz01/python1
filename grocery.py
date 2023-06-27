groceries = {}

while True:
    try:
        item = input().upper()
        #check whether the item is already input. If yes, add count. else create it.
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    #when user inputs ctrl+d to end list
    except EOFError:
        for i in sorted(groceries):
            print(groceries[i], i)
        break
