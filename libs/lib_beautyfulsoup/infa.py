class Liczba:
    def __init__(self, number: str, system: int=2):
        self.num = number
        self.sys = system
    
    def __repr__(self):
        return str(self.num)
    
    def __add__(self, other):
        max_len = max([len(self.num), len(other.num)])
        num1 = self.num
        num2 = other.num

        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        forward = 0
        full = []
        for item_x, item_y in zip(num1[::-1], num2[::-1]):
            suma = int(item_x) + int(item_y) + forward
            if suma >= self.sys:
                forward = suma//self.sys
                suma -= self.sys
            else:
                forward=0
            full.append(suma)


        if forward > 0:
            full.append(forward)
        
        return full




x = Liczba("100")
y = Liczba("10")

print(x+y)
# x = input("Podaj liczbe 1: ")
# y = input("Podaj liczbe 2: ")


# # from itertools import zip_longest

# system = 2
# forward = 0
# full = []
# c = max([len(x), len(y)])

# print(c)
# x = x.zfill(c)
# y = y.zfill(c)

# print(x,y)

# for item_x, item_y in zip(x[::-1],y[::-1]):
#     item_x = item_x if item_x is not None else 0
#     item_y = item_y if item_y is not None else 0

#     suma = int(item_x) + int(item_y) + forward
#     if suma >= system:
#         forward = suma//system
#         suma -= system
#     else:
#         forward=0

#     full.append(suma)

# if forward > 0:
#     full.append(forward)

# print(full[::-1])

        