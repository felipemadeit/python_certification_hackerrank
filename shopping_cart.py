class Item:

    def __init__(self, name:str, price:int):

        self.name = name
        self.price = price


class ShoppingCart:

    def __init__(self):
        self.cart = []


    def add(self, item: Item):
        self.cart.append(item)

    def total(self) -> int:
        return sum(item.price for item  in self.cart)
    
    def __len__(self):
        return len(self.cart)


if __name__ == '__main__':

    n = int(input())
    items = []

    for _ in range(n):

        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
            line = input().split()
            command, params = line[0], line[1:]
            if command == "len":
                print(str(len(cart)))
            elif command == "total":
                print(str(cart.total()))
            elif command == "add":
                name = params[0]
                item = next(item for item in items if item.name == name)
                cart.add(item)
            elif command == 'ShoppingCart':
                continue
            else:
                raise ValueError("Unknown command %s" % command)

            
