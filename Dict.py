


g = {
    'o':{'p':0, 'q':0},
    'm':{'p':0, 'q':0}
}

def additems(item, price, quat):
    g[item] ={
        'p':price,
        'q':quat
    }

def printitems():
    for items in g.keys():
        print(f'items {items} has price {g[items]["p"]} and quantity{g[items]["q"]}')


item = input('item >')
price = input("price >")
quat = input("quantity >")
additems(item, price, quat)
printitems()
