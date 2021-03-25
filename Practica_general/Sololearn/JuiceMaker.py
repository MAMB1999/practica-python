class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self,other):
        total_name = self.name +"$"+ other.name
        total_capacity = self.capacity + other.capacity
        return Juice(total_name,total_capacity)
a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

res = a+b
print(res)
